import sys,Ventana2

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout)

class PrimeraVentana(QMainWindow):
    def on_btnSaudo_clicked(self):
        nome = self.saludo.strip()
        if nome == "":
            nome = self.txtSaudo.text().strip()
        print("Pulsado")
        if nome != "" :
            print(nome)
            self.lblEtiqueta.setText("Hola "+nome)

        self.on_btnMaiusculas_toggled()
        self.saludo=""
        self.txtSaudo.clear()

    def on_btnVolver_clicked(self):
        self.close()
        self.vV.show()

    def on_btnMaiusculas_toggled(self):
        print("cambio")
        if self.chkMaiusculas.isChecked():
            self.lblEtiqueta.setText(self.lblEtiqueta.text().upper())
            self.txtSaudo.setText(self.txtSaudo.text().upper()) # esta linea no funciona
            self.maiusculas = True
        else:
            self.lblEtiqueta.setText(self.lblEtiqueta.text().lower())
            self.txtSaudo.setText(self.txtSaudo.text().lower()) # esta linea tampoco
            self.maiusculas = False

    def on_cambio_texto(self):
        if self.maiusculas:
            self.txtSaudo.setText(self.txtSaudo.text().upper())
        else:
            self.txtSaudo.setText(self.txtSaudo.text().lower())
        self.igualarTexto()


    def on_chkOculto_toogled(self):
        if self.chkOculto.isChecked():
            self.saludo = self.txtSaudo.text()
            self.txtSaudo.setText("*" * len(self.saludo))
        else:
            self.txtSaudo.setText(self.saludo)

    def igualarTexto(self):
        if self.chkOculto.isChecked():
            for letra in self.txtSaudo.text():
                if letra != "*":
                    indx = self.txtSaudo.text().find(letra)
                    if len(self.saludo)<len(self.txtSaudo.text()):
                        self.saludo = self.saludo[:indx]+letra+self.saludo[indx:]
                        break
            self.txtSaudo.setText("*"*len(self.saludo))
        print(self.saludo)

    def __init__(self):
        super().__init__()
        self.vV = Ventana2.VentanaHija(self)
        self.vV.hide()
        self.setWindowTitle("Primera ventana con QT")
        self.setMinimumSize(400,300)

        caixaV = QVBoxLayout()

        self.saludo = ""
        self.txtSaudo = QLineEdit()
        self.txtSaudo.setPlaceholderText("Introduce tu nombre")
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)
        self.txtSaudo.textChanged.connect(self.on_cambio_texto)

        btnSaudo = QPushButton("Saúdo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        """ cambiamos de un boton normal a una checkBox
        self.btnMaiuscula = QPushButton("Maiúsculas")
        self.btnMaiuscula.setCheckable(True)
        self.btnMaiuscula.setChecked(True)
        self.btnMaiuscula.toggled.connect(self.on_btnMaiusculas_toggled)
        """
        self.chkMaiusculas = QCheckBox("Maiusculas")
        self.chkMaiusculas.setChecked(False)
        self.chkMaiusculas.toggled.connect(self.on_btnMaiusculas_toggled)
        self.maiusculas = False

        self.chkOculto = QCheckBox("Ocultar")
        self.chkOculto.setChecked(False)
        self.chkOculto.toggled.connect(self.on_chkOculto_toogled)
        self.oculto = False


        btnVolver = QPushButton("Volver")
        btnVolver.clicked.connect(self.on_btnVolver_clicked)

        self.lblEtiqueta = QLabel("Hola a todos")
        self.lblEtiqueta.setText("Hola Mundo")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)


        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(self.txtSaudo)
        caixaV.addWidget(btnSaudo)
        caixaV.addWidget(btnVolver)

        caixaH = QHBoxLayout()
        caixaH.addWidget(self.chkMaiusculas)
        caixaH.addWidget(self.chkOculto)
        caixaV.addLayout(caixaH)
        contaniner = QWidget()
        contaniner.setLayout(caixaV)

        self.setCentralWidget(contaniner)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PrimeraVentana()
    aplicacion.exec()