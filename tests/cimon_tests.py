import unittest
import sys

sys.path.append('../src') # needed for loading backends

import backends

known_plugins = ['Hudson','Dummy','CruiseControl']

class BackendModuleWellFormedness(unittest.TestCase):

    def testAttribute_PLUGIN_NAME(self):
        """ All plugins should have a PLUGIN_NAME"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.PLUGIN_NAME in known_plugins)
            except:
                print x

    def testMethod_getProjectStatus(self):
        for x in backends.getAvailableBackends():
            try:
                self.assertEquals("
            
if __name__ == "__main__":
    unittest.main()
