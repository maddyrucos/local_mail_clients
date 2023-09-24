from PyQt5 import QtWidgets

from new_mail.ui import dialogui


class Dialog(QtWidgets.QMainWindow, dialogui.Ui_Dialog):

    def __init__(self, text):
        super().__init__()
        self.setupUi(self)

        self.text = text

        self.button_ok.clicked.connect(self.close_dialog)

        self.label.setText(self.text)

    def close_dialog(self):
        self.hide()

    def show_dialog(self):
        self.show()