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

    def on_xenero_changed(self,celda,fila,indx,modeloTab):
        modeloTab[fila][3] = celda.props.model[indx][0]

    def filtro_usuarios_xenero(self,modelo, fila, datosUsuario):
        if self.filtradoXenero is None or self.filtradoXenero == "None":
            return True
        else:
            return modelo [fila] [3] == self.filtradoXenero

    def on_xeneroToggled(self,boton,modelo):
        if boton.get_active():
            print(boton.get_label())
            self.filtradoXenero = boton.get_label()
            modelo.refilter()

    def on_rbtEdad_toggled(self,boton,scale,modelo):
        if boton.get_active():
            self.filtradoEdad = scale.get_value()
            self.filtradoEdadAux = boton.get_label()
            modelo.refilter()

    def on_scaleEdad_changed(self,scale,modelo):
        self.filtradoEdad = scale.get_value()
        modelo.refilter()

    def filtro_usuarios_edade(self,modelo, fila, datosUsuario):
        if self.filtradoEdadAux is None or self.filtradoEdad is None:
            return True
        else:
            if self.filtradoEdadAux=="Mayor de":
                return modelo[fila][2] > self.filtradoEdad
            else:
                return modelo[fila][2] < self.filtradoEdad

    def filtros_usuarios(self,modelo,fila,datosUsuario):
        edad = self.filtro_usuarios_edade(modelo,fila,datosUsuario)
        xenero = self.filtro_usuarios_xenero(modelo,fila,datosUsuario)
        return (edad and xenero)

    def compara_edades(self,modelo,fila1, fila2, datosUsuarios):
        columna_ordear,_ = modelo.get_sort_column_id()
        edade1 = modelo.get_value (fila1,columna_ordear)
        edade2 = modelo.get_value (fila2,columna_ordear)

        if edade1>edade2:
            return 1
        elif edade1 <edade2:
            return -1
        elif edade1 == edade2:
            return 0


    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo de Treeview en árbol")

        self.filtradoXenero = None
        self.filtradoEdad = None
        self.filtradoEdadAux = "Mayor de"

        caixav = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing= 6)
        modelo = Gtk.ListStore(str,str,int,str,bool)
        listaUsuarios = [('1234H','Ana Perez',34,'Muller',False),
                         ('4321T','Pepe Diz',78,'Home',True),
                         ('5678U','Rosa Gil',56, 'Muller',False),
                         ('8765R','Juan Vila', 43,'Home',False),
                         ('4567P','Iris Vazquez',39,'Outros',True)]

        for usuario in listaUsuarios:
            modelo.append(usuario)
        modelo.set_sort_func(2,self.compara_edades,None)
        modeloFiltrado = modelo.filter_new()
        #modeloFiltrado.set_visible_func(self.filtro_usuarios_xenero)
        #modeloFiltrado.set_visible_func(self.filtro_usuarios_edade)
        modeloFiltrado.set_visible_func(self.filtros_usuarios)

        trvVista = Gtk.TreeView(model=modelo)

        for i, tituloColumna in enumerate (('Dni','Nome')):
            celda = Gtk.CellRendererText()
            celda.set_property("editable",True)
            celda.connect("edited",self.on_celdaNome_edited,i,modelo)
            columna = Gtk.TreeViewColumn(tituloColumna,celda,text = i)
            trvVista.append_column(columna)

        celda = Gtk.CellRendererProgress()
        columna = Gtk.TreeViewColumn('Edade',celda, value = 2)
        columna.set_sort_column_id(2)
        trvVista.append_column(columna)

        modeloComboXenero = Gtk.ListStore(str)
        modeloComboXenero.append(("Home",))
        modeloComboXenero.append(("Muller",))
        modeloComboXenero.append(("Outros",))

        celda = Gtk.CellRendererCombo()

        celda.set_property("editable",True)
        celda.props.model = modeloComboXenero
        celda.set_property("text-column",0)
        celda.set_property("has-entry",False)
        celda.connect("changed",self.on_xenero_changed,modelo)

        columna = Gtk.TreeViewColumn('Xénero', celda, text=3)
        trvVista.append_column(columna)

        celda = Gtk.CellRendererToggle()
        celda.set_property("sensitive",True)
        celda.connect("toggled", self.on_celdaFalecido_toogled,modelo)
        columna = Gtk.TreeViewColumn('Falecido',celda,active=4)
        trvVista.append_column(columna)

        caixav.pack_start(trvVista, True, True, 5)

        caixaH = Gtk.Box ( orientation= Gtk.Orientation.HORIZONTAL,spacing=4)
        rbtHome = Gtk.RadioButton(label = "Home")
        rbtMuller = Gtk.RadioButton.new_with_label_from_widget(rbtHome,label = "Muller")
        rbtOutros = Gtk.RadioButton.new_with_label_from_widget(rbtHome,label = "Outros")
        caixaH.pack_start(rbtHome,False,False,2)
        caixaH.pack_start(rbtMuller,False,False,2)
        caixaH.pack_start(rbtOutros,False,False,2)
        rbtHome.connect("toggled",self.on_xeneroToggled,modeloFiltrado)
        rbtMuller.connect("toggled",self.on_xeneroToggled,modeloFiltrado)
        rbtOutros.connect("toggled",self.on_xeneroToggled,modeloFiltrado)


        scale = Gtk.Scale.new_with_range(orientation= Gtk.Orientation.HORIZONTAL, min= 1, max=135, step=1)
        caixaH2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=6)
        rbtMayor = Gtk.RadioButton(label = "Mayor de")
        rbtMenor = Gtk.RadioButton.new_with_label_from_widget(rbtMayor, label="Menor de")
        caixaH2.pack_start(rbtMayor,False,False,2)
        caixaH2.pack_start(rbtMenor,False,False,2)
        scale.connect("value-changed",self.on_scaleEdad_changed,modeloFiltrado)
        rbtMayor.connect("toggled",self.on_rbtEdad_toggled,scale,modeloFiltrado)
        rbtMenor.connect("toggled",self.on_rbtEdad_toggled,scale,modeloFiltrado)



        caixav.pack_start(caixaH,True,True,0)
        caixav.pack_start(scale,True,True,5)
        caixav.pack_start(caixaH2,True,True,5)

        self.add(caixav)
        self.connect("delete_event",Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    EjemploTree()
    Gtk.main()