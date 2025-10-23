import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

class CaixaCor(Gtk.DrawingArea):
    def __init__(self,color):
        super().__init__()
        self.set_size_request(50,50)
        rgba = Gdk.RGBA() # RGBA: (r=0.0-1.0, g=0.0-1.0, b=0.0-1.0 a=0.0-1.0) Entre 0.0 y 1.0
        rgba.parse(color)
        self.color = rgba
        self.connect("draw",self.on_draw)

    def on_draw(self,control,cr):
        r,g,b,a = self.color
        cr.set_source_rgba(r,g,b,a)
        cr.paint()