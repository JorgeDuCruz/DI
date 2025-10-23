import  gi
from EjemploEssemtia.CaixaCor import CaixaCor
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject

"""Diseño

rojo-marron-amarillo-naranja
rojo-verde-verde-morado
azul-azul-rosa-negro

"""

class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de uso de grid layout")

        rojo = CaixaCor("red")
        morado = CaixaCor("purple")
        amarillo = CaixaCor("yellow")
        verde = CaixaCor("green")
        azul = CaixaCor("blue")
        rosa = CaixaCor("pink")
        naranja = CaixaCor("orange")
        marron = CaixaCor("brown")
        negro = CaixaCor("black")

        caixa = Gtk.Grid()
        caixa.attach_next_to(rojo,None,Gtk.PositionType.LEFT,1,2)
        caixa.attach_next_to(marron,rojo,Gtk.PositionType.RIGHT,1,1)
        caixa.attach_next_to(verde, marron, Gtk.PositionType.BOTTOM, 2, 1)
        caixa.attach_next_to(azul, rojo, Gtk.PositionType.BOTTOM, 2, 1)

        caixa.attach_next_to(amarillo, marron, Gtk.PositionType.RIGHT, 1, 1)
        caixa.attach_next_to(rosa, azul, Gtk.PositionType.RIGHT, 1, 1)
        caixa.attach_next_to(morado, verde, Gtk.PositionType.RIGHT, 1, 1)

        caixa.attach_next_to(naranja, morado, Gtk.PositionType.TOP, 1, 1)
        caixa.attach_next_to(negro, morado, Gtk.PositionType.BOTTOM, 1, 1)




        self.add(caixa)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemplosBoxColor()
    Gtk.main()