import os
import pandas as pd
from time import sleep
import logging
from loguru import logger

# mangaFile = os.path.dirname(__file__)

def add_manga():
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

def import_manga(fileName):
  try:
    # print('Manga File')
    # print(mangaFile)
    df = pd.read_excel(fileName)
    print('Importacao realizada com sucesso!')

    print('\n\nDf inicial\n\n')
    print(df.head(5))

    print('\n\nDf substituindo NaN por vazio\n\n')
    df_fillna = df.fillna('')
    print(df_fillna.head(5))

    print('\n\nInserindo dados\n\n')
    for row in df_fillna.values:
      line = ';'.join([str(cell) for cell in row])
      print(line)
      insertFile(line)
  except Exception as e:
    print('Falha na importacao')
    print(e)

def list_manga():
  print('\nSua lista de mangas, animes e filmes!')
  file = open('mangas/mangas.csv', 'r')

  for line in file.readlines():
    print(line.strip().split(';')[1])

  file.close()

def update_manga():
  print('Atualizando manga!')
  
  sleep(3)

  print('Manga atualizado com sucesso!')

def insertFile(line):
  try:
    # file = open('mangas/mangas.csv', 'a+')
    file = open('../mangas/mangas.csv', 'a+')
    file.write(f'{line}\n')
    # file.write(f'{line}')
    file.close()
  except Exception as e:
    print('Erro na insercao')
    print(e)

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
