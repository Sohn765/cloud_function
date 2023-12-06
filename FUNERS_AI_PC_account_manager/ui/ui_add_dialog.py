# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 663)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.BT_old_version = QRadioButton(self.groupBox)
        self.BT_old_version.setObjectName(u"BT_old_version")

        self.horizontalLayout_2.addWidget(self.BT_old_version)

        self.BT_block_version_2 = QRadioButton(self.groupBox)
        self.BT_block_version_2.setObjectName(u"BT_block_version_2")

        self.horizontalLayout_2.addWidget(self.BT_block_version_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.LE_owner = QLineEdit(Dialog)
        self.LE_owner.setObjectName(u"LE_owner")

        self.gridLayout.addWidget(self.LE_owner, 2, 2, 1, 1)

        self.TE_memo = QTextEdit(Dialog)
        self.TE_memo.setObjectName(u"TE_memo")

        self.gridLayout.addWidget(self.TE_memo, 4, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.LE_account = QLineEdit(Dialog)
        self.LE_account.setObjectName(u"LE_account")
        self.LE_account.setEnabled(True)

        self.gridLayout.addWidget(self.LE_account, 0, 2, 1, 1)

        self.SB_keyCount = QSpinBox(Dialog)
        self.SB_keyCount.setObjectName(u"SB_keyCount")

        self.gridLayout.addWidget(self.SB_keyCount, 1, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.CB_category = QComboBox(Dialog)
        self.CB_category.addItem("")
        self.CB_category.addItem("")
        self.CB_category.addItem("")
        self.CB_category.setObjectName(u"CB_category")

        self.gridLayout.addWidget(self.CB_category, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.BT_addAccount = QPushButton(Dialog)
        self.BT_addAccount.setObjectName(u"BT_addAccount")

        self.verticalLayout.addWidget(self.BT_addAccount)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.BT_old_version.setText(QCoreApplication.translate("Dialog", u"\uae30\uc874\ubc84\uc804", None))
        self.BT_block_version_2.setText(QCoreApplication.translate("Dialog", u"\ube14\ub85d\ubc84\uc804", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\uacc4\uc815 \uc720\ud615", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\uacc4\uc815", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\ud0a4 \uac1c\uc218", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"   \uba54\ubaa8", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\uc18c\uc720\uc790", None))
        self.CB_category.setItemText(0, QCoreApplication.translate("Dialog", u"\uad6c\ub9e4", None))
        self.CB_category.setItemText(1, QCoreApplication.translate("Dialog", u"\ubb34\uc0c1", None))
        self.CB_category.setItemText(2, QCoreApplication.translate("Dialog", u"\uc784\uc2dc", None))

        self.BT_addAccount.setText(QCoreApplication.translate("Dialog", u"\ucd94\uac00", None))
    # retranslateUi

