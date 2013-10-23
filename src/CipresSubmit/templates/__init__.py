'''
This package does nothing but hold the templates for job scripts.

'cmdfile.template' is a template that only runs the one command line program specified.
'runfile.template' is the outer run file that is submit to qsub.


The following names will be standard over templates:

User Templates must expect/use these:
	OTHERPBSHEADERS : Optional, but you should have a place for it in your script template.
	
	cluster_header : Optional, lines of bash script that you might add to the basic template (for example, to setup path and modules and things.)
					: It is discouraged to use this in any kind of per-job way.
	
	CIPRESNOTIFYURL
		threads_per_process
		total_threads
	
	command
	queuename
	jobname
	runtime : Given as a number of minutes
	email
	account
	nodes
	ppn
	jobdir : Absolute path for the job's directory



If you want to use the default templates:

	cmdfile : Relative or absolute path for the command file.



Created on Jul 3, 2013

@author: lunt
'''

import pkg_resources
import os.path

import pystache

def execute_template(template_string, *args, **kwargs):
	therenderer = pystache.Renderer(escape=lambda x:x)
	return therenderer.render(template_string, *args, **kwargs)

def load_template(template_filename,template_directory=None):
	'''
	Loads a template. If given as an absolute path, that path is loaded. Otherwise,
	templates are resolved first from the specified template_directory (if any), and lastly from those stored as resources with this package.
	'''
	filename_to_use = None
	load_resource   = False #Needed because the project might be stored in an egg, and then we can't get a resource by filename.
	if os.path.isabs(template_filename):
		filename_to_use = template_filename
	elif (template_directory is not None) and os.path.exists(os.path.join(template_directory,template_filename)):
		filename_to_use = os.path.join(template_directory,template_filename)
	elif pkg_resources.resource_exists(__name__,template_filename):
		load_resource=True
	
	if (filename_to_use == None) and (load_resource == False):
		raise Exception('Could not find the specified template to load.')
	
	if load_resource:
		return pkg_resources.resource_string(__name__,template_filename)
	else: #implies filename_to_use not None
		retstring = None
		with open(filename_to_use) as infile:
			retstring = infile.read()
		return retstring