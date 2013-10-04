'''
Created on Oct 3, 2013

@author: Bryan Lunt
'''

import pyjavaproperties as Props


import ConfigParser as CFGP
import os

import CipresSubmit.schema as SubmitXML

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
	readfiles      = baseconfig.read([os.path.expanduser('~/.cipressubmit.cfg'), 'submit.cfg' ])
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
	xmlFileList    = []
	for root, dirs, filenames in os.walk(search_dir):
		for one_filename in filenames:
			if one_filename.endswith('.xml'):
				xmlFileList.append(os.path.join(root,one_filename))	
	
	resource_xmls = dict([load_resource_xml(one_filename) for one_filename in xmlFileList])
	return resource_xmls

def load_resource_xml(filepath):
	"""
	Open the file specified by the path, and read its contents as a resource.xml file.
	
	returns: a tuple of ("resource_name", RESOURCE_OBJECT)
	"""
	resource_object = SubmitXML.read_resource_file(filepath)
	return (str(resource_object.name), resource_object)