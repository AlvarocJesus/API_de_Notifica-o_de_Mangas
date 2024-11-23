from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Gerenciador de Mangas')
# root.geometry('500x500')
addManga = ttk.Frame(root, padding=10)
addManga.grid()

ttk.Label(addManga, text='Hello').grid(column=0, row=0)
ttk.Button(addManga, text='Quit', command=root.destroy).grid(column=1, row=0)

tipo = ''
ttk.Radiobutton(addManga, text='Manga', variable=tipo, value='Manga').grid(column=0, row=0)
ttk.Radiobutton(addManga, text='Anime', variable=tipo, value='Anime').grid(column=1, row=0)
ttk.Radiobutton(addManga, text='Filme', variable=tipo, value='Filme').grid(column=2, row=0)
# tipo = input('Indique se é um Anime, ou Manga, ou Filme: ') # 'Manga' ou 'Anime' ou 'Filme'

ttk.Label(addManga, text=f'Digite o nome do {tipo}:').grid(column=0, row=1)
nome = ttk.Entry(addManga).grid(column=1, row=1)
# nome = input(f'Digite o nome do {tipo}: ') # 'One Piece'

ttk.Label(addManga, text='Digite o episodio em que esta: ').grid(column=0, row=2)
nome = ttk.Entry(addManga).grid(column=1, row=2)
# cap_atual = int(input('Digite o episodio em que esta: ')) # 1000

ttk.Label(addManga, text='Digite o total de episodios: ').grid(column=0, row=3)
nome = ttk.Entry(addManga).grid(column=1, row=3)
# total_caps = int(input('Digite o total de episodios: ')) # 1000

ttk.Label(addManga, text='Digite a temporada em que esta: ').grid(column=0, row=4)
nome = ttk.Entry(addManga).grid(column=1, row=4)
# temp_atual = int(input('Digite a temporada em que esta: ')) # ''

ttk.Label(addManga, text='Digite o total de temporadas: ').grid(column=0, row=5)
nome = ttk.Entry(addManga).grid(column=1, row=5)
# temp_total = int(input('Digite o total de temporadas: ')) # ''

ttk.Label(addManga, text='Digite a url onde esta acompanhando:').grid(column=0, row=6)
nome = ttk.Entry(addManga).grid(column=1, row=6)
# url = input('Digite a url onde esta acompanhando: ') # 'https://onepieceex.net/manga/one-piece-capitulo-1000/'

ttk.Label(addManga, text=f'Digite o status do {tipo}, como Em Andamento ou Finalizado: ').grid(column=0, row=7)
nome = ttk.Entry(addManga).grid(column=1, row=7)
# status = input(f'Digite o status do {tipo}, como Em Andamento ou Finalizado: ') # 'Em andamento'

root.mainloop()