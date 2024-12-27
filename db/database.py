import psycopg2
from config.log.log import Log

class Database:
	logger = None
	
	def __init__(self):
		print('Database')
		self.logger = Log().initLog('database.log')

	def addManga(self, manga):
		print(f'addManga: {manga}')
		conn, cursor = self.getEngine()
		print(f'Connection: {conn}')
		print(f'Cursor: {cursor}')

		try:
			teste = cursor.execute('insert into manga (name, total_caps, temporadas, tipo) values (%s, %s, %s, 11)', (manga['nome'], manga['total_episodios'], manga['total_temporadas'], manga['tipo']))
			teste = 'teste'
			conn.commit()
			conn.close()

			print(f'Teste: {teste}')

			Log().log(self.logger, 'info', 'Manga added')
			return True
		except Exception as e:
			Log().log(self.logger, 'error', e)
	
	def addUrlManga(self, urlManga):
		print(f'addManga: {urlManga}')
		conn, cursor = self.getEngine()
		print(f'Connection: {conn}')
		print(f'Cursor: {cursor}')

		try:
			teste = cursor.execute('insert into manga (url, id_manga, status) values (%s, %s, %s)', (urlManga['url'], urlManga['id_manga'], urlManga['status']))
			teste = 'teste'
			conn.commit()
			conn.close()

			print(f'Teste: {teste}')

			Log().log(self.logger, 'info', 'Manga added')
			return True
		except Exception as e:
			Log().log(self.logger, 'error', e)

	def addUserManga(self, userManga):
		print(f'addManga: {userManga}')
		conn, cursor = self.getEngine()
		print(f'Connection: {conn}')
		print(f'Cursor: {cursor}')

		try:
			teste = cursor.execute('insert into manga (id_manga, episodio_atual, temporada_atual, id_user) values (%s, %s, %s, %s)', (userManga['id_manga'], userManga['episodio_atual'], userManga['temporada_atual'], userManga['id_user']))
			teste = 'teste'
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
			conn = psycopg2.connect('dbname=postegre_notify_manga user=postegre_notify_manga_user password=8UesZFjtUpAtLGhcn7JZO8GrJlV0VZtN')
			cursor = conn.cursor()

			Log().log(self.logger, 'info', 'Connection with database')
			return conn, cursor
		except Exception as e:
			Log().log(self.logger, 'error', e)
		
