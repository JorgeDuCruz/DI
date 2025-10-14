import sys,saudoQT

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget)

class VentanaHija(QMainWindow):
    def on_btnSaudo_clicked(self):
        if self.ventanPadre is not None:
            self.close()
            self.vp = self.ventanPadre
            self.vp.show()

    def __init__(self,ventanaPadre):
        super().__init__()
        self.ventanPadre = ventanaPadre
        self.setWindowTitle("Primera ventana con QT")
        self.setMinimumSize(400, 300)
        caixaV = QVBoxLayout()


        btnSaudo = QPushButton("Saúdo")
        btnSaudo.clicked.connect(self.on_btnSaudo_clicked)

        self.lblEtiqueta = QLabel("Inicio")
        fonte = self.lblEtiqueta.font()
        fonte.setPointSize(30)
        self.lblEtiqueta.setFont(fonte)
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        caixaV.addWidget(self.lblEtiqueta)
        caixaV.addWidget(btnSaudo)

        contaniner = QWidget()
        contaniner.setLayout(caixaV)

        self.setCentralWidget(contaniner)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaHija(None)
    aplicacion.exec()