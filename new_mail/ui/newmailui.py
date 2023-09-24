# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newmail.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewmailWindow(object):
    def setupUi(self, NewmailWindow):
        NewmailWindow.setObjectName("NewmailWindow")
        NewmailWindow.resize(660, 324)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewmailWindow.sizePolicy().hasHeightForWidth())
        NewmailWindow.setSizePolicy(sizePolicy)
        NewmailWindow.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(NewmailWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textfield_address = QtWidgets.QLineEdit(self.centralwidget)
        self.textfield_address.setGeometry(QtCore.QRect(10, 30, 241, 27))
        self.textfield_address.setInputMask("")
        self.textfield_address.setFrame(True)
        self.textfield_address.setObjectName("textfield_address")
        self.textfield_theme = QtWidgets.QLineEdit(self.centralwidget)
        self.textfield_theme.setGeometry(QtCore.QRect(10, 90, 241, 27))
        self.textfield_theme.setObjectName("textfield_theme")
        self.textfield_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textfield_text.setGeometry(QtCore.QRect(10, 150, 631, 161))
        self.textfield_text.setObjectName("textfield_text")
        self.label_address = QtWidgets.QLabel(self.centralwidget)
        self.label_address.setGeometry(QtCore.QRect(10, 10, 241, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_address.setFont(font)
        self.label_address.setObjectName("label_address")
        self.label_theme = QtWidgets.QLabel(self.centralwidget)
        self.label_theme.setGeometry(QtCore.QRect(10, 70, 241, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_theme.setFont(font)
        self.label_theme.setObjectName("label_theme")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(10, 130, 241, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_text.setFont(font)
        self.label_text.setObjectName("label_text")
        self.button_send = QtWidgets.QPushButton(self.centralwidget)
        self.button_send.setGeometry(QtCore.QRect(510, 80, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(9)
        self.button_send.setFont(font)
        self.button_send.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(238, 238, 236);")
        self.button_send.setFlat(False)
        self.button_send.setObjectName("button_send")
        NewmailWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NewmailWindow)
        QtCore.QMetaObject.connectSlotsByName(NewmailWindow)

    def retranslateUi(self, NewmailWindow):
        _translate = QtCore.QCoreApplication.translate
        NewmailWindow.setWindowTitle(_translate("NewmailWindow", "Новое сообщение"))
        self.label_address.setText(_translate("NewmailWindow", "Получатель"))
        self.label_theme.setText(_translate("NewmailWindow", "Тема"))
        self.label_text.setText(_translate("NewmailWindow", "Текст"))
        self.button_send.setText(_translate("NewmailWindow", "Отправить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewmailWindow = QtWidgets.QMainWindow()
    ui = Ui_NewmailWindow()
    ui.setupUi(NewmailWindow)
    NewmailWindow.show()
    sys.exit(app.exec_())
