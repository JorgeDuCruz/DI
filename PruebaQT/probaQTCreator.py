import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi

class MinhaAplicacion:
    def __init__(self):
        self.aplicacion = QApplication(sys.argv)

        self.fiestra = loadUi("InterfaceQTCreator/form.ui")
        self.txtApelidos = self.fiestra.txtApelidos
        self.txtApelidos.setText("Hola")
        self.cmbNumeroCliente = self.fiestra.cmbNumeroCliente
        self.cmbNumeroCliente.insertItems(0,('1','2','3','4','5'))
        self.btnEditar = self.fiestra.btnEditar
        self.btnEditar.pressed.connect(self.on_btnEditar_pressed)

        self.fiestra.show()

    def run(self):
        sys.exit(self.aplicacion.exec())
    def on_btnEditar_pressed(self):
        numCliente = self.cmbNumeroCliente.currentText()
        self.txtApelidos.setText("O numero de cliente é: "+numCliente)

if __name__ == "__main__":
    apli = MinhaAplicacion()
    apli.run()