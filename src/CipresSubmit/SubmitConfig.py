'''
Created on Oct 3, 2013

@author: Bryan Lunt
'''

from . import pyjavaproperties as Props

import pkg_resources

import configparser as CFGP
import os
import os.path

import CipresSubmit.schema as SubmitXML
import CipresSubmit.hosts as DefaultSubmitHosts

def __config_to_str_dict(config):
	"""
	Convert a config object to a str->str dict.
	"""
	retdict = dict([
				(sect_name,
					dict( config.items(sect_name) )
				)
				for sect_name in config.sections()])
	return retdict

def load_configs():
	"""
	Load the most basic config files.
	
	Loads "cipressubmit.cfg" from the python packages, then "~/.cipresssubmit.cfg" from the user's home directory, then "cipresssubmit.cfg" from the current directory.
	
	Each subsequent file overrides the last one.
	"""
	baseconfig = CFGP.ConfigParser()
	#setup defaults.
	baseconfig.add_section('general')
	baseconfig.set('general','job_status_email',"")
	baseconfig.add_section('templates')
	baseconfig.set('templates','templatedir',"")
	baseconfig.add_section('hosts')
	baseconfig.set('hosts','resourcexmldir',"")
	#Load a global submit configuration but allow it to be overridden by a local configuration
	
	baseconfig.readfp(pkg_resources.resource_stream(__name__,"cipressubmit.cfg"),"default_config")
	readfiles      = baseconfig.read([os.path.expanduser('~/.cipressubmit.cfg'), 'cipressubmit.cfg' ])
	
	return __config_to_str_dict(baseconfig)

#Defaults for java .properties type files

scheduler_conf_defaults = {"jobtype":"serial",
						"mpi_processes":1,
						"threads_per_process":1,
						"runhours":0.5,
						"node_exclusive":0,
						"nodes":None,
						"ppn":1,
						"queue":None}

jobinfo_txt_defaults = {"Task label":None,
					"Task ID":None,
					"Tool":None,
					"created on":None,
					"JobHandle":None,
					"User ID":None,
					"User Name":None,
					"email":None,
					"JOBID":None,
					"resource":None,
					'Output':None}#"ChargeFactor" and "cores" should not be in the file when submit.py is parsing it.

def __load_properties(filename,defaults=dict(),error_on_unknown=False):
	"""
	Helper method for loading properties files with defaults.
	
	If a default of _None_ is given, then there is no default, but that name is recognized and does not raise an error.
	"""
	default_properties = Props.Properties()
	for key, default_val in defaults.items():
		if default_val is not None:
			default_properties.setProperty(key,str(default_val))
	
	with open(filename) as infile:
		default_properties.load(infile)
	
	if error_on_unknown:
		for onename in default_properties.propertyNames():
			if onename not in defaults:
				raise Exception("Invalid property '%s' in file %s " % (onename, filename))
	
	return default_properties
	

def load_jobinfo(filename="_JOBINFO.TXT"):
	"""
	Reads a _JOBINFO.TXT file and returns a dictionary.
	Adds the additional property "jobdir" which is the current working directory.
	"""
	job_info = __load_properties(filename,defaults=jobinfo_txt_defaults, error_on_unknown=True)
	job_info.setProperty('jobdir', os.getcwd())#reset this?
	return dict(job_info)

def load_scheduler_conf(filename="scheduler.conf"):
	"""
	We do this here because there are some defaults we want to enforce.
	"""
	scheduler_properties = __load_properties(filename, defaults=scheduler_conf_defaults, error_on_unknown=True)
	
	return dict(scheduler_properties)


def load_all_resource_XMLs(search_dir):
	"""
	Searches search_dir for resource.xml files. If search_dir is None, instead the package is searched for xmls installed with the code.
	
	"""
	resource_xmls = dict()
	
	if search_dir is not None:
		for root, dirs, filenames in os.walk(search_dir):
			for one_filename in filenames:
				if (not one_filename.endswith('.xml')):
					continue
				resource_object = SubmitXML.read_resource_file(os.path.join(root,one_filename))
				resource_xmls[str(resource_object.name)] = resource_object
	else: #Search dir none, default to resources packaged with the program.
		python_resource_names = [i for i in pkg_resources.resource_listdir(DefaultSubmitHosts.__name__,'') if i.endswith('xml')]
		for one_name in python_resource_names:
			python_resource_string = pkg_resources.resource_string(DefaultSubmitHosts.__name__,one_name)
			resource_object = SubmitXML.read_resource_string(python_resource_string)
			resource_xmls[str(resource_object.name)] = resource_object
	
	return resource_xmls
			

def load_resource_xml(filepath):
	"""
	Open the file specified by the path, and read its contents as a resource.xml file.
	
	returns: a tuple of ("resource_name", RESOURCE_OBJECT)
	"""
	resource_object = SubmitXML.read_resource_file(filepath)
	return (str(resource_object.name), resource_object)
