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
    BUILD_STATUS_OK = 1
    BUILD_STATUS_BROKE = 0
    IS_MONITORED = 1
    IS_NOT_MONITORED = 0
    
    def __init__(self,projectId=None,projectName=None,projectStatus=None,projectBackend=None,projectHost=None,projectLast=None,projectState=IS_MONITORED):
        self._projectId = projectId
        self._projectName = projectName
        self._projectStatus = projectStatus
        self._projectBackend = projectBackend
        self._projectHost = projectHost
        self._projectLastChecked = projectLast
        self._projectState=projectState

    def getId(self):
        return self._projectId

    def setId(self, value):
        self._projectId = value

    def getName(self):
        return self._projectName

    def setName(self, value):
        self._projectName = value

    def getStatus(self):
        return self._projectStatus

    def setStatus(self, value):
        self._projectStatus = value
     
    def getBackend(self):
        return self._projectBackend
    
    def setBackend(self,value):
        self._projectBackend = value
    
    def getHost(self):
        return self._projectHost

    def setHost(self, value):
        self._projectHost = value

    def getlastChecked(self):
        return self._projectLastChecked

    def setLastChecked(self, value):
        self._projectLastChecked = value

    def getState(self):
        return self._projectState

    def setState(self, value):
        self._projectState = value

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
