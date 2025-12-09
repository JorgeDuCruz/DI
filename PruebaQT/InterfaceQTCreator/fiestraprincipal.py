# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_FiestraPrincipal

class FiestraPrincipal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FiestraPrincipal()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FiestraPrincipal()
    widget.show()
    sys.exit(app.exec())
