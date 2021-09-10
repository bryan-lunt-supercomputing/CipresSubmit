'''
Created on Jul 12, 2013

@author: lunt
'''
import unittest
import os

import submit

SCHEDULER_CONF_FILENAME ="scheduler.conf"
JOBINFO_TXT_FILENAME = "_JOBINFO.TXT"

def _write_properties(outfile,indict):
	with open(outfile,"w") as OUTFILE:
		for key,value in indict.items():
			OUTFILE.write("%s=%s\n" % (key.replace(' ','\\ '), value))

TESTING_BASE=os.path.dirname(os.path.realpath(__file__))
TESTING_OUTPUT=os.path.join(TESTING_BASE,'testoutput')


class BasicTest(unittest.TestCase):


	def setUp(self):
		self.ONE_TEST_DIR=os.path.join(TESTING_OUTPUT,"BasicTest")
		try:
			os.mkdir(self.ONE_TEST_DIR)
		except Exception as e:
			print(e)
		
		_write_properties(os.path.join(self.ONE_TEST_DIR,SCHEDULER_CONF_FILENAME), {'runhours':0.5 , 'mpi_processes':2, 'jobtype':'mpi', 'nodes':1})
		_write_properties(os.path.join(self.ONE_TEST_DIR,JOBINFO_TXT_FILENAME), {'resource':'gordon'})

	def tearDown(self):
		#os.rmdir(self.ONE_TEST_DIR)
		pass


	def testSubmit(self):
		commandline = "foobarbaz".split()
		CURRENTDIR = os.getcwd()
		os.chdir(self.ONE_TEST_DIR)

		submit.main(['submit.py', '--dry-run', '--'] + commandline)
		
		os.chdir(CURRENTDIR)


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
