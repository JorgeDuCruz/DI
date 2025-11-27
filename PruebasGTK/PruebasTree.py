import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemploTree(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Treeview en árbol")

        caixav = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing= 6)

        modelo = Gtk.TreeStore(str,int)

        for avo in range(5):
            punteiroAvo = modelo.append(None,["Avo %i" % (avo,),avo])
            for pai in range(4):
                punteiroPai = modelo.append(punteiroAvo,["Pai %i do avó %i" % (pai,avo), pai])
                for fillo in range(3):
                    modelo.append(punteiroPai,["Fillo %i, do pai %i, do avó %i" % (fillo,pai,avo), fillo])
        trvVista = Gtk.TreeView(model=modelo)
        tvcColumna = Gtk.TreeViewColumn("Parentesco")
        trvVista.append_column(tvcColumna)
        celda = Gtk.CellRendererText(   )
        tvcColumna.pack_start(celda,True)
        tvcColumna.add_attribute(celda,'text',0)

        tvcColumna2 = Gtk.TreeViewColumn("Orde")
        trvVista.append_column(tvcColumna2)
        celda = Gtk.CellRendererText()
        tvcColumna.pack_start(celda,True)
        tvcColumna.add_attribute(celda,'text',1)

        caixav.pack_start(trvVista, True, True, 5)

        self.add(caixav)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploTree()
    Gtk.main()