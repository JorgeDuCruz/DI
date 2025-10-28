import sys
from  PyQt6.QtCore import Qt,QAbstractListModel
from PyQt6.QtGui import QImage

doc = QImage('imgs/unDocs.png')
fol = QImage('imgs/unFol.png')
class ModeloFollas (QAbstractListModel):
    def __init__(self,follas = None):
        super().__init__()
        self.follas = follas or []

    def rowCount(self, indice):
        return len(self.follas)

    def data(self,indice,rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            texto,_ = self.follas [indice.row()]
            return texto
        if rol == Qt.ItemDataRole.DecorationRole:
            _,tipo = self.follas[indice.row()]
            if tipo == "F":
                return fol
            elif tipo=="D":
                return doc