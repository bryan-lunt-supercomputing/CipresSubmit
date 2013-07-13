#!/usr/bin/env python
'''
Created on Jun 7, 2013

@author: blunt
'''

import os
import sys
import subprocess

def qsub(script_path,env,envarg=None,l=None,N=None,W=None,V=True,A=None,M=None):

	allArgs = ["qsub"]
	if l is not None:
		allArgs.append("-l")
		allArgs.append(l)
	if N is not None:
		allArgs.append("-N")
		allArgs.append(N)
	if W is not None:
		allArgs.append("-W")
		allArgs.append(W)
	if A is not None:
		allArgs.append("-A")
		allArgs.append(A)
	if M is not None:
		allArgs.append("-M")
		allArgs.append(M)
	if V:
		allArgs.append("-V")
	allArgs.append(script_path)

	localEnv = dict()
	localEnv.update(env)
	if envarg is not None:
		localEnv.update(envarg)

	localEnv = dict([(i,str(j)) for i,j in localEnv.iteritems() if j is not None])

	qsub_proc = subprocess.Popen(allArgs,env=localEnv,stdout=subprocess.PIPE)
	qsub_retval = qsub_proc.wait()

	qsub_stdout = qsub_proc.stdout.read()

	return qsub_retval, qsub_stdout.strip()


def submit_job_array(SCRIPT_PATH,env,jobname=None,nodes=1,ppn=16,walltime="1:00:00",array=1,array_sync=False):
	"""
	Job submission helper. May get broken out into own library later. For the moment, it is useful here.
	"""
	
	env["ARRAY_TOTAL"] = array

	if jobname is None:
		jobname = os.path.basename(SCRIPT_PATH)

	loption="nodes=%i:ppn=%i:native,walltime=%s" % (nodes, ppn, walltime)

	jobids = list()
	
	for ARRAY_JOB_INDEX in range(array):

		depend_option=None
		if ARRAY_JOB_INDEX == 0 and array > 1 and array_sync:
			depend_option="depend=synccount:%i"%(array-1)
		elif array > 1 and array_sync:
			depend_option="depend=syncwith:%i"%(int(jobids[0].split(".")[0])) #May seem convoluted, but casting it as an int ensures it really was a parsable int.


		qsubret, another_job = qsub(SCRIPT_PATH,env,envarg={"ARRAY_JOB_INDEX":str(ARRAY_JOB_INDEX)},l=loption,N=jobname+str(ARRAY_JOB_INDEX),W=depend_option,V=True)

		if qsubret != 0:
			#do something to cancel all the jobs
			raise Exception("qsub returned non-zero value: %i",qsubret)
		else:
			jobids.append(another_job)
		
	return jobids
