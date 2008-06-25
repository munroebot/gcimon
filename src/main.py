import backends
from gcimon.types import Project
from gcimon.core import Persistance
import logging
import time

logging.basicConfig(level=logging.DEBUG, \
                    format='%(asctime)s %(levelname)s %(message)s', \
                    filename='/tmp/gcimon.log', filemode='a')

db1 = Persistance('/tmp/gcimon.db')

# project = Project(projectName="GCI Monitor 2",projectHost="http://localhost:8080/hudson",projectBackend="hudson")
# db1.newProject(project)
# db1.updateProject(project)
# db1.deleteProject(project)

while 1:

    for project in db1.getMonitoredProjects():
        be1 = backends.getBackend(project.getBackend()).Backend()
        project.setStatus(be1.getProjectStatus(project))
        print "Project Name: %s, Build Status: %s, Last Checked: %s" % (project.getName(), project.getStatus(), str(project.getlastChecked()))
    
        db1.updateProject(project)
        db1.setMonitoringState(Project(projectId=2,projectState=Project.IS_NOT_MONITORED))
        
    time.sleep(10)
