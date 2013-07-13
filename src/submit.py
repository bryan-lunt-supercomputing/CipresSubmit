#!/usr/bin/env python
'''
Created on Jul 11, 2013

@author: lunt
'''
import os
import sys

import CipresSubmit.pyjavaproperties as Props
from CipresSubmit.SubmitLogger import SubmitLogger
import CipresSubmit.SchedulerEnv as SEnv

import CipresSubmit.plugins as CipresPlugins

def main(argv=sys.argv):
	"""
    Usage is:
    submit.py [id=account] <url> <commandline> 
    Run from the working dir of the job which must contain (in addition
    to the job files) a file named scheduler.conf with scheduler properties for the job.

    id=<chargecode> if present gives the project to charge the job to.
    Url is url of the submitting website including taskid parameter.

    Returns 0 with "jobid=<jobid>" on stdout if job submitted ok
    Returns 1 with multiline error message on stdout if error.
    Returns 2 for the specific error of queue limit exceeded.
    """
		
	#Load Settings from a well-known settings file.
	#in the meantime
	
	global_settings = {'plugin_path':'./plugins', 'account':'TG-DEB090011'}
	
	#TODO: Load Global Settings. The hosts.json file might be elsewhere.
	cluster_info = SEnv.get_current_host_config()
	
	#now we can parse the input, because we have a default account.
	splits = argv[1].split("=", 1)
	if (len(splits) == 2 and splits[0] == "id"):
		account = splits[1]
		url = argv[2]
		cmdline = argv[3:]
	else:
		account = cluster_info.get('account',global_settings.get('account',None))
		url = argv[1]
		cmdline = argv[2:]
	
	cmdline = " ".join(cmdline)
	
	sub_log = SubmitLogger(url=url)
	
	job_properties = {'account':account,'jobid':'0000','jobdir':os.getcwd()}
	
	#Read the scheduler.conf file
	scheduler_properties = Props.Properties()
	try:
		scheduler_properties.load(open("scheduler.conf"))
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("No 'scheduler.conf' or it could not be parsed.")
	
	
	#find the appropriate plugin
	try:
		submitter = CipresPlugins.load_appropriate_plugin(global_settings['plugin_path'], cluster_info, cmdline, job_properties, scheduler_properties)
		if submitter == None:
			raise Exception("No Valid Submission Plugin at all?")
	except Exception as e:
			sub_log.submit_fail(e.message)
			exit(1)
	
	#By here, we are guaranteed a valid "submitter" object.
	
	#TODO: These need to be wrapped in some exception handling / logging.
	input_valid = submitter.validate()
	#TOOD: If the input is invalid, fail.
	
	num_cpus	= submitter.parallel_rules()
	
	#TODO: This is where the submit system will choose a queue for the submitter, set nodes, set ppn, etc, etc
	#TODO: It should also extend job_properties with that queue's "additional_properties" 
	the_queue, nodes, ppn = SEnv.choose_queue(num_cpus, cluster_info)
	
	#TODO: With the queue chosen, we need to enforce maximum walltime
	#TOOD: With the number of cores chosen, we need to enforce maximum SU usage by altering the walltime.
	
	job_properties.update(the_queue)#Gets queuename and node_properties, though we might want to edit node_properties? (For example, some jobs might not need local storage, so asking for flash..
	job_properties['nodes'] = nodes
	job_properties['ppn'] = ppn
	
	submitter.submitJob()
	#TODO: How do we get back the qsub status? as an Exception, or a return type?
	#TODO: How do we get back the jobid? As another return value or, with another method call to the submitter?
	
	print "DEBUG INFO:"
	print "NUM CPUS : %i \n" % num_cpus
	
	print "Submitter : ", submitter

	print "CLUSTER INFO: ", cluster_info
	print "SCHEULER INFO: ", scheduler_properties


if __name__ == "__main__":
	exit(main(sys.argv))