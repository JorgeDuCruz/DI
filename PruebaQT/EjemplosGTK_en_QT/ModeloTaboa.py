from PyQt6 import QtGui
from PyQt6.QtCore import QAbstractTableModel,Qt

class ModeloTaboa(QAbstractTableModel):
    def __init__(self,taboa):
        super().__init__()
        self.taboa = taboa

    def rowCount(self,indice):
        return len(self.taboa)

    def columnCount(self, indice):
        return len(self.taboa[0]) if len(self.taboa ) != 0 else 0

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            if indice.column() == 3 and indice.row() > 0:
                return ""
            else:
                return self.taboa[indice.row()][indice.column()]
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.taboa[indice.row()][2] == "Home":
                return QtGui.QColor("lightblue")
            elif self.taboa[indice.row()][2] == "Muller" :
                return QtGui.QColor("pink")
        if rol == Qt.ItemDataRole.ForegroundRole:
            if self.taboa[indice.row()][3] == True:
                if indice.column()==3:
                    return QtGui.QColor("green")
        if rol == Qt.ItemDataRole.DecorationRole:
            if isinstance(self.taboa[indice.row()][indice.column()],bool):
                if self.taboa[indice.row()][indice.column()]:
                    return QtGui.QIcon("/home/dam/Documentos/DI/PruebaQT/tic16x16.jpg")
                else:
                    return QtGui.QIcon("/home/dam/Documentos/DI/PruebaQT/equis16x216.jpg")