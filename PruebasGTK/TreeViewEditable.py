import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemploTree(Gtk.Window):
    def on_celdaFalecido_toogled(self,celda,fila,modelo):
        print('Clicamos en ',fila)
        modelo [fila][4] = not modelo [fila][4]

    def on_celdaNome_edited(self,celda,fila,cadroTexto,numero,modelo):
        print("Editamos: ",numero,fila,cadroTexto)
        if numero == 1:
            modelo[fila][1] = cadroTexto

    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Treeview en árbol")

        caixav = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing= 6)
        modelo = Gtk.ListStore(str,str,int,str,bool)
        listaUsuarios = [('1234H','Ana Perez',34,'Muller',False),
                         ('4321T','Pepe Diz',78,'Home',True)]

        for usuario in listaUsuarios:
            modelo.append(usuario)

        trvVista = Gtk.TreeView(model=modelo)

        for i, tituloColumna in enumerate (('Dni','Nome')):
            celda = Gtk.CellRendererText()
            celda.set_property("editable",True)
            celda.connect("edited",self.on_celdaNome_edited,i,modelo)
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            trvVista.append_column(columna)
        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn('Edade',celda, value = 2)
        trvVista.append_column(columna)

        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn('Xénero', celda, text=3)
        trvVista.append_column(columna)

        celda = Gtk.CellRendererToggle()
        celda.set_property("sensitive",True)
        celda.connect("toggled", self.on_celdaFalecido_toogled,modelo)
        columna = Gtk.TreeViewColumn('Falecido',celda,active=4)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)

        self.add(caixav)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploTree()
    Gtk.main()