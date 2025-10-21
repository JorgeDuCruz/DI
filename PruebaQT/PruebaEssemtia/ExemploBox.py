import sys
import CaixaCor

from PyQt6.QtWidgets import QVBoxLayout,QHBoxLayout,QMainWindow,QWidget,QApplication

class ExemploBox(QMainWindow):
    def __init__(self):
        super().__init__()
        
        CaixaO = QHBoxLayout()

        CaixaI = QVBoxLayout()
        CaixaI.addWidget(CaixaCor.CaixaCor("red"))
        CaixaI.addWidget(CaixaCor.CaixaCor("yellow"))
        CaixaI.addWidget(CaixaCor.CaixaCor("purple"))

        CaixaC = QVBoxLayout()
        CaixaC.addWidget(CaixaCor.CaixaCor("green"))

        CaixaD = QVBoxLayout()
        CaixaD.addWidget(CaixaCor.CaixaCor("red"))
        CaixaD.addWidget(CaixaCor.CaixaCor("purple"))

        CaixaO.addLayout(CaixaI)
        CaixaO.addLayout(CaixaC)
        CaixaO.addLayout(CaixaD)

        widgetAux = QWidget()
        widgetAux.setLayout(CaixaO)
        self.setCentralWidget(widgetAux)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ExemploBox()
    sys.exit(app.exec())