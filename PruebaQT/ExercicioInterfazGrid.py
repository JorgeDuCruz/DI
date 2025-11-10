import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout)

import ModeloLista


class Interfaz(QMainWindow):
    def ocultar(self):
        indices = self.lstVisible.selectedIndexes()
        if indices:
            self.modeloOculto.follas.append(self.modeloVisible.follas[indices[0].row()])
            del self.modeloVisible.follas[indices[0].row()]
            self.modeloVisible.layoutChanged.emit()
            self.modeloOculto.layoutChanged.emit()
            self.lstVisible.clearSelection()


    def mostrar(self):
        indices = self.lstOculta.selectedIndexes()
        if indices:
            self.modeloVisible.follas.append( self.modeloOculto.follas[indices[0].row()])
            del self.modeloOculto.follas[indices[0].row()]
            self.modeloVisible.layoutChanged.emit()
            self.modeloOculto.layoutChanged.emit()
            self.lstOculta.clearSelection()

    def cerrar(self):
        self.close()

    def __init__(self):
        super().__init__()
        listaFollas = [("Folla 1","F"),("Documento 2","D"),("Folla 3","F")]
        self.modeloVisible = ModeloLista.ModeloFollas(listaFollas)
        self.modeloOculto = ModeloLista.ModeloFollas()

        self.setWindowTitle("Primera ventana con QT")
        maia = QGridLayout()
        lblFollasVisibles = QLabel("Follas Visibles")
        lblFollasOcultas = QLabel("Follas Ocultas")
        btnMOstrar = QPushButton("<<Mostrar")
        btnMOstrar.clicked.connect(self.mostrar)
        btnOcultar = QPushButton("Ocultar>>")
        btnOcultar.clicked.connect(self.ocultar)
        btnCerrar = QPushButton("Cerrar")
        btnCerrar.clicked.connect(self.cerrar)
        btnCerrar.setFixedSize(60,30)
        self.lstOculta = QListView()
        self.lstVisible = QListView()


        self.lstVisible.setModel(self.modeloVisible)
        self.lstOculta.setModel(self.modeloOculto)


        controlsInerte = QWidget()
        controlsInerte.setFixedSize(1,20)

        maia.addWidget(lblFollasVisibles)
        maia.addWidget(lblFollasOcultas,0,2,1,1)
        maia.addWidget(self.lstVisible,1,0,5,1)
        maia.addWidget(self.lstOculta,1,2,5,1)
        maia.addWidget(btnOcultar,1,1,1,1)
        maia.addWidget(btnMOstrar,3,1,1,1)
        maia.addWidget(btnMOstrar,7,1,1,1)
        maia.addWidget(btnCerrar,8,2,1,1,alignment=Qt.AlignmentFlag.AlignRight)

        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()