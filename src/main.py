import gnomeapplet
import sys
import pygtk
import gtk

import backends
from gcimon.types import Project

# Fetch a Hudson backend and set the site to monitor
hudson = backends.getBackend('hudson')
site1 = hudson.Backend()
site1.setBaseUrl('http://localhost:8080/hudson')
site1.setUsername('brian')
site1.setPassword('password')

# Or, if you wish, you can set everything at once
site2 = hudson.Backend('http://localhost:8080/hudson','brian','password')

# Get the status of a specfic project
print site1.getProjectStatus('Dummy Project for Hudson Monitor')
print site2.getProjectStatus('gcimon unit tests')

## Or report the status for ALL the projects
## on a continuous integration server dashboard
## getDashboardStatus() returns a list of Project types.
for project in site1.getDashboardStatus():
	print project.getProjectName()
	print project.getProjectStatus()