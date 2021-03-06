#!/usr/bin/env python
import pygtk
pygtk.require('2.0')

import gtk
import gnomeapplet
import gobject
import sys

def sample_factory(applet, iid):
    label = gtk.Label("Hello, world --- -- ")
    applet.add(label)
    
    applet.show_all()
    return gtk.TRUE

if len(sys.argv) == 2 and sys.argv[1] == "--run-in-window":   
    main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    main_window.set_title("Python Applet Debug Windos")
    main_window.connect("destroy", gtk.main_quit) 
    app = gnomeapplet.Applet()
    sample_factory(app, None)
    app.reparent(main_window)
    main_window.show_all()
    gtk.main()
    sys.exit()
    
gnomeapplet.bonobo_factory("OAFIID:GNOME_PythonAppletSample_Factory", 
                           gnomeapplet.Applet.__gtype__, 
                           "hello", "0", sample_factory)

