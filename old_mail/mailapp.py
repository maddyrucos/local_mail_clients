import os
import sys

from PyQt5 import QtWidgets

import dialog
import login
import mail
import reg


class Login(QtWidgets.QMainWindow, login.Ui_LoginWindow):
		
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.enterBtn.clicked.connect(self.auth)
		self.regBtn.clicked.connect(self.open_registration)
		
	def auth(self):
		username = self.usernameText.text()
		password = self.passwordText.text()
		check = username+';'+password+'\n'
		f = open('users.txt', 'r')
		users = f.readlines()	
		for i in range(len(users)):		
			if check == users[i]:
				self.mail = Mail()
				self.hide()
				self.mail.init(username)
				self.mail.show()
			else:
				pass
		f.close()
		
	def open_registration(self):
		self.reg = Registration()
		self.hide()
		self.reg.show()
	



	

class Mail(QtWidgets.QMainWindow, mail.Ui_mailWindow):	

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.sendBtn.clicked.connect(self.send_letter)
		self.nextBtn.clicked.connect(self.next_letter)
		self.backBtn.clicked.connect(self.prev_letter)
		self.deleteBtn.clicked.connect(self.delete_letter)
		
	def init(self, user):
		self.username = user
		self.welcomeLbl.setText('Приветствую, '+self.username+'!')
		mails = os.listdir(self.username)
		self.i = len(mails)		
		f = open('/home/igor/python/mail/'+self.username+'/'+mails[self.i-1], 'r')
		main_mail = f.read()
		self.mailText.setText(main_mail)
		
		
	def send_letter(self):
		address = self.addressText.text()
		text = self.letterText.toPlainText()
		mail = self.username+'\n'+text
		mails = os.listdir(address)
		self.dialog = Dialog()
		os.system('echo "'+mail+'" >> ~/python/mail/'+address+'/'+str(len(mails))+'_'+self.username)
		self.dialog.show()
		
		
	def prev_letter(self):
		mails = os.listdir(self.username)		
		if self.i<len(mails)-2:
			self.i+=1
		f = open('/home/igor/python/mail/'+self.username+'/'+mails[self.i], 'r')
		main_mail = f.read()
		self.mailText.setText(main_mail)
		

	def next_letter(self):
		mails = os.listdir(self.username)			
		if self.i>0:
			self.i-=1
		f = open('/home/igor/python/mail/'+self.username+'/'+mails[self.i], 'r')
		main_mail = f.read()
		self.mailText.setText(main_mail)
		
	def delete_letter(self):
		mails = os.listdir(self.username)					
		os.system('rm '+self.username+'/'+mails[self.i])
		self.i-=1
		f = open('/home/igor/python/mail/'+self.username+'/'+mails[self.i], 'r')
		main_mail = f.read()
		self.mailText.setText(main_mail)
		
		



class Registration(QtWidgets.QMainWindow, reg.Ui_regWindow):
	
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.regBtn.clicked.connect(self.registration)
		
	def registration(self):
		username = self.usernameText.text()
		password = self.passwordText.text()
		name = self.nameText.text()
		lastname = self.lastnameText.text()	
		#notes = self.notesText.PlainText()
		os.system('mkdir ' + username)
		os.system('cd '+username+' && echo "'+username+'\n'+password+'\n'+name+'\n'+lastname+'" >> data.txt')
		os.system('echo "'+username+';'+password+'" >> users.txt')
		os.system('cd '+username+' && echo "Добро пожаловать в наш почтовый клиент!" >> 0_0')
		self.login = Login()
		self.hide()
		self.login.show()



class Dialog(QtWidgets.QMainWindow, dialog.Ui_Dialog):	

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
	def accept(self):
		self.hide()
	
	def reject(self):
		pass



def main():
	app = QtWidgets.QApplication(sys.argv)
	login = Login()
	login.show()

	
	app.exec()
	
if __name__ == '__main__':
	main()