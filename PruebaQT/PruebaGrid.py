import sys,saudoQT


from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget,
                             QGridLayout)

from PruebaEssemtia.CaixaCor import CaixaCor


class EjemploGrid(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Primera ventana con QT")

        maia = QGridLayout()
        maia.addWidget(CaixaCor("red"))
        maia.addWidget(CaixaCor("blue"),0,1,1,2)
        maia.addWidget(CaixaCor("green"),1,0,2,1)
        maia.addWidget(CaixaCor("pink"),1,1,1,2)
        maia.addWidget(CaixaCor("orange"), 2, 1, 1, 1)
        maia.addWidget(CaixaCor("yellow"), 2, 2, 1, 1)



        contaniner = QWidget()
        contaniner.setLayout(maia)

        self.setCentralWidget(contaniner)
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = EjemploGrid()
    aplicacion.exec()