import sqlite3 as sq


# Подключение к существующей БД/создание новой БД
db = sq.connect('database/mail.db')
cur = db.cursor() 


# Функция создания необходимых таблиц
def create_db():
	
	cur.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    name     TEXT,
    surname  TEXT,
    father   TEXT,
    notes    TEXT)''')
	
	cur.execute('''CREATE TABLE IF NOT EXISTS mails (
    id       INTEGER  PRIMARY KEY AUTOINCREMENT,
    sender   TEXT     REFERENCES users (username),
    receiver TEXT     REFERENCES users (username),
    theme    TEXT,
    text     TEXT,
    time     DATETIME)''')
	
	db.commit()


# Функция проверки логина и пароля
def check_auth(username, password):
	
	# Из БД берутся логин и пароль с совпадающим username и передаются в переменную user_data
	user_data = cur.execute(f'SELECT username, password FROM users WHERE "username" = "{username}"').fetchone()
	
	# Если user_data содержит не None, то происходит сравнение с введенным пользователем логином и паролем
	if user_data != None:
		if user_data[0] == username and user_data[1] == password:
			return True
	else:
		return False
		
		
# Функция регистрации пользователя		
def register_user(username, password, name, surname, father, notes):
	
	try:
		cur.execute(f'INSERT INTO users(username, password, name, surname, notes) VALUES("{username}", "{password}", "{name}", "{surname}", "{notes}")')
		db.commit()
		
		return 'new'
		
	
	except sq.IntegrityError:
		cur.execute(f'UPDATE users SET "password" = "{password}" WHERE "username"="{username}"')
		db.commit()
		
		return 'existed'
		
		
# Функция получения данных о пользователе
def get_user_info(username):
	
	user_info = cur.execute(f'SELECT * FROM users WHERE "username" = "{username}"').fetchone()
	return user_info	


# Функция получения всех входящих писем
def get_income_mails(username):
	
	# Из общей БД писем берутся письма, получателем в которых указан username
	income_mails = cur.execute(f'SELECT sender, theme, text, time FROM mails WHERE "receiver" = "{username}"').fetchall()
	
	return income_mails
	

# Функция получения всех отправленных писем
def get_sent_mails(username):
	
	# Из общей БД писем берутся письма, получателем в которых указан username
	sent_mails = cur.execute(f'SELECT receiver, theme, text, time FROM mails WHERE "sender" = "{username}"').fetchall()
	
	return sent_mails
	
	
def send_mail(username, address, theme, text, time):
	
	cur.execute(f'INSERT INTO mails(sender, receiver, theme, text, time) VALUES("{username}", "{address}", "{theme}", "{text}", "{time}")')
	db.commit()
	
	return True
	
		
		
		
if __name__ == '__main__':
	create_db()