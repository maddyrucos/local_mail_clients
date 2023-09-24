from PyQt5 import QtWidgets

from new_mail.ui import newmailui
import dialog
from new_mail.database import database
from datetime import datetime


class NewMail(QtWidgets.QMainWindow, newmailui.Ui_NewmailWindow):

    def __init__(self, username):
        super().__init__()
        self.setupUi(self)

        self.username = username

        self.button_send.clicked.connect(self.send_mail)

    def send_mail(self):
        address = self.textfield_address.text()
        theme = self.textfield_theme.text()
        text = self.textfield_text.toPlainText()
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if database.send_mail(self.username, address, theme, text, time):
            self.sent_dialog = dialog.Dialog('Сообщение отправлено!')
            self.sent_dialog.show()
            self.hide()

