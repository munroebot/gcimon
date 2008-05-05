#!/usr/bin/env python

# applet_factory.py
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

import gnomeapplet
import sys
import pygtk
import gtk
from gcimon import Gcimon

def gcimon_factory(applet, iid):
    Gcimon(applet,iid)
    return gtk.TRUE

if len(sys.argv) == 2 and sys.argv[1] == "--run-in-window":
    print "Running Interactively"
    main_window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    main_window.set_title("Python Applet Debug Windos")
    main_window.connect("destroy", gtk.main_quit) 
    app = gnomeapplet.Applet()
    gcimon_factory(app, None)
    app.reparent(main_window)
    main_window.show_all()
    gtk.main()
    sys.exit()
    
gnomeapplet.bonobo_factory("OAFIID:GNOME_PythonAppletSample_Factory", 
                           gnomeapplet.Applet.__gtype__, 
                           "hello", "0", gcimon_factory)