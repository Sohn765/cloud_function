from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from ui.ui_main_window import Ui_MainWindow
from io_module import CSVModule
import csv
from login_dialog import LoginDialog
from log_module import Log_module
from addPage import AddpageWidget
# from addPage import AddpageWidget

class MainWindow(Ui_MainWindow, QMainWindow) :
    login_signal = Signal(bool)
    addAccount_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cellcount = 0
        self.module = CSVModule()
        self.log = Log_module()
        self.BT_block_version.setChecked(False)
        self.BT_old_version.setChecked(True)
        # self.PB_BT.clicked.connect(self.showAddpage)
        self.modify_BT.clicked.connect(self.modify)
        self.tableWidget.cellClicked.connect(self.cellCheck)
        self.delButton.clicked.connect(self.delButton_event)
        self.BT_useclaer.clicked.connect(self.useclaer)
        self.BT_block_version.clicked.connect(self.button_Click)
        self.BT_old_version.clicked.connect(self.button_Click)
        self.BT_search.clicked.connect(self.search)

        self.BT_F5.clicked.connect(self.F5)
        self.BT_Addpage.clicked.connect(self.showAddPage)
        self.list = self.module.read()
        self.readAll("auth")

        self.login_signal.connect(self.login)
        self.addAccount_signal.connect(self.account_Log)


        self.loginDialog = LoginDialog(self.module,self.login_signal)
        self.addpage = AddpageWidget(self.module,self.addAccount_signal)
        self.loginDialog.show()
        self.main.hide()

        self.text2.append(self.log.log(f"로그인에 성공하였습니다."))    

    
    def account_Log(self,accountMessage):
        self.text2.append(self.log.log(accountMessage)) 
    
    def login(self):
        self.main.show()
    
    def showAddPage(self):
        self.addpage.show()

    def addAccount(self):
        account = self.LE_account.text()
        keycount = self.SB_keyCount.text()
        owner = self.LE_owner.text()
        category = self.CB_category.currentText()
        memo = self.TE_memo.toPlainText()
        select =""
        if self.BT_block_version.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        check = self.module.read(select)
        print(check)
        count = 0

        for i in range(len(check)):
            if len(check) != 0 and account in check[i]:
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
            self.inputLine(self.index,account,keycount, owner, category, memo,0)
            self.index += 1
            QMessageBox.information(self,"추가",f"{account}, {keycount}, {owner}, {category}, {memo}가 추가되었습니다")


            self.LE_account.setText("")
            self.SB_keyCount.setValue(0)
            self.LE_owner.setText("")
            self.CB_category.setCurrentText("구매")
            self.TE_memo.setText("")

    def readAll(self,select):
        a= []
        if(select == "auth"):
            a= self.list[0]
        else:
            a= self.list[1]
            
        row = 0
        for line in a:
            try:
                self.inputLine(row, line[0], line[1], line[2], line[3], line[4],line[5])
                row += 1
            except:
                print(str(line) + "has wrong data.")
        self.index = row
        
    def inputLine(self, row=int, account=str, key=str, owner=str, category=str, memo=str,use = str):
        self.tableWidget.setRowCount(int(row)+1)
        self.tableWidget.setItem(int(row), 0, QTableWidgetItem(account))
        self.tableWidget.setItem(int(row), 1, QTableWidgetItem(str(key)))
        self.tableWidget.setItem(int(row), 2, QTableWidgetItem(owner))
        self.tableWidget.setItem(int(row), 3, QTableWidgetItem(category))
        self.tableWidget.setItem(int(row), 4, QTableWidgetItem(memo))   
        self.tableWidget.setItem(int(row), 5, QTableWidgetItem(str(use))) 
        # self.tableWidget.resizeColumnsToContents()

    def overlap(self):
        QMessageBox.information(self,"중복","계정 아이디가 중복되었습니다.")

    def out(self):
        QMessageBox.information(self,"오류","1개 이상을 구매해 주십시오.")

    def cellCheck(self):
        x = self.tableWidget.selectedIndexes()
        row = x[0].row()
        self.LE_account.setText(self.tableWidget.item(row, 0).text())
        self.SB_keyCount.setValue(int(self.tableWidget.item(row, 1).text()))
        self.LE_owner.setText(self.tableWidget.item(row, 2).text())
        self.CB_category.setCurrentText(self.tableWidget.item(row, 3).text())
        self.TE_memo.setText(self.tableWidget.item(row, 4).text())


    def modify(self):
        select =""
        if self.BT_block_version.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        x = self.tableWidget.selectedIndexes()
        row = x[0].row()
        self.module.read()
        account = self.LE_account.text()
        keycount = self.SB_keyCount.text()
        owner = self.LE_owner.text()
        category = self.CB_category.currentText()
        memo = self.TE_memo.toPlainText()

        list = [account, keycount, owner, category, memo]
        self.module.modify(select,account, keycount, owner, category, memo)

        for i in range(len(list)):
            self.tableWidget.setItem(row,i,QTableWidgetItem(list[i]))
        self.F5()
        QMessageBox.information(self,"수정",f"{account}, {keycount}, {owner}, {category},{memo}의 내용이 수정되었습니다")
        self.text2.append(self.log.log(f"{account}, {keycount}, {owner}, {category},{memo}의 내용이 수정되었습니다"))



    def deleteRow(self):
        select =""
        if self.BT_block_version.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        x = self.tableWidget.selectedIndexes()
        row = x[0].row()
        data = self.tableWidget.item(row, 0)
        self.module.delete(select,data.text())
        self.tableWidget.removeRow(row)
        self.index -= 1

        self.LE_account.setText("")
        self.SB_keyCount.setValue(0)
        self.LE_owner.setText("")
        self.CB_category.setCurrentText("구매")
        self.TE_memo.setText("")
        self.F5()

    def btnClicked(self):
        self.addAccount()

    def delButton_event(self):
        account = self.LE_account.text()
        buttonReply = QMessageBox.question(self,"삭제","정말로 삭제하시겠습니까?")
        if buttonReply == QMessageBox.Yes:
            QMessageBox.information(self,"삭제",f"{account}의 사용자가 삭제되었습니다")
            self.text2.append(self.log.log(f"{account}의 사용자가 삭제되었습니다"))
            self.deleteRow()
    
    def useclaer(self):
        account = self.LE_account.text()
        select =""
        if self.BT_block_version.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        x = self.tableWidget.selectedIndexes()
        row = x[0].row()
        data = self.tableWidget.item(row, 0)
        buttonReply = QMessageBox.question(self,"초기화","사용자를 초기화하시겠습니까?")
        if buttonReply == QMessageBox.Yes:
            self.module.useReset(select,data.text())
            self.readAll(select)
            QMessageBox.information(self,"초기화",f"{account}의 사용자가 초기화되었습니다")
            self.text2.append(self.log.log(f"{account}의 사용자가 초기화되었습니다"))
    
    def button_Click(self):
        if self.BT_block_version.isChecked():
            self.readAll("block")
        if self.BT_old_version.isChecked():
            self.readAll("auth")

    def F5(self):
        select =""
        if self.BT_block_version.isChecked():
            select = "block"
        if self.BT_old_version.isChecked():
            select = "auth"
        self.list = self.module.read()
        self.readAll(select)

    def search(self):
        select =[]
        c = []
        count = 0
        if self.BT_block_version.isChecked():
            select = self.list[1]
        if self.BT_old_version.isChecked():
            select = self.list[0]
        
        for i in select:
            if self.lineEdit.text() in i[0]:
                c.append(i)
                count +=1 
        
        if count == 0: QMessageBox.information(self,"검색",f"검색결과가 존재하지 않습니다.")


        row = 0
        for line in c:
            try:
                self.inputLine(row, line[0], line[1], line[2], line[3], line[4],line[5])
                row += 1
            except:
                print(str(line) + "has wrong data.")

        print(c)

if __name__ == '__main__':
    app = QApplication()
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())