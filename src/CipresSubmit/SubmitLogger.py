"""
THis should be modified to be a python "logging" logger.
"""

import os
import urllib.request, urllib.parse, urllib.error
import json

class SubmitLogger(object):
	"""
	This class does double duty as both a storage container for environment, and a logging/notification system.
	Perhaps this isn't a good idea...
	"""
	def __init__(self,jobdir=os.getcwd(),url=None):
		self.jobid = "00000" #Placeholder
		self.jobdir = jobdir
		self.jobname = os.environ.get("WB_JOBID", "")
		self.url = url
		self.messages = list()
		self.data = {'messages':self.messages}
		self.jobinfofilename = '_JOBINFO.TXT'

	def log(self,message,messagetype="INFO"):
		self.messages.append("%s : %s" % (messagetype,message) )

	def notify(self,status):
		"""
		Later on we want to break notification out into a Strategy Pattern. It may not always be via URL....
		
		(But, in that case, you should have SubmitEnvironment setup some of the command line options. There is a limit to how much we can break out into config scripts.)
		
		But, for the moment:
		"""
		try:
			connection = urllib.request.urlopen(self.url+"&%s"%status)
			connection.read()
			connection.close()
		except:
			pass

	def write_errorfile(self):
		with open(os.path.join(self.jobdir,"stderr.txt"),"wc") as errfile:
			for m in self.messages:
				errfile.write(str(m) + "\n")

	def format_json(self):
		return json.dumps(self.data,indent=4, separators=(',', ': '))
	

	def submit_fail(self,message):
		if status != 2:
			self.notify("START")
			self.notify("DONE")
		
		self.log(message,"FAILURE")
		self.write_errorfile()

		print(message)
		print(self.format_json())

	def submit_success(self,jobid=None,cores=None,message=None,ChargeFactor=None):
		if jobid is None:
			jobid = self.jobid
		
		#Write jobid back to _JOBINFO.TXT
		try: 
			with open(self.jobinfofilename,"a") as JOBINFO_FILE:
				if ChargeFactor is not None:
					JOBINFO_FILE.write("\nChargeFactor=%s" % ChargeFactor )
				if cores is not None:
					JOBINFO_FILE.write("\ncores=%s" % cores )
				JOBINFO_FILE.write("\nJOBID=%s\n" % jobid )
		except:
			self.log("Unable to write to _JOBINFO.TXT, but the job was submitted, so we can't back out now.","ERROR")
		
		
		print("jobid=%i" % int(jobid.split('.')[0]))
		
		
		if message is not None:
			self.log(message,"SUCCESS")
		
		print(self.format_json())
