import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout)

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera ventana con QT")
        maia = QGridLayout()
        lblFollasVisibles = QLabel("Follas Visibles")
        lblFollasOcultas = QLabel("Follas Ocultas")
        btnMOstrar = QPushButton("<<Mostrar")
        btnOcultar = QPushButton("Ocultar>>")
        btnCerrar = QPushButton("Cerrar")
        btnCerrar.setFixedSize(60,30)
        lstOculta = QListView()
        lstVisible = QListView()

        controlsInerte = QPushButton()
        controlsInerte.setFixedSize(1,20)

        maia.addWidget(lblFollasVisibles)
        maia.addWidget(lblFollasOcultas,0,2,1,1)
        maia.addWidget(lstVisible,1,0,5,1)
        maia.addWidget(lstOculta,1,2,5,1)
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