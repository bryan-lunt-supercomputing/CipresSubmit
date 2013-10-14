#!/usr/bin/env python
'''
Created on Jul 11, 2013

@author: lunt
'''
import os
import sys

from math import ceil

import CipresSubmit.pyjavaproperties as Props
from CipresSubmit.SubmitLogger import SubmitLogger
import CipresSubmit.SubmitConfig as SConfig
import CipresSubmit.schema as SSchema
import CipresSubmit.templates as STemp
import CipresSubmit.SubmitEnv as SEnv
from CipresSubmit.SubmitEnv.__init__ import TooManyJobs

import stat

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
	sub_log = SubmitLogger()
	
	#COMMAND LINE PARSING
	import argparse
	parser = argparse.ArgumentParser()
	
	
	parser.add_argument('--account', metavar="ACCOUNT", type=str,
					help="The account string to use when submitting jobs. Default is read from config files.")
	
	parser.add_argument('--url', metavar="URL", dest="CIPRESNOTIFYURL", type=str,
					help="Notification URL")
	
	try:
		cmdline_options, cmdline = parser.parse_known_args(argv)
		cmdline = cmdline[1:] if not ('--' in cmdline) else cmdline[cmdline.index('--')+1:]
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("Incorrect options to submit.py")
	
	
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
	
	if cmdline_options.account is not None:
		job_properties['account'] = cmdline_options.account
	
	#Read the scheduler.conf file
	try:
		scheduler_properties = SConfig.load_scheduler_conf('scheduler.conf')
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("No 'scheduler.conf' or it could not be parsed.")
	
	
	#_JOBINFO.TXT has told us what resource we are running on, so open that resource
	resource_configuration = SSchema.Resource(all_resources[job_properties['resource']])
	
	#ENVIRONMENT IS PREPARED
	
	
	
	
	#TODO: This is where we should execute the pre-run script. I guess.
	#TOOLNAME_prerun cmdline
	
	
	
	#
	#CHOOSE THE QUEUE
	#
	myBatchSystem = SEnv.get_batch_instance(resource=resource_configuration)
	the_queue, nodes, ppn = myBatchSystem.choose_queue(scheduler_properties)
	scheduler_properties['queue'] = the_queue #Gets queuename and node_properties, though we might want to edit node_properties? (For example, some jobs might not need local storage, so asking for flash..
	scheduler_properties['nodes'] = nodes
	scheduler_properties['ppn'] = ppn
	
	
	#TOOD: With the number of cores chosen, we need to enforce maximum SU usage by altering the walltime.
	
	scheduler_properties['runminutes'] = int(ceil(float(scheduler_properties['runhours'])*60))
	
	
	#Execute all templates
	created_files = list()
	for template_entry in resource_configuration.templates:
		created_files.append(template_entry.name)
		with open(template_entry.name,"w") as outfile:
			template_string = STemp.load_template(template_entry.filename,global_settings['templates']['templatedir'])
			outfile.write( STemp.execute_template(template_string,
											template_entry.parameters,
											global_settings,
											resource_configuration,
											{'CIPRESNOTIFYURL':cmdline_options.CIPRESNOTIFYURL},
											job_properties,
											{'env_vars_string':','.join(['%s=%s' % (i,j) for i,j in  scheduler_properties['queue'].env_vars_dict.iteritems()])},
											scheduler_properties,
											{'cmdline':' '.join(cmdline)})
						)
		os.chmod(template_entry.name,stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH )
	
	
	
	
	#Actually submit the job, which should be the first template.
	jobid=None
	try:
		jobid = myBatchSystem.submit(created_files[0], scheduler_properties)
		jobid = jobid.strip()
	except TooManyJobs as too:
		sub_log.log(too.message,"ERROR")
		sub_log.submit_fail("There were too many jobs enqueued.",status=2,terminate=True)
	except Exception as e:
		sub_log.log(e.message,"ERROR")
		sub_log.submit_fail("There was some error submitting the job to the cluster system",terminate=True)
		
	
	#Write jobid back to _JOBINFO.TXT
	try: 
		with open("_JOBINFO.TXT","a") as JOBINFO_FILE:
			JOBINFO_FILE.write("\nJOBID=%s\n" % jobid)
	except:
		sub_log.log("Unable to write to _JOBINFO.TXT, but the job was submitted, so we can't back out now.","ERROR")
	
	
	sub_log.jobid = jobid.split('.')[0]
	sub_log.submit_success()


if __name__ == "__main__":
	exit(main(sys.argv))