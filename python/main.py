from time import sleep

def add_manga():
  file = open('../mangas/mangas.csv', 'a+')

  tipo = input('Indique se é um Anime, ou Manga, ou Filme: ') # 'Manga' ou 'Anime' ou 'Filme'
  nome = input(f'Digite o nome do {tipo}: ') # 'One Piece'
  cap_atual = int(input('Digite o episodio em que esta: ')) # 1000
  total_caps = int(input('Digite o total de episodios: ')) # 1000
  temp_atual = int(input('Digite a temporada em que esta: ')) # ''
  temp_total = int(input('Digite o total de temporadas: ')) # ''
  url = input('Digite a url onde esta acompanhando: ') # 'https://onepieceex.net/manga/one-piece-capitulo-1000/'
  status = input(f'Digite o status do {tipo}, como Em Andamento ou Finalizado: ') # 'Em andamento'

  file.write(f'{tipo};{nome};{cap_atual};{total_caps};{status};{temp_atual};{temp_total};{url}\n')

  file.close()

  if tipo == 'Manga':
    print('Manga adicionado com sucesso!')
  else:
    print('Anime adicionado com sucesso!')

def list_manga():
  print('\nSua lista de mangas, animes e filmes!')
  file = open('../mangas/mangas.csv', 'r')

  for line in file.readlines():
    print(line.strip().split(';')[1])

  file.close()

def update_manga():
  print('Atualizando manga!')
  
  sleep(3)

  print('Manga atualizado com sucesso!')

print('Bem-vindo a sua lista de mangas, animes e filmes!')
while True:
  option = input("""
Escolha uma ação:
1 - Adicionar
2 - Listar
3 - Atualizar
4 - Sair\n
""")

  if option == '1':
    add_manga()
  elif option == '2':
    list_manga()
  elif option == '3':
    update_manga()
  elif option == '4':
    break
