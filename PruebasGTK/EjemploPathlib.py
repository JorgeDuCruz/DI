import  gi
import  pathlib
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemploTree(Gtk.Window):
    def explorarDirectorio(self,ruta,punteiroPai, modelo):
        contidoDir = pathlib.Path(ruta)
        for entrada in contidoDir.iterdir():
            if  entrada.is_dir():
                punteiroFillo = modelo.append(punteiroPai, ("folder", entrada.name))
                #self.explorarDirectorio(ruta+'/'+entrada.name,punteiroFillo,modelo)
            else:
                modelo.append(punteiroPai,("emblem-documents", entrada.name))

    def on_seleccion_changed(self, seleccion):
        ruta = ""
        modelo,fila = seleccion.get_selected()
        if modelo[fila][0] == "folder":
            ruta = self.obterRuta(modelo,fila)
            self.explorarDirectorio("/home/dam/"+ruta,fila,modelo)



    def obterRuta(self,modelo,fila):

        punteiroPai = modelo.iter_parent(fila)

        if punteiroPai is None:
            return modelo[fila][1]
        else:
            return self.obterRuta(modelo,punteiroPai)+"/"+modelo[fila][1]



    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Treeview en árbol")

        caixav = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing= 6)

        modelo = Gtk.TreeStore(str,str)
        trvVista = Gtk.TreeView(model=modelo)
        seleccion = trvVista.get_selection()
        seleccion.connect("changed",self.on_seleccion_changed)

        tvcColumna = Gtk.TreeViewColumn()
        trvVista.append_column(tvcColumna)
        celda = Gtk.CellRendererPixbuf()
        tvcColumna.pack_start(celda, True)
        tvcColumna.add_attribute(celda, 'icon_name', 0)

        tvcColumna = Gtk.TreeViewColumn()
        trvVista.append_column(tvcColumna)
        celda = Gtk.CellRendererText()
        tvcColumna.pack_start(celda, True)
        tvcColumna.add_attribute(celda, 'text', 1)

        self.explorarDirectorio('/home/dam/',None, modelo)

        caixav.pack_start(trvVista,True,True,10)

        self.add(caixav)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploTree()
    Gtk.main()