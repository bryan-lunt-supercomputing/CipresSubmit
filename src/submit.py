#!/usr/bin/env python
'''
Created on Jul 11, 2013

@author: lunt
'''

import sys

import CipresSubmit.pyjavaproperties as Props
from CipresSubmit.SubmitLogger import SubmitLogger

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
	
	#Load Settings
	
	
	splits = argv[1].split("=", 1)
	if (len(splits) == 2 and splits[0] == "id"):
        account = splits[1]
        url = argv[2]
        cmdline = argv[3:]
    else:
        account = None
        url = argv[1]
        cmdline = argv[2:]
	
	
	sub_log = SubmitLogger()
	
	
	scheduler_properties = Props.Properties()
	scheduler_properties.load(open("scheduler.conf"))



if __name__ == "__main__":
	exit(main(sys.argv))