from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from new_mail.ui import mainwindow

from new_mail.database import database
import dialog
import newmail

import sys

import hashpass


class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.show()
        self.setupUi(self)

        self.username = ''

        self.setWindowIcon(QtGui.QIcon('images/madico_128.png'))

        # Группа окна авторизации
        self.group_login.setVisible(True)
        self.button_login_enter.clicked.connect(self.try_auth)
        self.button_login_registration.clicked.connect(self.open_registration)

        self.pix = QtGui.QPixmap('images/madico_128.png')
        self.label_image.setPixmap(self.pix)

        self.label_login_incorrect_pass.setVisible(False)

        # Группа главного окна
        self.group_mail.setVisible(False)
        self.button_exit.clicked.connect(self.back_to_login)
        self.button_new_message.clicked.connect(self.new_message)
        self.button_update.clicked.connect(self.update_mails)

        self.table_income.resizeRowsToContents()

        self.table_income.setColumnWidth(0, 125)
        self.table_income.setColumnWidth(1, 125)
        self.table_income.setColumnWidth(2, 520)
        self.table_income.setColumnWidth(3, 180)

        self.table_sent.resizeRowsToContents()

        self.table_sent.setColumnWidth(0, 125)
        self.table_sent.setColumnWidth(1, 125)
        self.table_sent.setColumnWidth(2, 520)
        self.table_sent.setColumnWidth(3, 180)

        # Группа окна регистрации
        self.group_registration.setVisible(False)

        self.button_reg_apply.clicked.connect(self.register_user)
        self.button_reg_back.clicked.connect(self.back_to_login)

        self.label_reg_all_fields.setVisible(False)
        self.label_reg_password_doesnt_match.setVisible(False)

    def back_to_login(self):

        self.group_registration.setVisible(False)
        self.group_mail.setVisible(False)
        self.group_login.setVisible(True)
        self.textfield_login_username.setText('')
        self.textfield_login_password.setText('')

    def try_auth(self):

        username = self.textfield_login_username.text()
        password = self.textfield_login_password.text()

        hashed_password = hashpass.hash_password(password)

        if database.check_auth(username, hashed_password):
            self.username = username
            self.init_mail_window(username)
            self.update_mails()

        else:
            self.label_login_incorrect_pass.setVisible(True)

    def init_mail_window(self, username):

        self.group_login.setVisible(False)
        self.group_mail.setVisible(True)
        user_info = database.get_user_info(username)
        self.label_username.setText(f'{username}@mad.mail')
        self.label_name.setText(f'{user_info[2]} {user_info[3]} {user_info[4]}')

    def update_mails(self):

        income_mails = database.get_income_mails(self.username)
        sent_mails = database.get_sent_mails(self.username)

        self.table_income.setRowCount(len(income_mails))
        self.table_sent.setRowCount(len(sent_mails))

        for row, values in enumerate(income_mails):
            for column, value in enumerate(values):
                self.table_income.setItem(row, column, QtWidgets.QTableWidgetItem(value))

        self.table_income.resizeRowsToContents()

        for row, values in enumerate(sent_mails):
            for column, value in enumerate(values):
                self.table_sent.setItem(row, column, QtWidgets.QTableWidgetItem(value))

        self.table_income.sortItems(3, order=Qt.DescendingOrder)

    def new_message(self):
        self.new_message_window = newmail.NewMail(self.username)
        self.new_message_window.show()

    def open_registration(self):

        self.group_login.setVisible(False)
        self.group_registration.setVisible(True)

    def register_user(self):

        all_fields_not_empty = True

        if self.textfield_reg_username.text() == '':
            all_fields_not_empty = False

        elif self.textfield_reg_name.text() == '':
            all_fields_not_empty = False

        elif self.textfield_reg_surname.text() == '':
            all_fields_not_empty = False

        elif self.textfield_reg_password.text() == '':
            all_fields_not_empty = False

        elif self.textfield_reg_password_again.text() == '':
            all_fields_not_empty = False

        if all_fields_not_empty == False:
            self.label_reg_all_fields.setVisible(True)

        else:
            self.label_reg_all_fields.setVisible(False)
            self.label_reg_password_doesnt_match.setVisible(False)
            username = self.textfield_reg_username.text()
            password = self.textfield_reg_password.text()
            hashed_password = hashpass.hash_password(password)
            name = self.textfield_reg_name.text()
            surname = self.textfield_reg_surname.text()
            fathername = self.textfield_reg_father.text()
            notes = self.textfield_reg_notes.toPlainText()

            if self.textfield_reg_password.text() == self.textfield_reg_password_again.text():
                register_user = database.register_user(username, hashed_password, name, surname, fathername, notes)

                if register_user == 'existed':
                    self.new_user_dialog = dialog.Dialog('Такой аккаунт уже существует!\nПоздравляем, теперь он Ваш!')
                    self.new_user_dialog.show_dialog()

                elif register_user == 'new':
                    self.new_user_dialog = dialog.Dialog('Новый аккаунт создан!')
                    self.new_user_dialog.show_dialog()

                self.group_registration.setVisible(False)
                self.group_login.setVisible(True)

            else:
                self.label_reg_password_doesnt_match.setVisible(True)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    database.create_db()



    main = MainWindow()

    app.exec()