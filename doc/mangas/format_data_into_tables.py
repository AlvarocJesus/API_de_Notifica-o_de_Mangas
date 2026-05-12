from urllib.parse import urlsplit, urlunsplit
import pandas as pd
import re
from datetime import datetime
import sys
import os

# Adicionar caminho para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.infra.db.create_database import SessionLocal, Site, Manga, User, UserManga, create_database
from src.config.log.log import Log

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_excel('doc/mangas/lista_completa_manga.ods', engine='odf')

sites = []
mangas = []
users = [{
	'id': 1,
	'nome': 'Alvaro Coelho Jesus',
	'telegram_chat_id': 0,
}]
userMangas = []

def clean_dafault(url):
	partes = urlsplit(url)
	path = partes.path.rstrip('/')
	
	# remove sufixos de capítulo comuns (capitulo, chapter, ep, page, /\d+ no final)
	path = re.sub(r'/(capitulo|capítulo|chapter|chap|ep|episodio|episode|page|cap|online)[^/]*$','', path, flags=re.I)
	path = re.sub(r'/\d+/?$','', path)  # remove ids numéricos finais
	# às vezes existe "/online/12345" -> pode remover segmento 'online' e id
	path = re.sub(r'/online/\d+/?$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

# Outro handler para sites que têm '/<manga>/online/<id>/capitulo/<n>'
def clean_mangalivre_net(url):
	partes = urlsplit(url)
	path = partes.path.rstrip('/')
	
	# tenta manter até o slug do mangá (remover /online/<id>/...)
	path = re.sub(r'/online/\d+.*$','', path, flags=re.I)
	# path = re.sub(r'/capitulo/.*$','', path, flags=re.I)
	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def clean_mangalivre_blog(url):
	partes = urlsplit(url)
	path = partes.path.rstrip('/')
	
	# tenta manter até o slug do mangá (remover /capitulo/<slug>-capitulo-<id>)
	path = re.sub(r'-capitulo-.*$','', path, flags=re.I)
	# https://mangalivre.blog/capitulo/the-beginning-after-the-end-capitulo-228

	# path = re.sub(r'/capitulo/.*$','', path, flags=re.I)
	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

# Exemplo de handler específico (site que usa '/manga/<slug>/capitulo-<n>')
def clean_oldi_sussytoons_site(url):
	partes = urlsplit(url)
	path = partes.path.rstrip('/')
	# se a estrutura for /manga/<slug>/capitulo-<n>/ -> keep /manga/<slug>
	m = re.match(r'^(/manga/[^/]+)', path, flags=re.I)
	if m:
		base_path = m.group(1)
	else:
		base_path = path
	return urlunsplit((partes.scheme or 'https', partes.netloc, base_path, '', ''))

def clean_neoxscan(url):
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /manga/<slug>/cap-<n>
	# path = re.sub(r'/cap-\d+/?$','', path, flags=re.I)
	path = re.sub(r'/cap-.*$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def clean_mangaschan(url):
	# handler do mangaschan.net - estrutura /<id>/<slug>-capitulo-<n>
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /<id>/<slug>-capitulo-<n>
	# path = re.sub(r'-cap[ií]tulo-.*$','', path, flags=re.I)
	path = re.sub(r'-capitulo-.*$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def clean_tsuki_mangas(url):
	# handler do tsuki-mangas.com - estrutura /leitor/<id>/<id>/<slug>/<n>
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /leitor/<id>/<id>/<slug>/<n>
	# path = re.sub(r'/\d+$','', path, flags=re.I)
	path = re.sub(r'/[\d\.\-]+/?$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def clean_oldi_sussytoons_com(url):
	# handler do tsuki-mangas.com - estrutura /<slug>/capitulo-<n>
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /<slug>/capitulo-<n>
	path = re.sub(r'/capitulo-\d+$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def clean_mangaonline_biz(url):
	# handler do tsuki-mangas.com - estrutura /leitor/<id>/<id>/<slug>/<n>
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /leitor/<id>/<id>/<slug>/<n>
	path = re.sub(r'-capitulo-.*+$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

def classico(url):
	# handler do tsuki-mangas.com - estrutura /leitor/<id>/<id>/<slug>/<n>
	partes = urlsplit(url)
	path = partes.path.rstrip('/')

	# limpa url - estrutura /leitor/<id>/<id>/<slug>/<n>
	path = re.sub(r'/(capitulo|cap)-.*$','', path, flags=re.I)

	return urlunsplit((partes.scheme or 'https', partes.netloc, path, '', ''))

HANDLERS = {
	'mangalivre.net': clean_mangalivre_net,
	'mangaschan.net': clean_mangaschan,
	'tsuki-mangas.com': clean_tsuki_mangas,
	'neoxscan.net': clean_neoxscan,
	'mangaonline.biz': clean_mangaonline_biz,
	'mangalivre.blog': clean_mangalivre_blog,
}

def get_base_url(url):
	if not url or url.lower() in ('nan', 'none', 'anime'):
		return url	# Retorna a URL original se for vazia ou inválida
	
	partes = urlsplit(url)
	netloc = partes.netloc.lower()

	# tenta encontrar handler pelo netloc
	if netloc in HANDLERS:
		# print(f'Usando handler específico para "{netloc}"')
		return HANDLERS[netloc](url)
	
	# tenta match pelo sufixo (ex. subdominio)
	for domain, handler in HANDLERS.items():
		# print(f'Checando se "{domain}" está em "{netloc}"')
		if domain in netloc:
			return handler(url)
	
	return clean_dafault(url)  # fallback genérico

for index, row in df.iterrows():
	link = str(df['Link'][index].strip())
	manga_id = index + 1
	site_id = index + 1

	sites.append({
		'id': site_id,
		'nome': df['Nome'][index].split(' - ')[0] if ' - ' in df['Nome'][index] else df['Nome'][index],
		'url_base': get_base_url(link),
		'slug_script': link.split('/')[2] if 'Anime' not in link else link,
		'ativo': 1,  # Adicione isto
	})
	mangas.append({
		'id': manga_id,
		'nome': df['Nome'][index],
		'url_origem': link,
		'ultimo_capitulo_lancado': 0,
		'total_cap': 0,
		# 'data_ultima_verificacao': datetime.now(datetime.UTC).isoformat(),
		'data_ultima_verificacao': datetime.now().isoformat(),
		'site_id': site_id,
	})
	userMangas.append({
		'id': index + 1,
		'user_id': 1,
		'manga_id': manga_id,
		'capitulo_atual_usuario': 0,
	})

df_sites = pd.DataFrame(sites)
df_mangas = pd.DataFrame(mangas)
df_userMangas = pd.DataFrame(userMangas)
df_users = pd.DataFrame(users)

def inserir_dados_no_banco():
	"""Insere dados do Excel diretamente no banco usando ORM"""
	
	logger = Log().initLog('format_data.log')
	db = SessionLocal()
	
	try:
		# 1. Criar tabelas se não existirem
		create_database()
		print("✅ Tabelas criadas")
			
		# 2. Inserir usuário padrão
		user = db.query(User).filter(User.id == 1).first()
		if not user:
			user = User(
				id=1,
				nome='Alvaro Coelho Jesus',
				telegram_chat_id=0
			)
			db.add(user)
			db.commit()
			print(f"✅ Usuário inserido: {user.nome}")
			
		# 3. Dicionário para mapear url_base -> site_id (para evitar duplicatas)
		sites_map = {}
		site_counter = 1
			
		# 4. Processar linhas do Excel
		for index, row in df.iterrows():
			link = str(df['Link'][index].strip())
			nome_manga = df['Nome'][index]
				
			# Obter base URL
			url_base = get_base_url(link)
				
			# Verificar se site já existe (por url_base)
			if url_base not in sites_map:
				site_name = nome_manga.split(' - ')[0] if ' - ' in nome_manga else nome_manga
				
				# Tentar encontrar site no banco
				existing_site = db.query(Site).filter(
					Site.url_base == url_base
				).first()
				
				if existing_site:
					sites_map[url_base] = existing_site.id
					print(f"  ℹ️  Site existente: {existing_site.nome}")
				else:
					# Criar novo site
					new_site = Site(
						nome=site_name,
						url_base=url_base,
						slug_script=link.split('/')[2] if 'Anime' not in link else link,
						ativo=False
					)
					db.add(new_site)
					db.flush()  # Obter ID do novo site
					sites_map[url_base] = new_site.id
					print(f"  ✅ Site criado: {new_site.nome}")
			
			site_id = sites_map[url_base]
				
			# 5. Inserir manga (verificar se já existe por url_origem)
			existing_manga = db.query(Manga).filter(
				Manga.url_origem == link
			).first()
				
			if not existing_manga:
				manga = Manga(
					nome=nome_manga,
					url_origem=link,
					ultimo_capitulo_lancado=0,
					total_cap=0,
					data_ultima_verificacao=datetime.now(),
					site_id=site_id
				)
				db.add(manga)
				db.flush()
				print(f"  ✅ Mangá inserido: {manga.nome}")
				
				# 6. Inserir relação usuário-mangá
				user_manga = UserManga(
					user_id=1,
					manga_id=manga.id,
					capitulo_atual_usuario=0
				)
				db.add(user_manga)
			else:
				print(f"  ⚠️  Mangá já existe: {existing_manga.nome}")
			
		# Commit final
		db.commit()
			
		# 7. Exibir relatório
		print("\n📊 RELATÓRIO FINAL:")
		print(f"  • Usuários: {db.query(User).count()}")
		print(f"  • Sites: {db.query(Site).count()}")
		print(f"  • Mangás: {db.query(Manga).count()}")
		print(f"  • Relacionamentos: {db.query(UserManga).count()}")
		
		Log().log(logger, 'info', 'Dados inseridos com sucesso')
			
	except Exception as e:
		db.rollback()
		Log().log(logger, 'error', str(e))
		print(f"❌ Erro: {e}")
	finally:
		db.close()

if __name__ == "__main__":
	inserir_dados_no_banco()