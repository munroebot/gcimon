import unittest
import sys
import xmlrunner

sys.path.append('../src') # needed for loading backends
sys.path.append('trunk/src') # For Hudson Testing 

import backends

class BackendModuleWellFormedness(unittest.TestCase):

    def test_BACKEND_NAME(self):
        """ All backends should have a BACKEND_NAME"""
        try:
            for x in backends.getAvailableBackends():
                self.assertTrue(x.BACKEND_NAME != None)
        except Exception, e:
            print x
            print e
    
    def test_BACKEND_DESCRIPTION(self):
        """ All backends should have a BACKEND_DESCRIPTION"""
        try:
            for x in backends.getAvailableBackends():
                self.assertTrue(x.BACKEND_DESCRIPTION != None)
        except Exception, e:
            print x
            print e

    def test_BACKEND_VERSION(self):
        """ All backends should have a BACKEND_VERSION"""
        try:
            for x in backends.getAvailableBackends():
                self.assertTrue(x.BACKEND_VERSION != None)
        except Exception,e:
            print x
            print e

suite = unittest.TestSuite()
suite.addTest(BackendModuleWellFormedness("test_BACKEND_NAME"))
suite.addTest(BackendModuleWellFormedness("test_BACKEND_DESCRIPTION"))
suite.addTest(BackendModuleWellFormedness("test_BACKEND_VERSION"))

if __name__ == "__main__":
    #runner = unittest.TextTestRunner()
    runner = xmlrunner.XmlTestRunner(sys.stdout)
    runner.run(suite)
