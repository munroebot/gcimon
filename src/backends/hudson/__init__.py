# backends/hudson/__init__.py
# Copyright 2007, Brian Munroe <brian.e.munroe@gmail.com>

# This is the Hudson CI backend.  Please see the 
# docs/backends_howto.txt for more info on developing 
# new CI backends for gcimon.

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

from gcimon.types import BaseBackend, Project

import urllib
import logging
from xml.dom import minidom

BACKEND_NAME = "hudson"
BACKEND_DESCRIPTION = """
This backend is for the Hudson Continuous Integration Server.  
For more information, please see http://hudson.dev.java.net
"""
BACKEND_VERSION = "1.0"

logger = logging.getLogger("Hudson Backend")

class Backend(BaseBackend):

    def getDashboardStatus(self):
        try:
            projectArray = []
            sock = urllib.urlopen(self.getBaseUrl() + '/api/xml')
            xmlSource = sock.read()                           
            sock.close()
			
            xmldoc = minidom.parseString(xmlSource)
		
            ## Grab all jobs in the dashboard
            jobsList = xmldoc.getElementsByTagName('job')
			
            ## Job Names
            for x in jobsList:
                p1 = Project()
                nameList = x.getElementsByTagName('name')
                for y in nameList:
                    p1.setProjectName(y.firstChild.nodeValue)
					
                ## Job Statusus (colors)
                colorList = x.getElementsByTagName('color')
                for y in colorList:
                    if y.firstChild.nodeValue == 'blue':
                        p1.setProjectStatus(p1.BUILD_STATUS_OK)
                    else:
                        p1.setProjectStatus(p1.BUILD_STATUS_BROKE)
			
                    projectArray.append(p1)
		
            return projectArray
        except Exception, e:
            logger.error("Error in hudson.Backend.getDashboardStatus(): " + str(e))
            return None
			
    def getProjectStatus(self,project=None):
        try:
            sock = urllib.urlopen(project.getHost() + "/job/" + urllib.quote(project.getName()) +'/api/xml')
            xmlSource = sock.read()                           
            sock.close()
            xmldoc = minidom.parseString(xmlSource)
            colorList = xmldoc.getElementsByTagName('color')
            for y in colorList:
                if y.firstChild.nodeValue == 'blue':
                    return project.BUILD_STATUS_OK
                else:
                    return project.BUILD_STATUS_BROKE

        except Exception, e: 
            logger.error("Error in hudson.Backend.getProjectStatus(): " + str(e))
            return None
 
