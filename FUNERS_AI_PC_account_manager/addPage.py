from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from ui.ui_add_dialog import Ui_Dialog
from log_module import Log_module


class AddpageWidget(Ui_Dialog, QDialog) :
    def __init__(self,module,signal):
        super().__init__()
        self.setupUi(self)  
        self.setWindowTitle("사용자 추가")
        self.setFixedSize(QSize(400, 700))
        self.module = module
        self.log_module = Log_module
        self.LE_account.setFocus
        self.BT_block_version_2.setChecked(False)
        self.BT_old_version.setChecked(True)
        self.BT_addAccount.clicked.connect(self.addAccount)
        self.signal = signal


    def addAccount(self):
        account = self.LE_account.text()
        keycount = self.SB_keyCount.text()
        owner = self.LE_owner.text()
        category = self.CB_category.currentText()
        memo = self.TE_memo.toPlainText()
        select =""
        if self.BT_block_version_2.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        check = self.module.read()
        print(check)
        count = 0
        a= []
        if(select == "auth"):
            a= check[0]
        else:
            a= check[1]
        for i in range(len(a)):
            if len(a) != 0 and account in a[i]:
                count = 1
                break
            else:
                count = 0

        if count == 1:
            self.overlap()
        elif int(keycount) <= 0:
            self.out()
        else:
            self.module.write(select,account, keycount, owner, category, memo)
            
            QMessageBox.information(self,"추가",f"{account}, {keycount}, {owner}, {category}, {memo}가 추가되었습니다")
            self.LE_account.setText("")
            self.SB_keyCount.setValue(0)
            self.LE_owner.setText("")
            self.CB_category.setCurrentText("구매")
            self.TE_memo.setText("")
            self.signal.emit(f"{account}, {keycount}, {owner}, {category}, {memo}가 추가되었습니다")
            self.hide()

    def overlap(self):
        QMessageBox.information(self,"중복","계정 아이디가 중복되었습니다.")

    def out(self):
        QMessageBox.information(self,"오류","1개 이상을 구매해 주십시오.")

if __name__ == "__main__":
    app = QApplication()
    mainWindow = AddpageWidget()
    mainWindow.show()
    sys.exit(app.exec_())