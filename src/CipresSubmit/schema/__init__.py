'''
Created on Oct 3, 2013

@author: lunt
'''

import resource as R

import logging 
logger = logging.getLogger("pyxb.binding.basis")
logger.addHandler(logging.NullHandler())


def read_resource_file(filename):
	with open(filename) as infile:
		return R.CreateFromDocument(infile.read())

class SimpleTuple(object):
	def __init__(self,name, value):
		self.name = name
		self.value = value

class Queue(object):
	def __init__(self, queue_object):
		self.id = queue_object.id
		self.name = queue_object.name
		self.cores_per_node = queue_object.cores_per_node
		self.cores_increment = self.cores_per_node if (queue_object.cores_increment == None) else queue_object.cores_increment
		self.max_nodes = queue_object.max_nodes
		self.max_run_hours = queue_object.max_run_hours
		self.env_vars = [SimpleTuple(i.name,i.value()) for i in queue_object.env_vars.env]
		self.env_vars_dict = dict([(i.name,i.value) for i in self.env_vars])
		self.node_properties = [i for i in queue_object.node_properties.content()]

class Template(object):
	"""
	A slightly nicer container that should encapsulate a template as specified in the resource xml documents.
	Note that it reads the template file when instantiated.
	"""
	def __init__(self, template_object):
		"""
		@param: template_object A pyxb template object.
		"""
		self.name = template_object.name
		with open(template_object.filename) as infile:
			self.template = infile.read()
		self.parameters = dict()
		for one_param in template_object.param:
			self.parameters[str(one_param.name)] = one_param.value()


class Resource(object):
	def __init__(self, resource_object):
		self.name = resource_object.name
		self.account = resource_object.account.accountstr[0]
		self.batch_system_type = resource_object.batch_system.type
		self.queues = [Queue(i) for i in resource_object.batch_system.queues.queue]
		self.queues_dict = dict([(i.id, i) for i in self.queues]) 
		
		self.templates = [Template(i) for i in resource_object.batch_system.templates.template]
		self.templates_dict = dict([(i.name, i) for i in self.templates])