import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Primera aplicacion con Gtk")
        caixaV = Gtk.Box (orientation = Gtk.Orientation.VERTICAL, spacing = 10)
        lblSaudo = Gtk.Label(label = "Introduce o teu nome")
        caixaV.pack_start(lblSaudo,True,True,5)
        txtSaudo = Gtk.Entry()
        caixaV.pack_start(txtSaudo,False,True,5)
        btnSaudo = Gtk.Button(label = "Saudar")
        caixaV.pack_start(btnSaudo,False,False,5)

        self.add(caixaV)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()