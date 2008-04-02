import backends

def my_import(name):
    mod = __import__(name)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod

x = my_import("backends." + backends.__all__[1])

x.Backend()