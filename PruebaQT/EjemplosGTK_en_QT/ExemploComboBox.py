import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QListView, QGridLayout, QComboBox, QTextEdit, QRadioButton, QButtonGroup,
                             QTableView, QTabWidget)
from EjemplosGTK_en_QT.ModeloTaboa import ModeloTaboa


class Interfaz(QMainWindow):
    def cerrar(self):
        self.close()

    def on_comboBox_TextChanged(self,texto):
        print(texto)

    def on_comboBox_changed(self,indice):
        self.txtAreaTexto.append("Selecionaste el pokemon: "+self.pokedex[0][indice]+" número:"+str(self.pokedex[1][indice]))

    def on_taboa_selectionChanged(self):
        indices = self.taboa.selectedIndexes()
        if indices is not None:
            contenido = self.modelo.taboa[indices[0].row()][indices[0].column()]
            print(contenido)
            self.txtAreaTexto.append(str(contenido))

    def on_rb1_toggled(self):
        if self.rb1.isChecked():
            campos = self.txtAreaTexto.toPlainText().split(",")
            self.modelo.taboa.append([campos[0],campos[1],campos[2],True if campos[3]=="True" else False])
            self.modelo.layoutChanged.emit()
            print(campos)

    def __init__(self):
        super().__init__()
        maia = QGridLayout()
        self.setMinimumSize(1000,500)
        self.pokedex = [("Pikachu", "Charizard", "Bulbasaur", "Squirtle", "Eevee", "Mewtwo"),(25, 6, 1, 7, 133, 150)]
        datos = [["Nome","DNI","Xenero","Falecido"],
                 ["Ana","3456J","Muller",False],
                 ["Pepe","9876T","Home",True]]

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

        grupo1 = QButtonGroup(self)

        grupo2 = QButtonGroup(self)

        caixaV2 = QVBoxLayout()
        self.rb1 = QRadioButton("Botón 1")
        self.rb1.toggled.connect(self.on_rb1_toggled)
        self.rb2 = QRadioButton("Botón 2")
        self.rb3 = QRadioButton("Botón 3")
        self.rb4 = QRadioButton("Botón 4")


        grupo1.addButton(self.rb1)
        grupo1.addButton(self.rb2)
        grupo2.addButton(self.rb3)
        grupo2.addButton(self.rb4)

        caixaV2.addWidget(self.rb1)
        caixaV2.addWidget(self.rb2)
        caixaV2.addWidget(self.rb3)
        caixaV2.addWidget(self.rb4)
        maia.addLayout(caixaV2,0,0,1,1)

        clasificador = QTabWidget()
        clasificador.setTabPosition(QTabWidget.TabPosition.North)

        self.taboa = QTableView()
        self.taboa.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.modelo = ModeloTaboa(datos)
        self.taboa.setModel(self.modelo)
        self.seleccion = self.taboa.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_taboa_selectionChanged)

        clasificador.addTab(self.taboa,"Taboa")
        txtOutro = QTextEdit()
        clasificador.addTab(txtOutro,"Cadro de texto")


        maia.addWidget(clasificador,0,1,1,1)

        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Interfaz()
    aplicacion.exec()