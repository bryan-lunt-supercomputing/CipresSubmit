#!/usr/bin/env python
'''
Created on Jul 11, 2013

@author: lunt
'''
import os
import sys

from math import ceil as __ceil

import CipresSubmit.pyjavaproperties as Props
from CipresSubmit.SubmitLogger import SubmitLogger
import CipresSubmit.SubmitConfig as SConfig
import CipresSubmit.schema as SSchema
import CipresSubmit.templates as STemp
import CipresSubmit.SubmitEnv as SEnv
from CipresSubmit.SubmitEnv.__init__ import TooManyJobs

import stat



import subprocess
def submit_direct(cmdline, global_settings, resource_configuration, cmdline_options, job_properties, scheduler_properties):
	
	#breakign these out to separate lists gives us the option of making them empty if we want to omit something.
	ACCOUNT_OPTIONS = ['--account', job_properties.get('account',resource_configuration.account)]
	URL_OPTIONS = ['--url', cmdline_options.CIPRESNOTIFYURL]
	JOBEMAIL_OPTIONS = ['--email', global_settings['general']['job_status_email']]
	
	try:
		direct_submitter = subprocess.Popen(cmdline + ACCOUNT_OPTIONS + URL_OPTIONS + JOBEMAIL_OPTIONS, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderr   = direct_submitter.communicate()
		exit_value       = direct_submitter.returncode
	except Exception as e:
		raise SEnv.NotSubmit("Could not submit direct job: " + e.message)
	
	if exit_value != 0:
		raise SEnv.NotSubmit("Could not submit direct job:\n STDOUT: " + stdout + "\n\nSTDERR:\n" + stderr + "\n")
	
	firstline = stdout.splitlines()
	if len(firstline) <= 0:
		raise Exception("Job appeared to submit properly, but no STDOUT from direct job script.")
	
	JOBID = firstline[0].strip()
	return JOBID
	

def main(argv=sys.argv):
	"""
    Usage is:
    submit.py [--account <chargecode>] [--url <url>] -- <commandline> 
    Run from the working dir of the job which must contain (in addition
    to the job files) a file named scheduler.conf with scheduler properties for the job.

    <chargecode>, if present, gives the project to charge the job to.
    Url is the url of the submitting website including the taskid parameter.

    Returns 0 with "jobid=<jobid>" on stdout if job submitted ok
    Returns 1 with multiline error message on stdout if error.
    Returns 2 for the specific error of queue limit exceeded.
    """
	sub_log = SubmitLogger()
	
	#COMMAND LINE PARSING
	import argparse
	parser = argparse.ArgumentParser()
	
	
	parser.add_argument('--account', metavar="ACCOUNT", type=str,
					help="The account string to use when submitting jobs. Default is read from config files.")
	
	parser.add_argument('--url', metavar="URL", dest="CIPRESNOTIFYURL", type=str,
					help="Notification URL")
	
	parser.add_argument('--dry-run', dest='DRYRUN', action="store_true", help="Parse all inputs, build all outputs, don't submit job.")
	
	try:
		cmdline_options, cmdline = parser.parse_known_args(argv)
		cmdline = cmdline[1:] if not ('--' in cmdline) else cmdline[cmdline.index('--')+1:]
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("Incorrect options to submit.py")
		return 1
	
	
	#READ BASIC CONFIGURATIONS
	
	cmdline_options        = cmdline_options
	global_settings        = SConfig.load_configs();
	all_resources          = SConfig.load_all_resource_XMLs(global_settings['hosts']['resourcexmldir'])
	job_properties         = None
	scheduler_properties   = None
	resource_configuration = None
	
	#READ ENVIRONMENT
	#Read the _JOBINFO.TXT file
	try:
		job_properties = SConfig.load_jobinfo('_JOBINFO.TXT')
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("No '_JOBINFO.TXT' or it could not be parsed.")
		return 1
	
	if cmdline_options.account is not None:
		job_properties['account'] = cmdline_options.account
	
	#TODO: This is where we should execute the pre-run script. I guess.
	#Doing it here would allow a pre-run script to alter scheduler.conf, if it wants to.
	#TOOLNAME_prerun cmdline
	
	
	#Read the scheduler.conf file
	try:
		scheduler_properties = SConfig.load_scheduler_conf('scheduler.conf')
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("No 'scheduler.conf' or it could not be parsed.")
		return 1
	
	
	#_JOBINFO.TXT has told us what resource we are running on, so open that resource
	resource_configuration = SSchema.Resource(all_resources[job_properties['resource']])
	
	#ENVIRONMENT IS PREPARED
	
	#Direct jobs finish here.
	if scheduler_properties['jobtype'] == "direct":
		try:
			jobid = submit_direct(cmdline, global_settings, resource_configuration, cmdline_options, job_properties, scheduler_properties)
			sub_log.submit_success(jobid)
			return 0
		except Exception as ns:
			sub_log.log(ns.message,"ERROR")
			sub_log.submit_fail("Problem submitting direct job.")
			return 1
	

	
	
	
	#
	#CHOOSE THE QUEUE
	#
	myBatchSystem = SEnv.get_batch_instance(resource=resource_configuration)
	the_queue, nodes, ppn = myBatchSystem.choose_queue(scheduler_properties)
	scheduler_properties['queue'] = the_queue #Gets queuename and node_properties, though we might want to edit node_properties? (For example, some jobs might not need local storage, so asking for flash..
	scheduler_properties['nodes'] = nodes
	scheduler_properties['ppn'] = ppn
	
	
	#TODO: With the number of cores chosen, we need to enforce maximum SU usage by altering the walltime.
	
	scheduler_properties['runminutes'] = int(__ceil(float(scheduler_properties['runhours'])*60))
	
	
	#Execute all templates
	created_files = list()										#keep track of what files we've created, needed for submission
	for template_entry in resource_configuration.templates:
		created_files.append(template_entry.name)				#keep track of what files we've created, needed for submission
		with open(template_entry.name,"w") as outfile:			#context manager for the template output file
			template_string = STemp.load_template(template_entry.filename,global_settings['templates']['templatedir'])
			outfile.write( STemp.execute_template(template_string,
											template_entry.parameters,
											{'job_status_email': global_settings['general']['job_status_email']},
											resource_configuration,
											{'CIPRESNOTIFYURL':cmdline_options.CIPRESNOTIFYURL},
											job_properties,
											{'env_vars_string':','.join(['%s=%s' % (i,j) for i,j in  scheduler_properties['queue'].env_vars_dict.items()])},
											scheduler_properties,
											{'cmdline':' '.join(cmdline)})
						)
		os.chmod(template_entry.name,stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH ) #make the template executable
	
	
	
	if cmdline_options.DRYRUN:
		jobid = "8888888.test"
	else:
		#Actually submit the job, which should be the first template.
		jobid=None
		try:
			jobid = myBatchSystem.submit(created_files[0], scheduler_properties)
		except TooManyJobs as too:
			sub_log.log(too.message,"ERROR")
			sub_log.submit_fail("There were too many jobs enqueued.",status=2)
			return 2
		except Exception as e:
			sub_log.log(e.message,"ERROR")
			sub_log.submit_fail("There was some error submitting the job to the cluster system")
			return 1
		
	
	#EXIT with success
	sub_log.jobid = jobid
	sub_log.submit_success(cores=scheduler_properties['nodes']*scheduler_properties['ppn'],ChargeFactor=the_queue.charge_factor)
	return 0


if __name__ == "__main__":
	exit(main(sys.argv))