#!/usr/bin/env python
# import test_lib as lib
import lib
import sys
import os

def main(argv=None):
    """
    Usage is:
    submit.py [id=<chargecode>] <url> <commandline> 
    Run from the working dir of the job which must contain (in additoin
    to the job files) a file named scheduler.conf with scheduler properties for the job.

    id=<chargecode> if present gives the project to charge the job to.
    Url is url of the submitting website including taskid parameter.

    Returns 0 with "jobid=<jobid>" on stdout if job submitted ok
    Returns 1 with multiline error message on stdout if error.
    Returns 2 for the specific error of queue limit exceeded.
    """
    if argv is None:
        argv=sys.argv

    splits = argv[1].split("=", 1)
    if (len(splits) == 2 and splits[0] == "id"):
        account = splits[1]
        url = argv[2]
        cmdline = argv[3:]
    else:
        account = lib.account 
        url = argv[1]
        cmdline = argv[2:]
    tooltype = lib.getToolType(cmdline)

    scheduler_properties = lib.getProperties("scheduler.conf")
    # print scheduler_properties
    scheduler_info = lib.schedulerInfo(scheduler_properties, tooltype)
    # print scheduler_info

    # If this is a "direct" run type job we don't need to create a qsub script, we'll just run batch_ommand.cmdline.
    if scheduler_info["is_direct"]:
        return lib.submitDirectJob(account, url, lib.email, lib.jobname, cmdline)


    runtime = int(scheduler_info["runtime"])
    useLocalDisk = False

    """
    Workaround for problems with file io on oasis and longer mrbayes runs.  Instead of running on 
    oasis, we'll copy the working dir to the compute nodes local storage and copy the results back 
    when the job completes.  Since many mrbayes jobs timeout we need a special trick to copy results
    of jobs that timeout: Right before we launch mrbayes we launch a shell script in the background 
    that sleeps a few min less than the job's runtime and then copies the results.  If mrbayes terminates
    normally the background sleep is killed automatically.  
    """
    if (tooltype == "mrbayes" and runtime > 60):
        useLocalDisk = True
    
    # I'm backing out the workaround by setting useLocalDisk to false.  
    useLocalDisk = False


    # Write the command line to a file, batch_command.cmdline.
    rfile = open(lib.cmdfile, "w") 
    rfile.write("#!/bin/sh\n")
    rfile.writelines((" ".join(cmdline), "\n"))
    rfile.close()
    os.chmod(lib.cmdfile, 0744);




    # Create the qsub script
    rfile = open(lib.runfile, "w") 

    text = """#!/bin/sh
#PBS -q %s
#PBS -N %s
#PBS -l walltime=00:%d:00
#PBS -o scheduler_stdout.txt
#PBS -e scheduler_stderr.txt
#PBS -W umask=0007
##PBS -V

#PBS -v QOS=2

#PBS -M  %s
#PBS -m ae
#PBS -A %s
""" % (scheduler_info["queue"], lib.jobname,  scheduler_info["runtime"], lib.email, account)
    rfile.write(text)

    text = "#PBS -l nodes=%d:ppn=%d\n" % (scheduler_info["nodes"], scheduler_info["ppn"])
    rfile.write(text)

    rfile.write("cd %s\n" % (lib.jobdir, lib.local_jobdir)[useLocalDisk])
    if useLocalDisk == True:

        # Note that it's critical that newlines in the text string are all within the double
        # quotes; otherwise the echo command line would be split across lines and make no sense.
        text = """"Due to filesystem problems intermediate results for longer mrbayes runs
will not be available while the job is running.  The result files will be
available when mrbayes finishes. 

We're working to find a solution." """ 
        rfile.write("echo  %s > %s/INTERMEDIATE_RESULTS_README.TXT\n" % (text, lib.jobdir))

        rfile.write("cp -r %s/* .\n" % lib.jobdir);
        sleepTime = int(scheduler_info["runtime"]) - 10 
        rfile.write("sleep_cp.sh %s %s &\n" % (sleepTime, lib.jobdir))
    text = """
source /etc/profile.d/modules.sh
echo Job starting at `date` > start.txt
curl %s\&status=START
export CIPRES_THREADSPP=%d
export CIPRES_NP=%d
%s 1>stdout.txt 2>stderr.txt
echo Job finished at `date` > done.txt
""" % (url, 
        int(scheduler_info["threads_per_process"]), 
        int(scheduler_info["ppn"]) * int(scheduler_info["nodes"]),
        lib.cmdfile)
    rfile.write(text)

    if (useLocalDisk):
        text = """
echo "Job completed, starting to copy working directory."
echo "mkdir %s.complete"
mkdir %s.complete

echo "cp -r * %s.complete"
cp -r * %s.complete

echo "mv %s %s.sleep"
mv %s %s.sleep

echo "mv %s.complete %s"
mv %s.complete %s

echo "rm -rf %s.sleep"
rm -rf %s.sleep

echo "Finished copying working directory."
""" % (lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir, lib.jobdir)
        rfile.write(text)

    rfile.write("curl %s\&status=DONE\n" %  url)
    rfile.close()

    return lib.submitJob()
    return 0

if __name__ == "__main__":
    sys.exit(main())
