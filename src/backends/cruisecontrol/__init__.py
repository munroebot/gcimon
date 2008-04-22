from gcimon.types import Project

PLUGIN_NAME = 'cruisecontrol'
PLUGIN_DESCRIPTION = """ This is the CruiseControl CI Server Backend """
PLUGIN_VERSION = "1.0"

class Backend(object):
	def __init__(self):
		pass

	def getProjectStatus(self,projectName=None):
		return Project.BUILD_STATUS_OK
	
	def getDashboardStatus(self):
		pass
