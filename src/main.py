import backends
from gcimon.types import Project

hudson = backends.getBackend('hudson')
projectSite1 = hudson.Backend()
projectSite1.setBaseUrl('http://localhost:8080/hudson')

## Report the status for all the projects
## on a continuous integration server dashboard
for project in projectSite1.getDashboardStatus():
	print project.projectName
	print project.projectStatus

#print projectSite1.getProjectStatus('Dummy Project for Hudson Monitor')