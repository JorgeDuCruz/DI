import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemplosBoxColor(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de layout")
        self.set_size_request(500,500)
    #Contenedor general
        caixa = Gtk.Grid()
        panelcapition = Gtk.Frame(label="Panel Caption")
        panelcapition.add(caixa)

    #Priemra caja
        framePanel = Gtk.Frame()
        framePanel.set_label("Panel")
        caixa.add(framePanel)

        PanelContent = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        framePanel.add(PanelContent)

    #Lista
        listaConteido = Gtk.ListStore(str)
        listaConteido.append(["Item1"])
        listaConteido.append(["Item2"])

        lista = Gtk.TreeView(model=listaConteido)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Contido",renderer,text=0)
        lista.append_column(column)

        PanelContent.add(lista)

    #Botones
        BotonesPanel = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        PanelContent.add(BotonesPanel)

        #Botones radio
        botonesRadio1 =  Gtk.RadioButton.new_with_label_from_widget(None, "Boton 1")
        botonesRadio2 = Gtk.RadioButton.new_with_label_from_widget(botonesRadio1, "Boton 2")
        botonesRadio3 = Gtk.RadioButton.new_with_label_from_widget(botonesRadio1, "Boton 3")
        botonesRadioInac = Gtk.RadioButton.new_with_label_from_widget(botonesRadio1, "Boton inactivo")
        botonesRadioInac.set_sensitive(False)

        #Espacio entre botones
        relleno = Gtk.Label()
        relleno.set_size_request(0,50)

        #Boton normal
        boton = Gtk.Button(label="Botón")

    #Añadir los botones
        BotonesPanel.add(botonesRadio1)
        BotonesPanel.add(botonesRadio2)
        BotonesPanel.add(botonesRadio3)
        BotonesPanel.add(botonesRadioInac)
        BotonesPanel.add(relleno)
        BotonesPanel.add(boton)


    #Crear la ventana
        self.add(panelcapition)
        self.connect("delete-event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemplosBoxColor()
    Gtk.main()