# backends/__init__.py
# Copyright 2007, Brian Munroe <brian.e.munroe@gmail.com>

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

import os
availableBackendsList = []

def getAvailableBackends():
	return map(__subpackage_import, availableBackendsList)

def getBackend(backendName):
	return __subpackage_import("backends." + backendName)

def __subpackage_import(name):
	mod = __import__(name)
	components = name.split('.')
	for comp in components[1:]:
		mod = getattr(mod, comp)
	return mod

for module in os.listdir(__path__[0]):
	if not module.startswith("__") and not module.startswith("."):
		availableBackendsList.append("backends." + module)
