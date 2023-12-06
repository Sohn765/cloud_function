# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(426, 569)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, 0, 100, 0)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(200, 200))
        self.label.setPixmap(QPixmap(u":/image/image/Funers.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.label_2 = QLabel(Dialog)
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
        self.Id_Value = QLineEdit(Dialog)
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

        self.Passward_value = QLineEdit(Dialog)
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
        self.BT_login = QPushButton(Dialog)
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


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"login", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"FUNERS", None))
        self.Id_Value.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uad00\ub9ac\uc790 \uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.Passward_value.setPlaceholderText(QCoreApplication.translate("Dialog", u"\ud328\uc2a4\uc6cc\ub4dc\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.BT_login.setText(QCoreApplication.translate("Dialog", u"\ub85c\uadf8\uc778", None))
    # retranslateUi

