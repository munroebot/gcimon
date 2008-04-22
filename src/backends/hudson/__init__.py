# backends/hudson/__init__.py
# Copyright 2007, Brian Munroe <brian.e.munroe@gmail.com>

# This is the Hudson CI plugin.  Please see the 
# docs/plugins_howto.txt for more info on developing 
# new plugins for gcimon.

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

from gcimon.types import Project

import urllib
from xml.dom import minidom

PLUGIN_NAME = "hudson"
PLUGIN_DESCRIPTION = """
This plugin is for the Hudson Continuous Integration Server.  
For more information, please see http://hudson.dev.java.net
"""
PLUGIN_VERSION = "1.0"
	
class Backend(object):
	
	def __init__(self):
		self.baseUrl = None
		self.username = None
		self.password = None
	
	def setBaseUrl(self,baseUrl):
		self.baseUrl = baseUrl
	
	def getDashboardStatus(self):
		try:
			projectArray = []
			sock = urllib.urlopen(self.baseUrl + '/api/xml')
			xmlSource = sock.read()                           
			sock.close()
			
			xmldoc = minidom.parseString(xmlSource)
		
			## Grab all jobs in the dashboard
			jobsList = xmldoc.getElementsByTagName('job')
			
			## Job Nmaes
			for x in jobsList:
				p1 = Project()
				nameList = x.getElementsByTagName('name')
				for y in nameList:
					p1.projectName = y.firstChild.nodeValue
					
				## Job Statusus (colors)
				colorList = x.getElementsByTagName('color')
				for y in colorList:
					if y.firstChild.nodeValue == 'blue':
						p1.projectStatus = p1.BUILD_STATUS_OK
					else:
						p1.projectStatus = p1.BUILD_STATUS_BROKE
			
				projectArray.append(p1)
		
			return projectArray
		except:
			return None
			
	def getProjectStatus(self,projectName=None):
		try:
			sock = urllib.urlopen(self.baseUrl + '/job/'+ urllib.quote(projectName) +'/api/xml')
			xmlSource = sock.read()                           
			sock.close()
			xmldoc = minidom.parseString(xmlSource)
			return xmldoc.toxml()
		except: 
			return None
 