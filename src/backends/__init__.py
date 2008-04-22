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
