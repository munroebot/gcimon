PLUGIN_NAME = 'CruiseControl'
PLUGIN_STAT = 'MOCK'

class Backend(object):
	def __init__(self):
		pass

	def getProjectStatus(self,projectName=None):
		return "400_OK"
