import psycopg2
from config.log.log import Log

class Database:
	logger = None
	
	def __init__(self):
		print('Database')
		self.logger = Log().initLog('database.log')

	def addManga(self, manga):
		print(f'Data Manga: {manga}')
		conn, cursor = self.getEngine()

		try:
			teste = cursor.execute('insert into manga (name, author, release_date) values (%s, %s, %s)')
			conn.commit()
			conn.close()

			print(f'Teste: {teste}')

			Log().log(self.logger, 'info', 'Manga added')
			return True
		except Exception as e:
			Log().log(self.logger, 'error', e)

	def getAllManga(self):
		print('Get manga')
		conn, cursor = self.getEngine()

		try:
			mangas = cursor.execute('select * from manga with(nolock)')
			conn.commit()
			conn.close()

			Log().log(self.logger, 'info', 'Manga added')
			return mangas
		except Exception as e:
			Log().log(self.logger, 'error', e)
	
	def getMyMangas(self, userId):
		try:
			conn, cursor = self.getEngine()
			mangas = cursor.execute('select * from user_manga where user_id')
			conn.commit()
			conn.close()

			return mangas
		except Exception as e:
			Log().log(self.logger, 'error', e)

	def getEngine(self):
		try:
			conn = psycopg2.connect('dbname=teste user=teste password=teste')
			cursor = conn.cursor()

			Log().log(self.logger, 'info', 'Connection with database')
			return conn, cursor
		except Exception as e:
			Log().log(self.logger, 'error', e)
		
