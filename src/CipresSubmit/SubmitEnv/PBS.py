'''
Created on Oct 4, 2013

@author: lunt
'''

from CipresSubmit.SubmitEnv.__init__ import BatchEnvironment

class PBSBatchEnvironment(BatchEnvironment):
	"""
	Implementation of BatchEnvironment for PBS systems.
	
	"""
	def __init__(self):
		super(PBSBatchEnvironment, self).__init__()
	
	def submit(self,jobfilename,scheduler_properties):
		print "We would submit the job here: qsub %s" % jobfilename
		return True