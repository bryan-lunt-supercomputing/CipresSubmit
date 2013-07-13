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
	queue
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
