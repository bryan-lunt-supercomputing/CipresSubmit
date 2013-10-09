'''
Created on Oct 3, 2013

@author: Bryan Lunt
'''

import pyjavaproperties as Props

import pkg_resources

import ConfigParser as CFGP
import os
import os.path

import CipresSubmit.schema as SubmitXML
import CipresSubmit.hosts as DefaultSubmitHosts

def __config_to_str_dict(config):
	retdict = dict([
				(sect_name,
					dict( config.items(sect_name) )
				)
				for sect_name in config.sections()])
	return retdict

def load_configs():
	baseconfig = CFGP.ConfigParser()
	#Load a global submit configuration but allow it to be overridden by a local configuration
	default_config = pkg_resources.resource_filename(__name__,"cipressubmit.cfg")
	readfiles      = baseconfig.read([default_config,os.path.expanduser('~/.cipressubmit.cfg'), 'cipressubmit.cfg' ])
	return __config_to_str_dict(baseconfig)

def load_jobinfo(filename="_JOBINFO.TXT"):
	job_info = Props.Properties()
	
	job_info.setProperty('jobdir', os.getcwd())
	
	with open(filename) as infile:
		job_info.load(infile)
	return dict(job_info)

def load_scheduler_conf(filename="scheduler.conf"):
	"""
	We do this here because there are some defaults we want to enforce.
	"""
	scheduler_properties = Props.Properties()
	
	#Defaults
	scheduler_properties.setProperty("jobtype","non_mpi")
	scheduler_properties.setProperty("mpi_processes","1")
	scheduler_properties.setProperty("threads_per_process","1")
	scheduler_properties.setProperty("nodes","1")
	scheduler_properties.setProperty("node_exclusive","0")
	
	with open(filename) as infile:
		scheduler_properties.load(infile)
	return dict(scheduler_properties)


def load_all_resource_XMLs(search_dir):
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