# gcimon/core/__init__.py
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

from gcimon.types import Project
import sqlite3
import logging
import time

logger = logging.getLogger("Persistance")

class Persistance(object):

    def __init__(self,dataStore=":memory:"):
        self.dataStore = dataStore
    
    def newProject(self,project=None):
        try:
            if (project != None):
                conn = sqlite3.connect(self.dataStore)
                c = conn.cursor()
                strSQL = "insert into projects values (null,?,?,?,?,?,?)"
                c.execute(strSQL,(project.getName(),Project.BUILD_OK,project.getBackend(),project.getHost(),0,Project.IS_MONITORED))
                conn.commit()
                c.close()
            else:
                raise Exception, 'No Project Defined'
            return True
        except Exception, e:
            logger.error("Error in core.Persistance.newProject: " + str(e))
            return False
           
    def updateProject(self,project=None):
        try:
            conn = sqlite3.connect(self.dataStore)
            c = conn.cursor()
            c.execute("update projects set project_status = ?, project_last = ? where project_id = ?",(project.getStatus(),time.time(),project.getId()))
            conn.commit()
            c.close()
            return True
        
        except Exception, e:
            logger.error("Error in core.Persistance.updateProject: " + str(e))
            return False
    
    def deleteProject(self,project=None):
        try:
            if (project != None):
                conn = sqlite3.connect(self.dataStore)
                c = conn.cursor()
                c.execute("delete from projects where projectId = ?",(project.getId(),))
                conn.commit()
                c.close()
                return True
            else:
                raise Exception, 'No Project Defined'
        
        except Exception, e:
            logger.error("Error in core.Persistance.deleteProject: " + str(e))
            return False
    
    def setMonitoringState(self,project=None):
        try:
            if (project != None):
                conn = sqlite3.connect(self.dataStore)
                c = conn.cursor()
                c.execute("update projects set project_state = ? where project_id = ?",(project.getState(),project.getId()))
                conn.commit()
                c.close()
                return True
            else:
                raise Exception, 'No Project Defined'
        
        except Exception, e:
            logger.error("Error in core.Persistance.setMonitoringState: " + str(e))
            return False        
        
    def getMonitoredProjects(self):
        try:
            conn = sqlite3.connect(self.dataStore)
            c = conn.cursor()
            c.execute("select * from projects where project_state = ?",(Project.IS_MONITORED,))
            projectList = []
            for row in c:
                projectList.append(Project(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            
            c.close()
            return projectList
                       
        except Exception, e:
            logger.error("Error in core.Persistance.getMonitoredProjects: " + str(e))
            return None

    def getAllProjects(self):
        try:
            conn = sqlite3.connect(self.dataStore)
            c = conn.cursor()
            c.execute("select * from projects")
            projectList = []
            for row in c:
                projectList.append(Project(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            
            c.close()
            return projectList
                       
        except Exception, e:
            logger.error("Error in core.Persistance.getAllProjects: " + str(e))
            return None
       
