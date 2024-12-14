import psycopg2
from config.log.log import Log

class Database:
	def __init__(self):
		print('Database')

	def addManga(self, manga):
		print('Add manga')
		print(f'Data Manga: {manga}')

		conn, cursor = self.getEngine()

		try:
			# with engine.connect() as conn:
			# 	print('Connection')
			cursor.execute('insert into manga (name, author, release_date) values (%s, %s, %s)')
			conn.commit()
			conn.close()

			Log().log('info', 'Manga added')
			return True
		except Exception as e:
			Log().log('error', e)

	def getManga(self):
		print('Get manga')
		conn, cursor = self.getEngine()
		# engine = self.getEngine()

		# with engine.connect() as conn:
		# 	print('Connection')

		try:
			# with engine.connect() as conn:
			# 	print('Connection')
			mangas = cursor.execute('select * from manga with(nolock)')
			conn.commit()
			conn.close()

			Log().log('info', 'Manga added')
			return mangas
		except Exception as e:
			Log().log('error', e)
	
	def getEngine(self):
		try:
			conn = psycopg2.connect('dbname=teste user=teste password=teste')
			cursor = conn.cursor()

			Log().log('info', 'Connection with database')
			return conn, cursor
		except Exception as e:
			Log().log('error', e)
		
