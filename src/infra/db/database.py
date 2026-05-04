import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import psycopg2
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

from config.log.log import Log

load_dotenv()

class Database:
	logger = None
	
	def __init__(self):
		print('Database')
		self.logger = Log().initLog('database.log')

	def addManga(self, manga):
		print(f'addManga: {manga}')
		print(f'nome manga: {manga["nome"]}')
		engine = self.getEngine()

		try:
			with engine.connect() as conn:
				teste = conn.execute(
					text("""insert into mangas (name, total_caps, temporadas, tipo) values (:name, :total_caps, :temporadas, :tipo) returning id_manga"""),
					{'name': manga['nome'], 'total_caps': manga['total_episodios'], 'temporadas': manga['total_temporadas'], 'tipo': manga['tipo']}
				)

				conn.commit()
				insertedId = teste.scalar()
				conn.close()

			print(f'Teste: {insertedId}')

			Log().log(self.logger, 'info', f'Manga added with id {insertedId}')
			return insertedId
		except Exception as e:
			Log().log(self.logger, 'error', e)
	
	def addUrlManga(self, urlManga):
		print(f'addManga: {urlManga}')
		engine = self.getEngine()

		try:
			with engine.connect() as conn:
				teste = conn.execute(
					text("""insert into sites (url, "mangaId", ativo) values (:url, :id_manga, :status) returning id_site"""),
					{'url': urlManga['url'], 'id_manga': urlManga['id_manga'], 'status': urlManga['status']}
				)
				conn.commit()
				insertedId = teste.scalar()
				conn.close()

				print(f'Teste: {insertedId}')

			Log().log(self.logger, 'info', f'Url manga added with id {insertedId}')
			return insertedId
		except Exception as e:
			Log().log(self.logger, 'error', e)

	def addUserManga(self, userManga):
		print(f'addManga: {userManga}')
		engine = self.getEngine()

		try:
			with engine.connect() as conn:
				teste = conn.execute(
					text("""insert into manga_user ("mangaId", atual_cap, atual_temporada, "userId") values (:id_manga, :episodio_atual, :temporada_atual, :id_user) returning id"""),
					{'id_manga': userManga['id_manga'], 'episodio_atual': userManga['episodio_atual'], 'temporada_atual': userManga['temporada_atual'], 'id_user': userManga['id_user']}
				)
				conn.commit()
				insertedId = teste.scalar()
				conn.close()

				print(f'Teste: {insertedId}')

			Log().log(self.logger, 'info', f'User manga added with id {insertedId}')
			return insertedId
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
			# conn = psycopg2.connect('dbname=postegre_notify_manga user=postegre_notify_manga_user password=8UesZFjtUpAtLGhcn7JZO8GrJlV0VZtN')
			# cursor = conn.cursor()

			engine = create_engine(os.getenv('DATABASE_URL'))

			Log().log(self.logger, 'info', 'Connection with database')
			# return conn, cursor
			return engine
		except Exception as e:
			Log().log(self.logger, 'error', e)
		
	def updataManga(self, manga):
		try:
			engine = self.getEngine()

			with engine.connect() as conn:
				updated = conn.execute(
					text("""update manga set total_caps = :total_caps where name = :titulo"""),
					{'total_caps': manga['total_caps'], 'titulo': manga['id_manga']}
				)
				conn.commit()
				conn.close()
			
			Log().log(self.logger, 'info', 'Manga updated')
			return updated
		except Exception as e:
			Log().log(self.logger, 'error', e)
