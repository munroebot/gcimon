from backends import hudson

be1 = hudson.Backend()
print be1.getProjectStatus('Dummy Project')
