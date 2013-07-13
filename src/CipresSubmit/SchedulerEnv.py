'''
Created on Jul 12, 2013

@author: lunt
'''
import platform
import json
import re

default_hosts_config="./hosts.json"

def read_host_config(file=default_hosts_config):
	"""
	Read a JSON configuration* file describing hosts and the queues on those hosts.
	
	Find the appropriate current host, and return its information, queues, etc.
	
	 * JSON because its parser is included in python, reducing external requirements.
	
	
	The expected format of the configuration file is:
	
	{ 'host_descriptive_name' : {
		'hostlist' : [ 'host1', 'host2', 'host3' ],
		'hostregexlist' : ['A REGEX that will match the host'
		'cluster_header' : '''STRING : additional header line to put into runfile.template'''
		'queues' : {
			'descriptive_name' : {
				'name' : 'normal',
				'cores_per_node' : 16
				'max_run_time' : <FLOAT Hours>
				'cores_increment' : <int, minimum number of cores we can order.
				"max_cores" : 5000,
				'additional_properties' : { A dictionary of additional queue properties that will get passed to the submit system.}
				}
			'descriptive_name2' : {...}
		}
		'host_desciriptive_name2' : { ... 'queues':{ ... } }
	}
	
	
	"""
	f = open(file)
	retval = json.load(f)
	f.close()
	return retval

def get_current_host_config(config=None,current_host=None):
	if config == None:
		config = read_host_config()
	
	if current_host == None:
		current_host = platform.node()
	
	for hostname, hostdata in config.iteritems():
		matches=False
		fullnames=hostdata.get('hostlist',list())
		regexes = hostdata.get('hostregexlist',list())
		
		if len(fullnames) + len(regexes) > 0:
			raise Exception("No 'hostlist' or 'hostregexlist' for host '%s' in 'hosts.json' file." % hostname)
		
		#See if this host is one of the listed hosts
		for name in fullnames:
			if name.strip() == current_host:
				matches=True
		#Or see if this host matches one of the regular expressions
		for onereg in regexes:
			if re.search(onereg, current_host) is not None:
				matches=True
		
		if matches == False:
			continue
		#OK, if we made it here, we know what host we are!
		return hostdata
	return None
		
		