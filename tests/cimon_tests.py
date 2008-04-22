import unittest
import sys

sys.path.append('../src') # needed for loading backends

import backends

class BackendModuleWellFormedness(unittest.TestCase):

    def test_BACKEND_NAME(self):
        """ All backends should have a BACKEND_NAME"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.BACKEND_NAME != None)
            except:
                print x
                raise AssertionError

    def test_BACKEND_DESCRIPTION(self):
        """ All backends should have a BACKEND_DESCRIPTION"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.BACKEND_DESCRIPTION != None)
            except:
                print x
                raise AssertionError

    def test_BACKEND_VERSION(self):
        """ All backends should have a BACKEND_VERSION"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.BACKEND_VERSION != None)
            except:
                print x
                raise AssertionError

if __name__ == "__main__":
    unittest.main()
