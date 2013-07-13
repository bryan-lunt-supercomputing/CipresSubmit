import os
import string
import math
import re
import subprocess

# I didn't implement getProperties, found it somewhere, just reads a java style
# properties file into a dictionary.
def getProperties(filename):
    propFile= file( filename, "rU" )
    propDict= dict()
    for propLine in propFile:
        propDef= propLine.strip()
        if len(propDef) == 0:
            continue
        if propDef[0] in ( '!', '#' ):
            continue
        punctuation= [ propDef.find(c) for c in ':= ' ] + [ len(propDef) ]
        found= min( [ pos for pos in punctuation if pos != -1 ] )
        name= propDef[:found].rstrip()
        value= propDef[found:].lstrip(":= ").rstrip()
        propDict[name]= value
    propFile.close()
    # print propDict
    return propDict

def getToolType(commandlineString):
    if re.search(r'garli', "".join(commandlineString).lower()):
        return "garli"
    elif re.search(r'raxml', "".join(commandlineString).lower()):
        return "raxml"
    elif re.search(r'mbhwrapper', "".join(commandlineString).lower()):
        return "mrbayes"
    elif re.search(r'beast', "".join(commandlineString).lower()):
        return "beast"
    return None 
    



# There's only one queue.  Max runtime should be 2 weeks  hrs (which is 336 hrs or 20160 minutes) for user cipres.  Not
# sure what it is for other users. CHANGE: also using "shared" queue now. 
shared_queue = "shared"
shared_queue_limit = 20160.0
short_queue = "normal"
queues = (("normal", 20160.0), )
cores_per_node = 32 
# Effectively get rid of max_nodes by setting it to 5000
max_nodes = 5000
max_cores = max_nodes * cores_per_node
default_cores = cores_per_node
account = "TG-DEB090011"
# account = "ddp116"
scheduler_file = "scheduler.conf"

email = "terri@sdsc.edu"

jobname = ""
runfile = "./batch_command.run"
statusfile = "./batch_command.status"
cmdfile = "./batch_command.cmdline"

jobdir = os.getcwd()
local_jobdir = "/scratch/cipres/$PBS_JOBID"

jobname = os.environ.get("WB_JOBID", "cipres")

def schedulerInfo(properties, tooltype):
    """ properties is a dictionary containing keys: 
    jobtype, mpi_processes, threads_per_process, nodes, runhours.
    Based on properties and hardcoded info about the resource this returns a dictionary
    containing:
    is_direct, is_mpi, queue, runtime, mpi_processes, nodes, ppn"""


    # get runhours from properties and convert it to minutes, default to zero if not specified.
    try:
        runtime  = properties.get("runhours", 0.0)
        runtime = math.ceil(float(runtime) * 60 )
    except:
        runtime = 0.0

    qname = 0
    qlimit = 1
    # if runtime is 0 (which isn't really valid), change it to limit for the shortest queue
    # so we have something reasonable to work with.
    if runtime == 0.0:
        runtime = queues[qname][qlimit]

    # based on runtime, figure out which queue we should be using.
    queue = None
    for entry in queues:
        if runtime <= entry[qlimit]:
            queue = entry[qname] 
            break
    if queue == None:
        queue = queues[-1][qname] 
        runtime = queues[-1][qlimit]

    # Create retval and set values we just determined for runtime and queue.  Set defaults for some
    # if the other retvals which may be overriden below.  Note that for serial jobs we'll need to set nodes=1
    # and ppn=1 in the job run script.
    retval =    {"runtime":runtime, "queue":queue, "threads_per_process":int(properties.get("threads_per_process", 0)),
                 "nodes": int(properties.get("nodes", 1)), "ppn": int(1)}

    if properties.get("jobtype") == "direct":
        retval["is_direct"]  = True 
        return retval
    else:
        retval["is_direct"] = False

    if properties.get("jobtype", "")  == "mpi":
        retval["is_mpi"]  = True 
    else:
        retval["is_mpi"] = False 

    if (retval["is_mpi"] == True):
        # Some of our pise xml interfaces just specify the number of mpi processes they want. 
        # We round it down to a multiple of the number of cores per node and request enough nodes
        # so that each mpi process has its own core.
        #
        # Not sure if we still have any interfaces like I just described but it's definitely not
        # how we want to run garli here, so explicitly exclude it.  Garli just specifies
        # the number of mpi processes but we always want to use a single node for it.
        if (properties.get("nodes", "") == "") and (properties.get("thread_per_process", "") == "") and tooltype != "garli":
            processes = int(properties.get("mpi_processes", 1))
            processes = int(processes / cores_per_node) * cores_per_node
            processes = min(max(processes, default_cores), max_cores)
            retval["nodes"] = processes / cores_per_node 
            retval["mpi_processes"] = processes 
            retval["ppn"] = int(retval["mpi_processes"]) / int(retval["nodes"]);
        # Pise interfaces that have more knowledge of the specific machine explicitly specify
        # the number of nodes as well as the number of mpi processes; we don't 2nd guess them.
        else:
            retval["nodes"] = int(properties.get("nodes", 1));
            retval["mpi_processes"] = int(properties.get("mpi_processes", 1));
            retval["ppn"] = int(retval["mpi_processes"]) / int(retval["nodes"]);

        # Special case for garli.  Run small jobs in shared queue.
        if (tooltype == "garli") and (retval["mpi_processes"] < cores_per_node):
            retval["queue"] = shared_queue
            if runtime > shared_queue_limit:
                runtime = shared_queue_limit
                retval["runtime"] = runtime
    else:
        # Special case for small, non-mpi raxml jobs, run in the shared queue.  Also for beast
        if (retval["nodes"] == 1) and ((retval["threads_per_process"] == 8) or (tooltype == "beast")):
            queue = shared_queue
            retval["queue"] = queue
            retval["ppn"] = retval["threads_per_process"]
            if runtime > shared_queue_limit:
                runtime = shared_queue_limit
                retval["runtime"] = runtime


    return retval

