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
import pystache

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
		options, cmdline = parser.parse_known_args(argv)
		cmdline = cmdline if not ('--' in cmdline) else cmdline[cmdline.index('--')+1:]
	except Exception as e:
		sub_log.log(e.message, "ERROR")
		sub_log.submit_fail("Incorrect options to submit.py")
	
	
	#READ BASIC CONFIGURATIONS
	
	cmdline_options        = options
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
	
	
	
	
	#TODO: This is where the submit system will choose a queue for the submitter, set nodes, set ppn, etc, etc
	the_queue, nodes, ppn = (resource_configuration.queues_dict['shared'], 1, 16) #Dummy values for testing.
	
	#TODO: With the queue chosen, we need to enforce maximum walltime
	#TOOD: With the number of cores chosen, we need to enforce maximum SU usage by altering the walltime.
	
	job_properties['queue'] = the_queue #Gets queuename and node_properties, though we might want to edit node_properties? (For example, some jobs might not need local storage, so asking for flash..
	job_properties['nodes'] = nodes
	job_properties['ppn'] = ppn
	
	job_properties['env_vars_string'] = ','.join(['%s=%s' % (i,j) for i,j in  job_properties['queue'].env_vars_dict.iteritems()])
	
	scheduler_properties['runminutes'] = int(ceil(float(scheduler_properties['runhours'])*60))
	
	
	#TODO: Execute the template.
	print "commandline_options", cmdline_options
	print "global_settings", global_settings
	print "all_resources", all_resources
	print "job_properties", job_properties
	print "scheduler_properties", scheduler_properties
	print "resource_configuration", resource_configuration

	the_renderer = pystache.Renderer()#missing_tags='strict')
	
	for template_entry in resource_configuration.templates:
		print """
###
%s
###""" % template_entry.name
		print the_renderer.render(template_entry.template,template_entry.parameters,global_settings,job_properties,scheduler_properties, cmdline_options, {'cmdline':' '.join(cmdline)})
	

	import pdb
	pdb.set_trace()
	exit(1)
	
	
	
	
	#TODO: Actually submit the job.
	
	
	
	
	#TODO: How do we get back the qsub status? as an Exception, or a return type?
	#TODO: How do we get back the jobid? As another return value or, with another method call to the submitter?
	
	print "DEBUG INFO:"
	print "NUM CPUS : %i \n" % num_cpus
	
	print "Submitter : ", submitter

	print "CLUSTER INFO: ", cluster_info
	print "SCHEULER INFO: ", scheduler_properties


if __name__ == "__main__":
	exit(main(sys.argv))