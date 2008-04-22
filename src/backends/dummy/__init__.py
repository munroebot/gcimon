# backends/dummy/__init__.py
# Copyright 2007, Brian Munroe <brian.e.munroe@gmail.com>

# This is a dummy (mock) CI plugin.  Please see the 
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

PLUGIN_NAME = 'dummy'
PLUGIN_DESCRIPTION = """ This is a dummy CI backend """
PLUGIN_VERSION = "1.0"

class Backend(object):
	def __init__(self):
		pass

	def getProjectStatus(self,projectName=None):
		return Project.BUILD_STATUS_OK
	
	def getDashboardStatus(self):
		pass
