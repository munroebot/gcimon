import unittest
import sys

sys.path.append('../src') # needed for loading backends

import backends

known_plugins = ['hudson','dummy','cruisecontrol']

class BackendModuleWellFormedness(unittest.TestCase):

    def test_PLUGIN_NAME(self):
        """ All plugins should have a PLUGIN_NAME"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.PLUGIN_NAME in known_plugins)
            except:
                print x
                raise AssertionError

    def test_PLUGIN_DESCRIPTION(self):
        """ All plugins should have a PLUGIN_DESCRIPTION"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.PLUGIN_DESCRIPTION != None)
            except:
                print x
                raise AssertionError

    def test_PLUGIN_VERSION(self):
        """ All plugins should have a PLUGIN_DESCRIPTION"""
        for x in backends.getAvailableBackends():
            try:
                self.assertTrue(x.PLUGIN_VERSION != None)
            except:
                print x
                raise AssertionError

if __name__ == "__main__":
    unittest.main()
