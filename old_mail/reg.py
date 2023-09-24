# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_regWindow(object):
    def setupUi(self, regWindow):
        regWindow.setObjectName("regWindow")
        regWindow.resize(298, 328)
        self.centralwidget = QtWidgets.QWidget(regWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameText = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameText.setGeometry(QtCore.QRect(10, 10, 131, 31))
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(10, 60, 131, 31))
        self.passwordText.setObjectName("passwordText")
        self.nameText = QtWidgets.QLineEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.nameText.setObjectName("nameText")
        self.lastnameText = QtWidgets.QLineEdit(self.centralwidget)
        self.lastnameText.setGeometry(QtCore.QRect(10, 160, 131, 31))
        self.lastnameText.setObjectName("lastnameText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 10, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 60, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 110, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 160, 111, 31))
        self.label_4.setObjectName("label_4")
        self.notesText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.notesText.setGeometry(QtCore.QRect(10, 200, 131, 71))
        self.notesText.setObjectName("notesText")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(140, 220, 101, 31))
        self.label_5.setObjectName("label_5")
        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(150, 286, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.regBtn.setFont(font)
        self.regBtn.setObjectName("regBtn")
        regWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(regWindow)
        QtCore.QMetaObject.connectSlotsByName(regWindow)

    def retranslateUi(self, regWindow):
        _translate = QtCore.QCoreApplication.translate
        regWindow.setWindowTitle(_translate("regWindow", "Registration"))
        self.label.setText(_translate("regWindow", " - логин*"))
        self.label_2.setText(_translate("regWindow", " - пароль*"))
        self.label_3.setText(_translate("regWindow", " - имя*"))
        self.label_4.setText(_translate("regWindow", " - фамилия*"))
        self.label_5.setText(_translate("regWindow", " - заметки"))
        self.regBtn.setText(_translate("regWindow", "Зарегистрироваться"))

