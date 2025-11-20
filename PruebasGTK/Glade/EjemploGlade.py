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

        listaDetalleAlbara = [["00012",'']]

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
        self.trvDetallealbara.set_model()



if __name__ == "__main__":
    EjemploGlade()
    Gtk.main()