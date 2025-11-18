import  gi
from EjemploEssemtia.CaixaCor import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

"""Diseño

rojo-marron-amarillo-naranja
rojo-verde-verde-morado
azul-azul-rosa-negro

"""

class EjemploGlade:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("formularioAlbara.glade")
        wndPrincipal = builder.get_object("wndPrincipal")



if __name__ == "__main__":
    EjemploGlade()
    Gtk.main()