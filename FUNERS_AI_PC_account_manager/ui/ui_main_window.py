# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1118, 740)
        self.main = QWidget(MainWindow)
        self.main.setObjectName(u"main")
        self.horizontalLayout_6 = QHBoxLayout(self.main)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.main)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.BT_old_version = QRadioButton(self.groupBox)
        self.BT_old_version.setObjectName(u"BT_old_version")
        font = QFont()
        font.setFamily(u"Gabriola")
        font.setBold(False)
        font.setWeight(50)
        self.BT_old_version.setFont(font)

        self.horizontalLayout_5.addWidget(self.BT_old_version)

        self.BT_block_version = QRadioButton(self.groupBox)
        self.BT_block_version.setObjectName(u"BT_block_version")
        self.BT_block_version.setFont(font)

        self.horizontalLayout_5.addWidget(self.BT_block_version)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.BT_F5 = QPushButton(self.groupBox)
        self.BT_F5.setObjectName(u"BT_F5")
        font1 = QFont()
        font1.setFamily(u"Gabriola")
        font1.setPointSize(10)
        self.BT_F5.setFont(font1)

        self.horizontalLayout_5.addWidget(self.BT_F5)


        self.horizontalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 0, -1)
        self.comboBox = QComboBox(self.main)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(self.main)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.BT_search = QPushButton(self.main)
        self.BT_search.setObjectName(u"BT_search")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BT_search.sizePolicy().hasHeightForWidth())
        self.BT_search.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.BT_search)

        self.BT_Addpage = QPushButton(self.main)
        self.BT_Addpage.setObjectName(u"BT_Addpage")

        self.horizontalLayout.addWidget(self.BT_Addpage)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tableWidget = QTableWidget(self.main)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(663, 400))
        self.tableWidget.setStyleSheet(u"text-align: center;")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setIconSize(QSize(0, 0))
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.tableWidget)

        self.text2 = QTextBrowser(self.main)
        self.text2.setObjectName(u"text2")

        self.verticalLayout_3.addWidget(self.text2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.LE_account = QLineEdit(self.main)
        self.LE_account.setObjectName(u"LE_account")
        self.LE_account.setEnabled(False)

        self.gridLayout.addWidget(self.LE_account, 0, 2, 1, 1)

        self.CB_category = QComboBox(self.main)
        self.CB_category.addItem("")
        self.CB_category.addItem("")
        self.CB_category.addItem("")
        self.CB_category.setObjectName(u"CB_category")

        self.gridLayout.addWidget(self.CB_category, 3, 2, 1, 1)

        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.main)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.main)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.SB_keyCount = QSpinBox(self.main)
        self.SB_keyCount.setObjectName(u"SB_keyCount")

        self.gridLayout.addWidget(self.SB_keyCount, 1, 2, 1, 1)

        self.label_5 = QLabel(self.main)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.LE_owner = QLineEdit(self.main)
        self.LE_owner.setObjectName(u"LE_owner")

        self.gridLayout.addWidget(self.LE_owner, 2, 2, 1, 1)

        self.TE_memo = QTextEdit(self.main)
        self.TE_memo.setObjectName(u"TE_memo")

        self.gridLayout.addWidget(self.TE_memo, 4, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.modify_BT = QPushButton(self.main)
        self.modify_BT.setObjectName(u"modify_BT")

        self.horizontalLayout_3.addWidget(self.modify_BT)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.delButton = QPushButton(self.main)
        self.delButton.setObjectName(u"delButton")

        self.horizontalLayout_2.addWidget(self.delButton)

        self.BT_useclaer = QPushButton(self.main)
        self.BT_useclaer.setObjectName(u"BT_useclaer")

        self.horizontalLayout_2.addWidget(self.BT_useclaer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout)

        self.horizontalLayout_6.setStretch(0, 2)
        MainWindow.setCentralWidget(self.main)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1118, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.BT_old_version.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc874\ubc84\uc804", None))
        self.BT_block_version.setText(QCoreApplication.translate("MainWindow", u"\ube14\ub85d\ubc84\uc804", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.BT_F5.setText(QCoreApplication.translate("MainWindow", u"\uc0c8\ub85c\uace0\uce68", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\uacc4\uc815", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud0a4 \uac1c\uc218", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc720\ud615", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\uba54\ubaa8", None))

        self.BT_search.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.BT_Addpage.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790 \ucd94\uac00", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ud0a4 \uac1c\uc218", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc720\uc790", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc720\ud615", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uba54\ubaa8", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc911", None));
        self.CB_category.setItemText(0, QCoreApplication.translate("MainWindow", u"\uad6c\ub9e4", None))
        self.CB_category.setItemText(1, QCoreApplication.translate("MainWindow", u"\ubb34\uc0c1", None))
        self.CB_category.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc784\uc2dc", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud0a4 \uac1c\uc218", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc18c\uc720\uc790", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc720\ud615", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"   \uba54\ubaa8", None))
        self.modify_BT.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.BT_useclaer.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790 \ucd08\uae30\ud654", None))
    # retranslateUi

