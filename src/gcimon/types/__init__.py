# gcimon/__init__.py
# Copyright 2008, Brian Munroe <brian.e.munroe@gmail.com>

# This file is part of gcimon.
#
# gcimon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# gcimon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with gcimon.  If not, see <http://www.gnu.org/licenses/>.

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
	