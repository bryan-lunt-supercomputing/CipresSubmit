'''
Created on Jul 12, 2013

@author: lunt
'''
import unittest

import CipresSubmit.SchedulerEnv as SEnv

class Test(unittest.TestCase):


	def setUp(self):
		pass


	def tearDown(self):
		pass


	def testLoad(self):
		self.scheduler = SEnv.get_current_host_config()


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()