from time import sleep

def add_manga():
  file = open('mangas/mangas.csv', 'a+')

  tipo = 'Manga'
  nome_manga = 'One Piece'
  cap_atual = 1000
  total_caps = 1000
  status = 'Em andamento'
  temp_atual = ''
  temp_total = ''
  url = 'https://onepieceex.net/manga/one-piece-capitulo-1000/'

  file.write(f'{tipo};{nome_manga};{cap_atual};{total_caps};{status};{temp_atual};{temp_total};{url}\n')

  file.close()

  if tipo == 'Manga':
    print('Manga adicionado com sucesso!')
  else:
    print('Anime adicionado com sucesso!')

def list_manga():
  file = open('mangas/mangas.csv', 'r')

  for line in file.readlines():
    print(line)

  file.close()

def update_manga():
  print('Atualizando manga!')
  
  sleep(3)

  print('Manga atualizado com sucesso!')

while True:
  print('Bem-vindo a sua lista de mangas e animes!')
  option = input("""
  Escolha uma ação:
  1 - Adicionar manga
  2 - Listar mangas
  3 - Atualizar manga
  4 - Sair
  """)

  if option == '1':
    add_manga()
  elif option == '2':
    list_manga()
  elif option == '3':
    update_manga()
  elif option == '4':
    break
