# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'masterId.ui'
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
        MainWindow.resize(472, 611)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, 0, 100, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"border-image:url(./image/Funers.png);\n"
"border:0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamily(u"Agency FB")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.verticalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(50, -1, 50, 30)
        self.Id_Value = QLineEdit(self.centralwidget)
        self.Id_Value.setObjectName(u"Id_Value")
        self.Id_Value.setMinimumSize(QSize(0, 40))
        self.Id_Value.setAutoFillBackground(False)
        self.Id_Value.setStyleSheet(u"font: 75 10pt \"NanumGothicExtraBold\";\n"
"background-color:rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2.5px;\n"
"border-radius: 10px;\n"
"border-color:  rgb(52, 145, 248);\n"
"padding-left: 10px;")

        self.verticalLayout_5.addWidget(self.Id_Value)

        self.Passward_value = QLineEdit(self.centralwidget)
        self.Passward_value.setObjectName(u"Passward_value")
        self.Passward_value.setMinimumSize(QSize(0, 40))
        self.Passward_value.setStyleSheet(u"font: 75 10pt \"NanumGothicExtraBold\";\n"
"background-color:rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2.5px;\n"
"border-radius: 10px;\n"
"border-color:  rgb(52, 145, 248);\n"
"padding-left:10px;")
        self.Passward_value.setEchoMode(QLineEdit.Password)

        self.verticalLayout_5.addWidget(self.Passward_value)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(75, -1, 75, 75)
        self.BT_login = QPushButton(self.centralwidget)
        self.BT_login.setObjectName(u"BT_login")
        self.BT_login.setMinimumSize(QSize(0, 30))
        self.BT_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.BT_login.setStyleSheet(u"font: 75 10pt \"NanumGothicExtraBold\";\n"
"background-color:rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2.5px;\n"
"border-radius: 10px;\n"
"border-color:  rgb(52, 145, 248);")

        self.verticalLayout_3.addWidget(self.BT_login)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2.setStretch(0, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 472, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FUNERS", None))
        self.Id_Value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.Passward_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ud328\uc2a4\uc6cc\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.BT_login.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778", None))
    # retranslateUi

