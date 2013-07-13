'''
Created on Jul 12, 2013

@author: lunt
'''
import unittest

CONFFILE ="./scheduler.conf"

class Test(unittest.TestCase):


	def setUp(self):
		f = file(CONFFILE,"w")
		f.write("""runhours=0.5
mpi_processes=2 
jobtype=mpi
nodes=1
""")
		f.close()


	def tearDown(self):
		pass


	def testSubmit(self):
		pass


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()