'''
Created on Oct 4, 2013

@author: Bryan Lunt
'''

from math import ceil
from . import PBS
from CipresSubmit.schema import Queue


def get_batch_instance(type="PBS",resource=None):
	"""
	Factory function to instantiate an instance an appropriate sub-class of "BatchEnvironment".
	
	Currently only PBS is implemented.
	
	@param type: A string giving the type for the batch system, one of "PBS"
	@type type: str
	
	@param resource: The resource we should get a batch instance for.
	@type resource: A resource object from the configs.
	
	@return: An instance from a sub-class of "BatchEnvironment".
	@rtype: BatchEnvironment 
	"""
	retval = None
	if resource is not None and resource.batch_system_type is not None:
		type = resource.batch_system_type
	type = type.upper()
	if type=="PBS":
		retval = PBS.PBSBatchEnvironment()
	else:
		raise Exception("The batch system type '%s' is not implemented yet." % type)
	
	if resource is not None:
		for one_queue in resource.queues:
			retval.add_queue(one_queue)
	
	return retval

class NotSubmit(Exception):
	def __init__(self,message):
		super(NotSubmit,self).__init__(message)

class TooManyJobs(NotSubmit):
	def __init__(self,message):
		super(TooManyJobs,self).__init__(message)

class BatchEnvironment(object):
	"""
	Abstract Base class of all batch environment objects
	"""
	def __init__(self):
		self.queues = list()
		self.queues_dict = dict()
	
	def add_queue(self,new_queue):
		self.queues.append(new_queue)
		self.queues_dict[new_queue.id] = new_queue
	
	def submit(self,jobfilename,scheduler_properties):
		"""
		Actually submit the job!
		"""
		raise NotImplementedError("This is an abstract base class")
		return False
	
	def choose_queue(self, job_properties):
		"""
		This implements the logic that Terri and Bryan discussed and that was e-mailed around.
		In the future, I'd just like it to handle figuring out the cheapest queue to run a job on.
		Choosing ppn and nodes could then be broken out to the actual submit step.
		
		@return: Queue, nodes, ppn
		
		"""
		jobtype = job_properties.get('jobtype','serial')
		mpi_processes = int(job_properties.get('mpi_processes',1))
		threads_per_process = int(job_properties.get('threads_per_process',1))
		node_exclusive = int(job_properties.get('node_exclusive',0))
		
		
		
		#RETURN VALUES
		retQ = None
		nodes = 0
		ppn = 0
		
		use_shared = False
		
		number_of_cpus = mpi_processes*threads_per_process
		
		normal_queue = self.queues_dict['normal'] # Exception if this doesn't exist
		shared_queue = self.queues_dict.get('shared', None)
		
		#If there is a shared queue, determine if we should use it.
		#The shared queue only gets used if we are submitting fewer tasks*threads than would take up a single node.
		#It does not get used if "node_exclusive=1" was specified.
		if ( not node_exclusive ) and shared_queue != None:
			shared_queue_cpu_increment = shared_queue.cores_increment
			shared_queue_max_cpus      = shared_queue.cores_per_node - shared_queue_cpu_increment
			if ( number_of_cpus <= shared_queue_max_cpus ):
				use_shared = True
				retQ  = shared_queue
				nodes = 1
				ppn   = shared_queue_cpu_increment * int(ceil(
															float(number_of_cpus) / shared_queue_cpu_increment
															))
			#End if test for shared queue
		#End test shared_queue existence
		
		
		#If the shared queue was not selected, select the normal queue
		if ( not use_shared ): #Either we decided not to use a shared queue, or there was no shared queue.
			retQ  = normal_queue
			nodes = int(ceil(
						float(number_of_cpus) / normal_queue.cores_per_node
						))
			ppn = normal_queue.cores_per_node
		#End of setting up normal queue
		
		
		return retQ, nodes, ppn	
				
			
		

