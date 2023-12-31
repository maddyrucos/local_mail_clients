# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(982, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../madico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.group_mail = QtWidgets.QGroupBox(self.centralwidget)
        self.group_mail.setGeometry(QtCore.QRect(0, -30, 981, 591))
        self.group_mail.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.group_mail.setTitle("")
        self.group_mail.setObjectName("group_mail")
        self.photo = QtWidgets.QGraphicsView(self.group_mail)
        self.photo.setGeometry(QtCore.QRect(10, 40, 51, 41))
        self.photo.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.photo.setObjectName("photo")
        self.label_username = QtWidgets.QLabel(self.group_mail)
        self.label_username.setGeometry(QtCore.QRect(70, 40, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_username.setFont(font)
        self.label_username.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.label_username.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_username.setObjectName("label_username")
        self.label_name = QtWidgets.QLabel(self.group_mail)
        self.label_name.setGeometry(QtCore.QRect(70, 60, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("")
        self.label_name.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.tabWidget = QtWidgets.QTabWidget(self.group_mail)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 961, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_income = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_income.sizePolicy().hasHeightForWidth())
        self.tab_income.setSizePolicy(sizePolicy)
        self.tab_income.setObjectName("tab_income")
        self.table_income = QtWidgets.QTableWidget(self.tab_income)
        self.table_income.setGeometry(QtCore.QRect(-1, -1, 961, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_income.sizePolicy().hasHeightForWidth())
        self.table_income.setSizePolicy(sizePolicy)
        self.table_income.setStyleSheet("font: 75 9pt \"Segoe UI\";")
        self.table_income.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_income.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_income.setLineWidth(0)
        self.table_income.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_income.setTabKeyNavigation(False)
        self.table_income.setProperty("showDropIndicator", False)
        self.table_income.setDragDropOverwriteMode(False)
        self.table_income.setShowGrid(True)
        self.table_income.setGridStyle(QtCore.Qt.SolidLine)
        self.table_income.setObjectName("table_income")
        self.table_income.setColumnCount(4)
        self.table_income.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_income.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_income.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_income.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_income.setHorizontalHeaderItem(3, item)
        self.table_income.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_income, "")
        self.tab_sent = QtWidgets.QWidget()
        self.tab_sent.setObjectName("tab_sent")
        self.table_sent = QtWidgets.QTableWidget(self.tab_sent)
        self.table_sent.setGeometry(QtCore.QRect(0, 0, 961, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_sent.sizePolicy().hasHeightForWidth())
        self.table_sent.setSizePolicy(sizePolicy)
        self.table_sent.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_sent.setFrameShadow(QtWidgets.QFrame.Plain)
        self.table_sent.setLineWidth(0)
        self.table_sent.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.table_sent.setDragDropOverwriteMode(False)
        self.table_sent.setShowGrid(True)
        self.table_sent.setGridStyle(QtCore.Qt.SolidLine)
        self.table_sent.setObjectName("table_sent")
        self.table_sent.setColumnCount(4)
        self.table_sent.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_sent.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_sent.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_sent.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(52, 101, 164))
        self.table_sent.setHorizontalHeaderItem(3, item)
        self.table_sent.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_sent, "")
        self.button_new_message = QtWidgets.QPushButton(self.group_mail)
        self.button_new_message.setGeometry(QtCore.QRect(340, 40, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.button_new_message.setFont(font)
        self.button_new_message.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(238, 238, 236);")
        self.button_new_message.setDefault(False)
        self.button_new_message.setFlat(False)
        self.button_new_message.setObjectName("button_new_message")
        self.button_exit = QtWidgets.QPushButton(self.group_mail)
        self.button_exit.setGeometry(QtCore.QRect(880, 530, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(9)
        self.button_exit.setFont(font)
        self.button_exit.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button_exit.setObjectName("button_exit")
        self.button_update = QtWidgets.QPushButton(self.group_mail)
        self.button_update.setGeometry(QtCore.QRect(863, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.button_update.setFont(font)
        self.button_update.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(238, 238, 236);")
        self.button_update.setObjectName("button_update")
        self.group_login = QtWidgets.QGroupBox(self.centralwidget)
        self.group_login.setGeometry(QtCore.QRect(0, -20, 981, 611))
        self.group_login.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.group_login.setTitle("")
        self.group_login.setFlat(False)
        self.group_login.setObjectName("group_login")
        self.textfield_login_password = QtWidgets.QLineEdit(self.group_login)
        self.textfield_login_password.setGeometry(QtCore.QRect(360, 280, 261, 31))
        self.textfield_login_password.setText("")
        self.textfield_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textfield_login_password.setObjectName("textfield_login_password")
        self.label_login_incorrect_pass = QtWidgets.QLabel(self.group_login)
        self.label_login_incorrect_pass.setEnabled(True)
        self.label_login_incorrect_pass.setGeometry(QtCore.QRect(370, 420, 251, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login_incorrect_pass.setFont(font)
        self.label_login_incorrect_pass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_login_incorrect_pass.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_login_incorrect_pass.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_login_incorrect_pass.setTextFormat(QtCore.Qt.PlainText)
        self.label_login_incorrect_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.label_login_incorrect_pass.setObjectName("label_login_incorrect_pass")
        self.button_login_registration = QtWidgets.QPushButton(self.group_login)
        self.button_login_registration.setGeometry(QtCore.QRect(430, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.button_login_registration.setFont(font)
        self.button_login_registration.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.button_login_registration.setObjectName("button_login_registration")
        self.button_login_enter = QtWidgets.QPushButton(self.group_login)
        self.button_login_enter.setGeometry(QtCore.QRect(430, 320, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.button_login_enter.setFont(font)
        self.button_login_enter.setStyleSheet("color: rgb(238, 238, 236);\n"
"background-color: rgb(52, 101, 164);")
        self.button_login_enter.setObjectName("button_login_enter")
        self.textfield_login_username = QtWidgets.QLineEdit(self.group_login)
        self.textfield_login_username.setGeometry(QtCore.QRect(360, 220, 261, 31))
        self.textfield_login_username.setText("")
        self.textfield_login_username.setFrame(True)
        self.textfield_login_username.setObjectName("textfield_login_username")
        self.label_login_login = QtWidgets.QLabel(self.group_login)
        self.label_login_login.setGeometry(QtCore.QRect(360, 200, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login_login.setFont(font)
        self.label_login_login.setObjectName("label_login_login")
        self.label_login_passwrod = QtWidgets.QLabel(self.group_login)
        self.label_login_passwrod.setGeometry(QtCore.QRect(360, 260, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_login_passwrod.setFont(font)
        self.label_login_passwrod.setObjectName("label_login_passwrod")
        self.label_image = QtWidgets.QLabel(self.group_login)
        self.label_image.setGeometry(QtCore.QRect(420, 60, 128, 128))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.textfield_login_password.raise_()
        self.label_login_incorrect_pass.raise_()
        self.button_login_registration.raise_()
        self.button_login_enter.raise_()
        self.label_login_login.raise_()
        self.label_login_passwrod.raise_()
        self.textfield_login_username.raise_()
        self.label_image.raise_()
        self.group_registration = QtWidgets.QGroupBox(self.centralwidget)
        self.group_registration.setGeometry(QtCore.QRect(0, -20, 981, 581))
        self.group_registration.setStyleSheet("background-color: rgb(238, 238, 236);")
        self.group_registration.setTitle("")
        self.group_registration.setObjectName("group_registration")
        self.textfield_reg_notes = QtWidgets.QPlainTextEdit(self.group_registration)
        self.textfield_reg_notes.setGeometry(QtCore.QRect(40, 290, 901, 201))
        self.textfield_reg_notes.setObjectName("textfield_reg_notes")
        self.textfield_reg_username = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_username.setGeometry(QtCore.QRect(40, 50, 281, 31))
        self.textfield_reg_username.setObjectName("textfield_reg_username")
        self.textfield_reg_password = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_password.setGeometry(QtCore.QRect(40, 170, 281, 31))
        self.textfield_reg_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textfield_reg_password.setObjectName("textfield_reg_password")
        self.textfield_reg_password_again = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_password_again.setGeometry(QtCore.QRect(40, 230, 281, 31))
        self.textfield_reg_password_again.setEchoMode(QtWidgets.QLineEdit.Password)
        self.textfield_reg_password_again.setObjectName("textfield_reg_password_again")
        self.textfield_reg_name = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_name.setGeometry(QtCore.QRect(40, 110, 281, 31))
        self.textfield_reg_name.setObjectName("textfield_reg_name")
        self.textfield_reg_surname = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_surname.setGeometry(QtCore.QRect(360, 110, 271, 31))
        self.textfield_reg_surname.setObjectName("textfield_reg_surname")
        self.textfield_reg_father = QtWidgets.QLineEdit(self.group_registration)
        self.textfield_reg_father.setGeometry(QtCore.QRect(670, 110, 271, 31))
        self.textfield_reg_father.setObjectName("textfield_reg_father")
        self.label_reg_username = QtWidgets.QLabel(self.group_registration)
        self.label_reg_username.setGeometry(QtCore.QRect(40, 30, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_username.setFont(font)
        self.label_reg_username.setObjectName("label_reg_username")
        self.label_reg_name = QtWidgets.QLabel(self.group_registration)
        self.label_reg_name.setGeometry(QtCore.QRect(40, 90, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_name.setFont(font)
        self.label_reg_name.setObjectName("label_reg_name")
        self.label_reg_surname = QtWidgets.QLabel(self.group_registration)
        self.label_reg_surname.setGeometry(QtCore.QRect(360, 90, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_surname.setFont(font)
        self.label_reg_surname.setObjectName("label_reg_surname")
        self.label_reg_father = QtWidgets.QLabel(self.group_registration)
        self.label_reg_father.setGeometry(QtCore.QRect(670, 90, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_father.setFont(font)
        self.label_reg_father.setObjectName("label_reg_father")
        self.label_reg_password = QtWidgets.QLabel(self.group_registration)
        self.label_reg_password.setGeometry(QtCore.QRect(40, 150, 72, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_password.setFont(font)
        self.label_reg_password.setObjectName("label_reg_password")
        self.label_reg_passwrod_again = QtWidgets.QLabel(self.group_registration)
        self.label_reg_passwrod_again.setGeometry(QtCore.QRect(40, 210, 191, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_passwrod_again.setFont(font)
        self.label_reg_passwrod_again.setObjectName("label_reg_passwrod_again")
        self.label_reg_notes = QtWidgets.QLabel(self.group_registration)
        self.label_reg_notes.setGeometry(QtCore.QRect(40, 270, 381, 19))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setItalic(False)
        self.label_reg_notes.setFont(font)
        self.label_reg_notes.setObjectName("label_reg_notes")
        self.button_reg_back = QtWidgets.QPushButton(self.group_registration)
        self.button_reg_back.setGeometry(QtCore.QRect(40, 510, 94, 31))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(7)
        self.button_reg_back.setFont(font)
        self.button_reg_back.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"")
        self.button_reg_back.setObjectName("button_reg_back")
        self.button_reg_apply = QtWidgets.QPushButton(self.group_registration)
        self.button_reg_apply.setGeometry(QtCore.QRect(750, 500, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Pixel Anchor-Jack")
        font.setPointSize(8)
        self.button_reg_apply.setFont(font)
        self.button_reg_apply.setStyleSheet("background-color: rgb(52, 101, 164);\n"
"color: rgb(238, 238, 236);")
        self.button_reg_apply.setObjectName("button_reg_apply")
        self.label_reg_all_fields = QtWidgets.QLabel(self.group_registration)
        self.label_reg_all_fields.setGeometry(QtCore.QRect(280, 510, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(14)
        font.setItalic(False)
        self.label_reg_all_fields.setFont(font)
        self.label_reg_all_fields.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_reg_all_fields.setObjectName("label_reg_all_fields")
        self.label_reg_password_doesnt_match = QtWidgets.QLabel(self.group_registration)
        self.label_reg_password_doesnt_match.setGeometry(QtCore.QRect(330, 198, 301, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_reg_password_doesnt_match.setFont(font)
        self.label_reg_password_doesnt_match.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_reg_password_doesnt_match.setObjectName("label_reg_password_doesnt_match")
        self.group_login.raise_()
        self.group_registration.raise_()
        self.group_mail.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 18))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.actionAlpha_0_0_1 = QtWidgets.QAction(MainWindow)
        self.actionAlpha_0_0_1.setObjectName("actionAlpha_0_0_1")
        self.menu.addAction(self.actionAlpha_0_0_1)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MadMail"))
        self.label_username.setText(_translate("MainWindow", "username"))
        self.label_name.setText(_translate("MainWindow", "Имя"))
        self.table_income.setSortingEnabled(True)
        item = self.table_income.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "От кого"))
        item = self.table_income.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.table_income.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Текст"))
        item = self.table_income.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_income), _translate("MainWindow", "Входящие"))
        self.table_sent.setSortingEnabled(True)
        item = self.table_sent.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Кому"))
        item = self.table_sent.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тема"))
        item = self.table_sent.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Текст"))
        item = self.table_sent.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Дата и время"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sent), _translate("MainWindow", "Отправленные"))
        self.button_new_message.setText(_translate("MainWindow", "Написать\n"
"письмо"))
        self.button_exit.setText(_translate("MainWindow", "Выход"))
        self.button_update.setText(_translate("MainWindow", "Обновить"))
        self.label_login_incorrect_pass.setText(_translate("MainWindow", "Неверный логин или пароль!"))
        self.button_login_registration.setText(_translate("MainWindow", "Регистрация"))
        self.button_login_enter.setText(_translate("MainWindow", "Войти"))
        self.label_login_login.setText(_translate("MainWindow", "Логин"))
        self.label_login_passwrod.setText(_translate("MainWindow", "Пароль"))
        self.label_reg_username.setText(_translate("MainWindow", "*Логин"))
        self.label_reg_name.setText(_translate("MainWindow", "*Имя"))
        self.label_reg_surname.setText(_translate("MainWindow", "*Фамилия"))
        self.label_reg_father.setText(_translate("MainWindow", "Отчество"))
        self.label_reg_password.setText(_translate("MainWindow", "*Пароль"))
        self.label_reg_passwrod_again.setText(_translate("MainWindow", "*Повторно введите пароль"))
        self.label_reg_notes.setText(_translate("MainWindow", "Дополнительная информация (адрес, телефон и т.д.)"))
        self.button_reg_back.setText(_translate("MainWindow", "Назад"))
        self.button_reg_apply.setText(_translate("MainWindow", "Регистрация"))
        self.label_reg_all_fields.setText(_translate("MainWindow", "Заполните все *обязательные поля"))
        self.label_reg_password_doesnt_match.setText(_translate("MainWindow", "Пароли не совпадают!"))
        self.menu.setTitle(_translate("MainWindow", "О программе"))
        self.actionAlpha_0_0_1.setText(_translate("MainWindow", "Версия 0.0.1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
