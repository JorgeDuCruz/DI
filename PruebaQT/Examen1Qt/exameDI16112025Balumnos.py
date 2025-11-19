import sys


from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit)


class FiestraPrincipal (QMainWindow):
    def cerrar(self):
        self.close()


    def on_currentIndexChanged_cmbAlbara(self):
        indice = self.cmbAlbara.currentIndex()
        if indice is not None:
            contido =self.albaras[indice]
            print(contido)
            self.txtData.setText(contido[1])
            self.txtNumeroCliente.setText(contido[2])
            self.txtNomeCliente.setText(contido[3])
            self.txtApelidosCliente.setText(contido[4])
    def on_clicked_editar(self):
        contido = []
        contido.append(self.cmbAlbara.currentText())
        contido.append(self.txtData.text())
        contido.append(self.txtNumeroCliente.text())
        contido.append(self.txtNomeCliente.text())
        contido.append(self.txtApelidosCliente.text())
        self.txtArea.append(str(contido))


    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2025 grupo A")
        maia = QGridLayout()
        self.albaras= [
            ['1111nm','02/11/2024','1111','Ana','Ruiz'],
            ['2222io','08/03/2024','2222','Pedro','Diz'],
            ['3333qw','23/10/2025','3333','Rosa','Sanz'],
        ]


        gpbCliente = QGroupBox("Albará")
        maia.addWidget(gpbCliente,0,0,3,3)
        maiaGroup = QGridLayout()
        gpbCliente.setLayout(maiaGroup)
       

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblNumeroAlbara = QLabel("Número Albará")
        lblData = QLabel("Data")

        maiaGroup.addWidget(lblNumeroAlbara,0,0,1,1)
        maiaGroup.addWidget(lblNumeroCliente,1,0,1,1)
        maiaGroup.addWidget(lblApelidosCliente,2,0,1,1)
        maiaGroup.addWidget(lblData,0,2,1,1)
        maiaGroup.addWidget(lblNomeCliente,1,2,1,1)


        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtData = QLineEdit()
        self.cmbAlbara = QComboBox()
        self.cmbAlbara.currentIndexChanged.connect(self.on_currentIndexChanged_cmbAlbara)
        numAlba = []
        for num in self.albaras:
            numAlba.append(num[0])
        self.cmbAlbara.addItems(numAlba)

        maiaGroup.addWidget(self.cmbAlbara, 0, 1, 1, 1)
        maiaGroup.addWidget(self.txtNumeroCliente, 1, 1, 1, 1)
        maiaGroup.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)
        maiaGroup.addWidget(self.txtData, 0, 3, 1, 1)
        maiaGroup.addWidget(self.txtNomeCliente, 1, 3, 1, 1)


        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.on_clicked_editar)
        btnBorrar = QPushButton("Borrar")

        maia.addWidget(btnEngadir,4,0,1,1)
        maia.addWidget(btnEditar,4,1,1,1)
        maia.addWidget(btnBorrar,4,2,1,1)

        self.txtArea = QTextEdit()
        maia.addWidget(self.txtArea, 5, 0, 3, 3)

        btnAceptar = QPushButton("Aceptar")
        btnAceptar.setEnabled(False)
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.cerrar)

        maia.addWidget(btnCancelar,8,1,1,1)
        maia.addWidget(btnAceptar,8,2,1,1)


        aux = QWidget()
        aux.setLayout(maia)
        self.setCentralWidget(aux)
        self.show()





if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()

    aplicacion.exec()