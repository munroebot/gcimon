PLUGIN_NAME = 'Hudson CI Server Backend'

class Backend(object):
	
	def __init__(self):
		pass
	
	def getProjectStatus(self,projectName=None):
		return "400_OK"