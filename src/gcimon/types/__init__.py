class Project(object):
    BUILD_STATUS_OK = "400_OK"
    BUILD_STATUS_BROKE = "200_BROKE"
    
    def __init__(self):
        self.__projectName = None
        self.__projectStatus = None

    def getProjectName(self):
        return self.__projectName

    def getProjectStatus(self):
        return self.__projectStatus

    def setProjectName(self, value):
        self.__projectName = value

    def setProjectStatus(self, value):
        self.__projectStatus = value

    def delProjectName(self):
        del self.__projectName

    def delProjectStatus(self):
        del self.__projectStatus
        
    projectName = property(getProjectName, setProjectName, delProjectName, "ProjectName's Docstring")
    projectStatus = property(getProjectStatus, setProjectStatus, delProjectStatus, "ProjectStatus's Docstring")

class BaseBackend(object):

	def __init__(self):
		self.__baseUrl = None
		self.__username = None
		self.__password = None

	def getBaseUrl(self):
		return self.baseUrl
	
	def setBaseUrl(self,value):
		self.baseUrl = value
	