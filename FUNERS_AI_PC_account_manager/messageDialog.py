from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.ui_addpage  import Ui_Dialog

class MessageDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check_button.clicked.connect(self.Popup)

    def Popup(self):
        QMessageBox.information(self, "BIG","오케이")
        
        
