import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from dotenv import load_dotenv
import datetime

# from config.log.log import Log

load_dotenv()

# connect_args={"check_same_thread": False} é uma configuração necessária só para o SQLite 
# não dar erro quando usado em APIs (como FastAPI ou Flask)
engine = create_engine(os.getenv('SQLALCHEMY_DATABASE_URL'), connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Site(Base):
	__tablename__ = 'sites'
	
	id = Column(Integer, primary_key=True, index=True)
	nome = Column(String, nullable=False)
	url_base = Column(String, nullable=False)
	slug_script = Column(String, nullable=False)
	ativo = Column(Boolean, default=True)

	# Relacao: Um site hospeda varios mangas
	mangas = relationship('Manga', back_populates='site')
	
class Manga(Base):
	__tablename__ = 'mangas'
	
	id = Column(Integer, primary_key=True, index=True)
	nome = Column(String, nullable=False)
	url_origem = Column(String, nullable=False)
	ultimo_capitulo_lancado = Column(Float, default=0)
	total_cap = Column(Float, default=0)
	data_ultima_verificacao = Column(DateTime, default=datetime.datetime.utcnow)
	site_id = Column(Integer, ForeignKey('sites.id'))

	site = relationship('Sites', back_populates='mangas')
	leitores = relationship('UsuarioManga', back_populates='mangas')

class User(Base):
	__tablename__ = 'users'
	
	id = Column(Integer, primary_key=True, index=True)
	nome = Column(String, nullable=False)
	telegram_chat_id = Column(String, nullable=True)

	# Relacao: Um site hospeda varios mangas
	mangas_acompanhados = relationship('UserManga', back_populates='user')

class UserManga(Base):
	__tablename__ = 'users_mangas'
	
	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	manga_id = Column(Integer, ForeignKey('mangas.id'))
	capitulo_atual_usuario = Column(Float, default=0)

	# Relacao: Um site hospeda varios mangas
	user = relationship('User', back_populates='mangas_acompanhados')
	manga = relationship('Manga', back_populates='leitores')

def create_database():
	# Esse comando olha para todas as classes que herdam de 'Base' 
	# e cria as tabelas no SQLite se elas ainda não existirem.

	Base.metadata.create_all(bind=engine)
	print('Database created successfully!')

if __name__ == "__main__":
	create_database()