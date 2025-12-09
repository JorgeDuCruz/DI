import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.uic import loadUi

class MinhaAplicacion:
    def __init__(self):
        self.aplicacion = QApplication(sys.argv)

        self.fiestra = loadUi("InterfaceQTCreator/form.ui")
        self.txtApelidos = self.fiestra.txtApelidos
        self.txtApelidos.setText("Hola")

        self.fiestra.show()

    def run(self):
        sys.exit(self.aplicacion.exec())

if __name__ == "__main__":
    apli = MinhaAplicacion()
    apli.run()