#!/usr/bin/env python

from distutils.core import setup, Extension

import os
def find_all_scripts(topdir):
        allfiles = list()
        for dirpath,subdirs,filenames in os.walk(topdir):
                for onefile in filenames:
                        allfiles.append(os.path.join(dirpath,onefile))
        return allfiles

setup(name="CipresSubmit",
        version="0.2.0",
        description="Tools for Submitting and managing jobs on a CIPRES portal backend.",
        author="Bryan Lunt",
        author_email="blunt@sdsc.edu",
        package_dir={'':'src'},
        packages=["CipresSubmit",'CipresSubmit.hosts','CipresSubmit.schema','CipresSubmit.SubmitEnv','CipresSubmit.templates'],
        package_data={'CipresSubmit.templates':['*.template'], 'CipresSubmit.hosts':['*.xml'], 'CipresSubmit':['cipressubmit.cfg']},
        scripts=find_all_scripts("scripts") + ['src/submit.py'],
        install_requires=["pystache>=0.5.3", "PyXB>=1.2.2"],
	)