from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from ui.ui_login_dialog import Ui_Dialog
import requests
import json


class LoginDialog(Ui_Dialog, QDialog) :


    def __init__(self,module,signal) :

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("로그인 페이지")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.BT_login.clicked.connect(self.login)
        self.module = module
        self.signal = signal


        


    def keyPressEvent(self, e): #키가 눌러졌을 때 실행됨
        if e.key() == Qt.Key_Return:
            self.login()
            

    def login(self):
        self.id =  f"{self.Id_Value.text()}|{self.Passward_value.text()}"
        response = requests.get(f"https://us-central1-just-test-tutorials.cloudfunctions.net/adminLogin?text={self.id}")
        res = json.loads(response.content.decode())
        print(res["result"])
        if res["result"] == "success":
            self.signal.emit(True)
            self.destroy()
        elif res["result"] == "IdError":
            QMessageBox.information(self,"중복","아이디가 일치하지 않습니다")
        else:
            QMessageBox.information(self,"오류","패스워드가 일치하지 않습니다")


        


if __name__ == "__main__":
    app = QApplication()
    mainWindow = LoginDialog(None)
    mainWindow.show()
    sys.exit(app.exec_())