'''
Created on Oct 4, 2013

@author: lunt
'''

from CipresSubmit.SubmitEnv.__init__ import BatchEnvironment, TooManyJobs, NotSubmit
import subprocess

class PBSBatchEnvironment(BatchEnvironment):
	"""
	Implementation of BatchEnvironment for PBS systems.
	
	"""
	def __init__(self):
		super(PBSBatchEnvironment, self).__init__()
	
	def submit(self,jobfilename,scheduler_properties):
		try:
			qsub_proc = subprocess.Popen(['qsub',jobfilename],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
			qsub_retval = qsub_proc.wait()
			qsub_stdout = qsub_proc.stdout.read()
			qsub_stderr = qsub_proc.stderr.read()
		except Exception as e:
			raise NotSubmit("Error invoking qsub: " + e.message + " " + e.strerror)
		
		if qsub_retval in [-226,30,157]:#Various error codes indicationg too many jobs on PBS implementations
			raise TooManyJobs("Too Many Jobs Enqueued.")
		
		if qsub_retval != 0:
			raise NotSubmit("Some error.: " + qsub_stderr)
		
		return qsub_stdout