import gnomeapplet
import sys
import pygtk
import gtk

class Gcimon(object):
    
    def __init__(self, applet, iid):
        
        self.box1 = gtk.HBox(False, 0)
        applet.add(self.box1)
 
        self.button1 = gtk.Button("Button 1")
        self.button1.connect("clicked", self.hello, None)
        self.box1.pack_start(self.button1, True, True, 0)
        self.button1.show()

        self.button2 = gtk.Button("Button 2")
        self.button2.connect("clicked", self.destroy, None)        
        self.box1.pack_start(self.button2, True, True, 0)
        self.button2.show()
        
        self.box1.show()
        applet.show_all()
    
    def hello(self, widget, data=None):
        print "hello, world"
        
    def destroy(self, widget, data=None):
        gtk.main_quit()
