# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(188, 171)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameText = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameText.setGeometry(QtCore.QRect(10, 10, 161, 31))
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(10, 50, 161, 31))
        self.passwordText.setObjectName("passwordText")
        self.enterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.enterBtn.setGeometry(QtCore.QRect(80, 90, 94, 27))
        self.enterBtn.setObjectName("enterBtn")
        self.regBtn = QtWidgets.QPushButton(self.centralwidget)
        self.regBtn.setGeometry(QtCore.QRect(60, 130, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.regBtn.setFont(font)
        self.regBtn.setObjectName("regBtn")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.enterBtn.setText(_translate("LoginWindow", "Войти"))
        self.regBtn.setText(_translate("LoginWindow", "Регистрация"))

