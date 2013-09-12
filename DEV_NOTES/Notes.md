
# LEFT To Do #
Basically everything.

We can now load plugins for jobs, based on the job's command line, and/or the scheduler.conf properties file.

The main program hasn't been written at all.

It needs to:

Load up configuration files, such as those describing hosts and queues.
Parse out and remove it's own command-line parameters.



# JSON hosts config file #

I decided to use JSON because it is:
*   Included in python.
*   Explicitly structured enough to avoid confusion. (YAML was the other choice.)
*   Not as painful as XML.
*   Very easy to learn.

The upside of XML would be that we can more easily enforce a schema...


## cores_per_node ##
