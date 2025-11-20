import  gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk,Gdk,GObject


class EjemploGlade:
    def on_cmbAlbara_changed(self,boton):
        pass
    def on_btnEngadir_clicked(self, boton):
        pass
    def on_btnEditar_clicked(self, boton):
        pass
    def on_btnBorrar_clicked(self, boton):
        pass
    def on_btnAceptar_clicked(self, boton):
        pass
    def on_btnCancelar_clicked(self, boton):
        pass


    def __init__(self):

        listaCabeceiraAlbara = ['Código','Descripción',"Cantidade","Prezo ud","Prezo Total"]
        listaDetalleAlbara = [["00012",'Parafuxo M8',100,0.02,2],
                              ["00013",'Arandela 10',200,0.001,0.2],
                              ["00014",'Porca M6',10,0.01,0.1],
                              ["00015",'Varilla roscada M6',10,0.50,5]]

        builder = Gtk.Builder()
        builder.add_from_file("formularioAlbara.glade")
        wndPrincipal = builder.get_object("wndPrincipal")
        self.trvDetallealbara = builder.get_object("trvDetallealbara")

        sinais = {"on_wndPrincipal_delete_event":Gtk.main_quit,
                  "on_cmbAlbara_changed":self.on_cmbAlbara_changed,
                  "on_btnEngadir_clicked":self.on_btnEngadir_clicked,
                  "on_btnEditar_clicked":self.on_btnEditar_clicked,
                  "on_btnBorrar_clicked":self.on_btnBorrar_clicked,
                  "on_btnAceptar_clicked":self.on_btnAceptar_clicked,
                  "on_btnCancelar_clicked":self.on_btnCancelar_clicked}
        builder.connect_signals(sinais)

        modelo = Gtk.ListStore(str,str,int,float,float)
        for entrada in listaDetalleAlbara:
            modelo.append(entrada)
        self.trvDetallealbara.set_model(modelo)




if __name__ == "__main__":
    EjemploGlade()
    Gtk.main()