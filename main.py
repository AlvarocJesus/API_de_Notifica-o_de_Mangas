import logging
import pandas as pd
from time import sleep
from loguru import logger

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
  handlers=[
    logging.FileHandler('projetoManga.log'),
    logging.StreamHandler()
  ]
)

def add_manga():
  try:
    logging.info('Inicia processo de adicionar um manga')

    tipo = input('Indique se é um Anime, ou Manga, ou Filme: ') # 'Manga' ou 'Anime' ou 'Filme'
    nome = input(f'Digite o nome do {tipo}: ') # 'One Piece'
    cap_atual = int(input('Digite o episodio em que esta: ')) # 1000
    total_caps = int(input('Digite o total de episodios: ')) # 1000
    temp_atual = int(input('Digite a temporada em que esta: ')) # ''
    temp_total = int(input('Digite o total de temporadas: ')) # ''
    url = input('Digite a url onde esta acompanhando: ') # 'https://onepieceex.net/manga/one-piece-capitulo-1000/'
    status = input(f'Digite o status do {tipo}, como Em Andamento ou Finalizado: ') # 'Em andamento'

    line = f'{tipo};{nome};{cap_atual};{total_caps};{status};{temp_atual};{temp_total};{url}'

    insertFile(line)

    if tipo == 'Manga':
      print('Manga adicionado com sucesso!')
    else:
      print('Anime adicionado com sucesso!')
    
    logging.info('Finaliza processo de adicionar um manga')
  except Exception as e:
    logging.error(f'Erro na funcao add_manga: {e}')

def import_manga(fileName):
  try:
    logging.info('Inicia importacao de arquivo')

    df = pd.read_excel(fileName)
    df_fillna = df.fillna('')

    for row in df_fillna.values:
      line = ';'.join([str(cell) for cell in row])
      insertFile(line)

    print('Importacao realizada com sucesso!')
    logging.info(f'Finaliza importacao de arquivo: {fileName}')
  except Exception as e:
    print('Falha na importacao')
    logging.error(f'Falha na funcao import_manga: {e}')

def list_manga():
  try:
    logging.info('Inicio listagem de mangas')

    print('\nSua lista de mangas, animes e filmes!')
    file = open('mangas/mangas.csv', 'r')

    for line in file.readlines():
      print(line.strip().split(';')[1])

    file.close()
    logging.info('Finaliza listagem de mangas')
  except Exception as e:
    logging.error(f'Falha da funcao list_manga: {e}')

def update_manga():
  try:
    logging.info('Inicia atualizacao de manga')

    print('Atualizando manga!')
    
    sleep(3)

    print('Manga atualizado com sucesso!')
    
    logging.info('Finaliza atualizacao de manga')
  except Exception as e:
    logging.errpr(f'Falha na funcao update_manga: {e}')

def insertFile(line):
  try:
    file = open('../mangas/mangas.csv', 'a+')
    file.write(f'{line}\n')
    file.close()
    logging.info(f'Insercao no arquivo realizada com sucesso {line}')
  except Exception as e:
    print('Erro na insercao')
    print(f'Falha na funcao insertFile{e}')


try:
  print('Bem-vindo a sua lista de mangas, animes e filmes!')
  while True:
    option = input("""
  Escolha uma ação:
  1 - Adicionar
  2 - Importar Arquivo
  3 - Listar
  4 - Atualizar
  0 - Sair\n
  """)

    if option == '1':
      add_manga()
    elif option == '2':
      fileName = input('Coloque o caminho do arquivo que deseja importar: ')
      import_manga(fileName)
    elif option == '3':
      list_manga()
    elif option == '4':
      update_manga()
    elif option == '0':
      break

except Exception as e:
  logging.error(f'Erro no main: {e}')