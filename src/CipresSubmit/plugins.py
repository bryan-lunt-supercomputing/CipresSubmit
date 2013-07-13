#!/usr/bin/env python
'''
Created on Jul 11, 2013

@author: lunt
'''
import os
import sys
import warnings
import subprocess
import pkgutil
import pystache

def load_appropriate_plugin(path,cluster_info,cmdline,job_properties,properties={}):
	"""
	This function is overly trusting of the modules it finds, and uses old-style module loading.
	
	I had wanted to use a nice plugin system, but then I was concerned that we might not be able to install it on cypres host locations.
	
	Based on this answer from stack overflow: http://stackoverflow.com/a/8556471
	
	It expects each plugin module to have a function that will test its appropriateness, and either return a JobPlugin instance, None, or raise an exception.
	
	"""
	warnings.filterwarnings('ignore')
	retPlugin = None
	for	importer, pname, _ in pkgutil.iter_modules([path]):
		try:
			full_package_name = '%s.%s' % (path,pname)
			m = importer.find_module(pname).load_module(full_package_name)
			candidate = m.check_appropriate(cluster_info,cmdline,job_properties,properties)
			if candidate is not None:
				retPlugin = candidate
		except:
			pass
	warnings.filterwarnings('default')
	
	#Defaults in case no plugin found
	if retPlugin is None:
		if(properties.get('jobtype','') == 'direct' or properties.get('is_direct',False)):
			retPlugin = DirectJobPlugin(cluster_info,cmdline,job_properties,properties)
		else:
			retPlugin = TemplateJobPlugin(cluster_info,cmdline,job_properties,properties)
			
	return retPlugin

class JobPlugin(object):
	"""
	A Default job plugin, it obeys everything from the CIPRES gateway, and it never thinks of thinking for itself at all.
	"""
	
	def __init__(self,clusterinfo,commandLine,job_properties,properties={}):
		self.cluster = clusterinfo
		self.job_properties = job_properties
		self.properties=properties #: See the files DEV_NOTES/scheduler_conf.txt, this properties may also later contain: 'queue', 'ppn'
		self.cmdLine = commandLine
		
	def validate(self):
		"""
		
		@return : True if input valid, False if invalid
		@rtype : boolean
		"""
		return True
	
	def parallel_rules(self):
		"""
		@precondition : validate has been called.
		
		@return : Total number of CPUs to use, None for "don't care".
		"""
		return int(self.properties.get('nodes',1))*int(self.properties.get('threads_per_process',1))*int(self.properties.get('mpi_processes',1))
	
	def submitJob(self):
		"""
		@precondition : parallel_rules has been called()
		@precondition : The queue we should use has been selected by outside code.
						It shall be the responsibility of _this_ code to adjust its expectations based on the final number of nodes/cpus for this queue.
		
		@return : Final Job Properties
		"""
		raise NotImplementedError("You must implement this in a subclass")


class DirectJobPlugin(JobPlugin):
	
	def parallel_rules(self):
		"""
		Direct jobs are responsible for this themselves.
		"""
		return None
	
	def submitJob(self):
		assert False, "this needs to be fixed"#TODO : fix the next line
		cmdLine = self.cmdLine + " --account %s --url %s --email %s" % (self.job_properties['account'], self.job_properties['CIPRESNOTIFYURL'], self.job_properties['email'])
		directscript = subprocess.Popen(cmdLine,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		direct_exitcode = directscript.wait()
		
		#TODO: Log stdout/stderr
		
		return direct_exitcode

class TemplateJobPlugin(JobPlugin):
	"""
	If overriding classes would like to make use of the submission system here, they can populate self.templates
	with a list of tuples
	('filename',Template as STR, {'other':'properties'})
	
	Each template is rendered using this JobPlugin's parameters, job_properties, etc. properties specific to a single template (discouraged, but sometimes necessary.) may be provided in the third position of the tuple.
	That rendered template is saved to Filename.
	
	The first file in the list is the one that will get qsubbed.
	
	"""
	
	def __init__(self,clusterinfo,commandLine,job_properties,properties={}):
		JobPlugin.__init__(self,clusterinfo,commandLine,job_properties,properties)
		
		self.parameters = dict()
		self.cmdfile = './batch_command.cmdline'
		self.batchfilename = 'batch_command.run'
		self.templates = list()
	
	def add_template(self,filename,template_object,additional_properties={}):
		self.templates.append((filename,template_object,additional_properties))
	
	def submitJob(self):
		"""
		Uses the templating engine to make script files and submit them.
		
		"""
		
		#setup parameters
		self.parameters['command'] = self.cmdLine
		
		#load default templates if not already loaded.
		if len(self.templates) == 0:
			self.add_template(self.batchfilename,pkgutil.get_data('CipresSubmit.templates','runfile.template'))
			self.add_template(self.cmdfile,pkgutil.get_data('CipresSubmit.templates','cmdfile.template'))
		
		
		
		submitParams = dict()
		submitParams.update(self.cluster)
		submitParams.update(self.job_properties)
		submitParams.update(self.parameters)

		
		
		#do templates
		myRenderer = pystache.Renderer()
		
		for destfilename, template, other_properties in self.templates:
			renderedTemplate = myRenderer.render(template,submitParams,**other_properties)
			destfullpath = os.path.join(self.job_properties['jobdir'],destfilename)
			with open(destfullpath,'w') as foofile:
				foofile.write(renderedTemplate)
			os.chmod(destfullpath,0754)
		
		#TODO: actually submit the job.
	