'''
Created on Jul 11, 2013

@author: lunt
'''

import CipresSubmit.plugins as P
import CipresSubmit.SubmitLogger as CSub

import unittest


class Test(unittest.TestCase):


	def setUp(self):
		self.my_env = CSub.SubmitLogger


	def tearDown(self):
		pass


	def testName(self):
		pass


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()




my_env = CSub.SubmitEnvironment()

print "testing a custom direct job"
job = P.load_appropriate_plugin('plugins',None,'this is a test',my_env)
print job

print job.validate()
print job.parallel_rules()

print job.submitJob()

job = P.load_appropriate_plugin('plugins',None,'that was also a test',my_env)
print job

print job.validate()
print job.parallel_rules()

print job.submitJob()

