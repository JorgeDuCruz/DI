import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout, QComboBox, QTextEdit)

import ModeloLista


class Interfaz(QMainWindow):
    def cerrar(self):
        self.close()

    def on_comboBox_TextChanged(self,texto):
        print(texto)

    def on_comboBox_changed(self,indice):
        self.txtAreaTexto.append("Selecionaste el pokemon: "+self.pokedex[0][indice]+" número:"+str(self.pokedex[1][indice]))

    def __init__(self):
        super().__init__()
        maia = QGridLayout()
        self.pokedex = [("Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Eevee", "Mewtwo"),(25, 6, 1, 7, 133, 150)]

        caixaV = QVBoxLayout()
        txt = QLineEdit()
        txtPssw = QLineEdit()
        self.comboBox = QComboBox()
        self.comboBox.addItems(self.pokedex[0])
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
        self.comboBox.currentTextChanged.connect(self.on_comboBox_TextChanged)

        cerrarBoton = QPushButton("Cerrar")
        cerrarBoton.clicked.connect(self.cerrar)

        caixaV.addWidget(txt)
        caixaV.addWidget(txtPssw)
        caixaV.addWidget(self.comboBox)
        caixaV.addWidget(cerrarBoton)
        maia.addLayout(caixaV,1,0,1,1)

        self.txtAreaTexto = QTextEdit()
        maia.addWidget(self.txtAreaTexto, 1, 1, 1, 1)

        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()