CipresSubmit
============

# Introduction #

This tool is intended to ease the submission of simple single-command jobs to compute clusters.
It was originally written as part of the back-end of the CIPRES Science Gateway.

Science-Gateways need to be able to submit jobs in a unified manner, and have certain expectations about the uniformity of jobs.
Even for non-gateway jobs, this can often be quite useful, if the computation one desires can be expressed on one line.

(Often a computation can be embodied in a normal shell-script and then it does become a single-line.)

I hope this will be useful to you.


## Concepts ##
This program is, in essence (and the majority of its code), a template engine.
Given a command-line and some configuration files, this program is primarily concerned with creating a script to be submit to PBS via qsub. (Or with configuration, any other way.)

This program also has some components for understanding which queues are available on a computational resource, and selecting the appropriate queue for a job to run on.

## Documentation ##
This was originally developed for in-house use, see the "DEV_NOTES" and "docs" directories for more comprehensive documentation.

## Licenses ##
This program itself is licensed under an MIT license, found in `LICENSE.txt`. It uses some external dependencies which have been directly included into the source tree, the license(s) for those are also provided.
