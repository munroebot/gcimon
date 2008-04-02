import backends

for x in backends.getAvailableBackends():
	print x.PLUGIN_NAME
	be = x.Backend()
	print be.getProjectStatus()
