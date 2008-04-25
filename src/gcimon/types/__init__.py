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
        self._projectName = None
        self._projectStatus = None

    def getProjectName(self):
        return self._projectName

    def getProjectStatus(self):
        return self._projectStatus

    def setProjectName(self, value):
        self._projectName = value

    def setProjectStatus(self, value):
        self._projectStatus = value

    def delProjectName(self):
        del self._projectName

    def delProjectStatus(self):
        del self._projectStatus

class BaseBackend(object):

    def __init__(self,baseUrl=None,username=None,password=None):
        self._baseUrl = baseUrl
        self._username = username
        self._password = password
		
    def getUsername(self):
        return self._username
    
    def setUsername(self,value):
        self._username = value
    
    def getPassword(self):
        return self._password
    
    def setPassword(self,value):
        self._password = value

    def getBaseUrl(self):
        return self._baseUrl
    
    def setBaseUrl(self,value):
        self._baseUrl = value
