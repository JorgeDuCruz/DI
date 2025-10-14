import sys,Ventana2

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

class PrimeraVentana(QMainWindow):
    def on_btnSaudo_clicked(self):
        nome = self.txtSaudo.text().strip()
        print("Pulsado")
        if nome != "" :
            print(nome)
            self.lblEtiqueta.setText("Hola "+nome)
            self.txtSaudo.clear()

    def on_btnVolver_clicked(self):
        self.close()
        self.vV.show()

    def on_btnMaiusculas_toggled(self):
        print("cambio")

    def __init__(self):
        super().__init__()
        self.vV = Ventana2.VentanaHija(self)
        self.vV.hide()
        self.setWindowTitle("Primera ventana con QT")
        self.setMinimumSize(400,300)

        caixaV = QVBoxLayout()

        self.txtSaudo = QLineEdit()
        self.txtSaudo.setPlaceholderText("Introduce tu nombre")
        self.txtSaudo.returnPressed.connect(self.on_btnSaudo_clicked)

        btnSaudo = QPushButton("Saúdo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked())

        btnMaiuscula = QPushButton("maiusculas")
        btnMaiuscula.setCheckable(True)
        btnMaiuscula.toggled.connect(self.on_btnMaiusculas_toggled)
        self.maiusculas = True

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

        contaniner = QWidget()
        contaniner.setLayout(caixaV)

        self.setCentralWidget(contaniner)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PrimeraVentana()
    aplicacion.exec()