def log(filename, message):
    f = open(filename, "a")
    f.write(message)
    f.close()

def deleteJob(jobid, workingdir):
    if os.path.isfile(workingdir + "/cancelJobs"):
        os.chdir(workingdir)
        cmd = "./cancelJobs %d" %  jobid
    else:
        cmd = "qdel %d" % jobid
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outerr = p.communicate()
    output =  outerr[0]
    err = outerr[1]
    if (p.returncode != 0):
        raise SystemError("Error running '%s', return code is %d. stdout is '%s', stderr is '%s'" % (cmd,  
            p.returncode, output, err))

def jobInQueue():
    cmd = "qstat"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outerr = p.communicate()
    output =  outerr[0]
    err = outerr[1]
    if (p.returncode != 0):
        raise SystemError("Error running qstat, return code is %d. stderr is %s" % (p.returncode, err))
    if (len(err) != 0):
        raise SystemError("Error running qstat, stderr is %s" % (err))
    if (len(output) < 5):
        raise SystemError("Error running qstat, output looks wrong: %s" % (output))

    # cmd = 'echo "%s" | grep `whoami`' % output
    cmd = 'grep `whoami`' 
    p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    outerr = p.communicate(output)
    output =  outerr[0]
    err = outerr[1]

    if (len(err) != 0):
        raise SystemError("Error piping qstat thru grep:  %s" % (err))

    output_rows = output.split("\n")
    jobs = [] 
    for row in output_rows:
        r = row.split()
        if len(r) > 4 and r[4] != "C":
            r[0] = r[0].split(".", 1)[0]
            jobs.append(r[0])
    

    return jobs




# To do: modify RAxML-Light.sh to accept --url argument and pass it here, like --account.  Decide whether
# to use --email too, maybe just on the last job?  Or ask Mark if he wants all the emails?
def submitDirectJob(account, url, email, jobname, commandline):
    # Not exactly a general purpose solution but for raxml-light we can just add account, email and url 
    # arguments to the command line.

    rfile = open(cmdfile, "w") 
    rfile.write("#!/bin/sh\n")
    rfile.write(" ".join(commandline))
    rfile.write(" --account %s" % account)
    rfile.write(" --url %s" % url)
    rfile.write(" --email %s" % email)
    rfile.write("\n")
    rfile.close()
    os.chmod(cmdfile, 0744);

    cmd = cmdfile
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  
    output =  p.communicate()[0]
    retval = p.returncode
    if retval != 0:
        print "Error submitting job:\n"
        print output 
        log(statusfile, "submitDirectJob is returning %d.\nStdout/stderr is:%s\n" %  (retval, output))

        # When there's a bash syntax error in a script it exits with 2, but if we return 2, we've
        # defined that to mean "too many jobs queued" and cipres will print a special message.
        if (retval == 2):
            retval = 1
        return retval
    log(statusfile, "Job submission stdout/stderr is: %s\n" % output) 

    # output should be just the full job id, <id>.trestles-fe1.sdsc.edu:
    firstline = output.splitlines()
    if len(firstline) == 1:
        firstline = firstline[0]
        p = re.compile(r"^(\d+).trestles.\S+", re.M)
        m = p.search(output)
        if m != None:
            jobid = m.group(0)
            short_jobid = m.group(1)
            print "jobid=%d" % int(short_jobid)
            log(statusfile, "JOBID is %s\n" % jobid)
            log("./_JOBINFO.TXT", "\nJOBID=%s\n" % jobid)
            return 0
    print "Error, job submission says: %s" % output
    log(statusfile, "can't find jobid, submitDirectJob is returning 1\n")
    return 1
    


# Returns 0 on success, 2 means too many jobs queued.
def submitJob():  
    cmd = "qsub %s 2>> %s" % (runfile, statusfile)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)  
    output =  p.communicate()[0]
    retval = p.returncode
    if retval != 0:
        # read whatever qsub wrote to the statusfile and print it to stdout
        print "Error submitting job:\n"
        f = open(statusfile, "r"); print f.read(), "\n\n"; f.close()
        print output 

        # When we return 2 it means too many jobs are queued.  qstat returns -226 on abe
        # in this situation ... not sure if that's true here, on trestles as well.
        if retval == -226:
            retval = 2

        log(statusfile, "submit_job is returning %d\n" %  retval)

        return retval
    log(statusfile, "qsub output is: " + output + "\n" + 
        "======================================================================" +  "\n")

    # output from qsub should on trestles is just the full job id, <id>.trestles-fe1.sdsc.edu:
    p = re.compile(r"^(\d+).trestles.\S+", re.M)
    m = p.search(output)
    if m != None:
        jobid = m.group(0)
        short_jobid = m.group(1)
        print "jobid=%d" % int(short_jobid)
        log(/, "JOBID is %s\n" % jobid)
        log("./_JOBINFO.TXT", "\nJOBID=%s\n" % jobid)
        return 0
    else:
        print "Error, qsub says: %s" % output
        log(statusfile, "can't get jobid, submit_job is returning 1\n")
        return 1

