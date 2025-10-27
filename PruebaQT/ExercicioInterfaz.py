import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView)

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Primera ventana con QT")
        self.setMinimumSize(400,300)

        caixaH = QHBoxLayout()

        caixaVisibles = QVBoxLayout()
        self.tituloVisible = QLabel("Hojas visibles:")
        self.listaVisibles = QListView()
        caixaVisibles.addWidget(self.tituloVisible)
        caixaVisibles.addWidget(self.listaVisibles)
        caixaVisibles.addWidget(QLabel(None))
        caixaH.addLayout(caixaVisibles)

        botonesCentrales = QVBoxLayout()
        self.botonOcultar = QPushButton("Ocultar>>")
        self.botonMostrar = QPushButton("<<Mostrar")
        botonesCentrales.addWidget(self.botonOcultar)
        botonesCentrales.addWidget(self.botonMostrar)
        caixaH.addLayout(botonesCentrales)

        caixaOcultas = QVBoxLayout()
        self.tituloOculto = QLabel("Hojas ocultas:")
        self.listaOculto = QListView()
        caixaOcultas.addWidget(self.tituloOculto)
        caixaOcultas.addWidget(self.listaOculto)

        self.botonCerrar = QPushButton("Cerrar")
        self.botonCerrar.setFixedSize(60,30)
        caixaOcultas.addWidget(self.botonCerrar,alignment=Qt.AlignmentFlag.AlignRight)
        caixaH.addLayout(caixaOcultas)


        aux = QWidget()
        aux.setLayout(caixaH)
        self.setCentralWidget(aux)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()