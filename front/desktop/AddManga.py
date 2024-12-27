import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tkinter import *
from tkinter import ttk
from db.database import Database

class AddManga:
	name = None
	tipo = None
	nomeLabel = None
	cap_atual = None
	cap_total = None
	temp_atual = None
	temp_total = None
	url = None
	status_manga = None

	def __init__(self):
		self.name = StringVar()
		self.tipo = StringVar()
		self.nomeLabel = StringVar()
		self.cap_atual = StringVar()
		self.cap_total = StringVar()
		self.temp_atual = StringVar()
		self.temp_total = StringVar()
		self.url = StringVar()
		self.status_manga = StringVar()

	def addManga(self, parent):
		root = Toplevel(parent)
		root.title('Adicionar Manga')

		ttk.Label(root, text='Hello').pack() #.grid(column=0, row=0)
		ttk.Button(root, text='Quit', command=root.destroy).pack() #.grid(column=1, row=0)

		ttk.Radiobutton(root, text='Manga', variable=self.tipo, value='Manga', command=self.alterTextTipo).pack() #.grid(column=0, row=0)
		ttk.Radiobutton(root, text='Anime', variable=self.tipo, value='Anime', command=self.alterTextTipo).pack() #.grid(column=1, row=0)
		ttk.Radiobutton(root, text='Filme', variable=self.tipo, value='Filme', command=self.alterTextTipo).pack() #.grid(column=2, row=0)

		ttk.Label(root, text=f'Digite o nome do {self.tipo}:').pack() #.grid(column=0, row=1)
		ttk.Entry(root, textvariable=self.name).pack() #.grid(column=1, row=1)

		ttk.Label(root, text='Digite o episodio em que esta: ').pack() #.grid(column=0, row=2)
		ttk.Entry(root, textvariable=self.cap_atual).pack() #.grid(column=1, row=2)

		ttk.Label(root, text='Digite o total de episodios: ').pack() #.grid(column=0, row=3)
		ttk.Entry(root, textvariable=self.cap_total).pack() #.grid(column=1, row=3)

		ttk.Label(root, text='Digite a temporada em que esta: ').pack() #.grid(column=0, row=4)
		ttk.Entry(root, textvariable=self.temp_atual).pack() #.grid(column=1, row=4)

		ttk.Label(root, text='Digite o total de temporadas: ').pack() #.grid(column=0, row=5)
		ttk.Entry(root, textvariable=self.temp_total).pack() #.grid(column=1, row=5)

		ttk.Label(root, text='Digite a url onde esta acompanhando:').pack() #.grid(column=0, row=6)
		ttk.Entry(root, textvariable=self.url).pack() #.grid(column=1, row=6)

		ttk.Label(root, text=f'Marque o status do {self.tipo.get()}').pack() #.grid(column=0, row=7)
		ttk.Radiobutton(root, text='Em Andamento', variable=self.status_manga, value='Em Andamento').pack() #.grid(column=0, row=7)
		ttk.Radiobutton(root, text='Finalizado', variable=self.status_manga, value='Finalizado').pack() #.grid(column=1, row=7)

		ttk.Button(root, text='Adicionar', command=self.saveManga).pack() #.grid(column=1, row=8)
	
	def alterTextTipo(self):
		print(self.tipo)
		if self.tipo == 'Manga':
			self.nomeLabel.config(text='Digite o nome do Manga:')
		elif self.tipo == 'Anime':
			self.nomeLabel.config(text='Digite o nome do Anime:')
		elif self.tipo == 'Filme':
			self.nomeLabel.config(text='Digite o nome do Filme:')
		# print(self.nomeLabel)
		# print(self.nomeLabel.cget('text'))
	
	def saveManga(self):
		print('salvou')

		print(self.name)

		mangaBody = {
			'tipo': self.tipo.get(),
			'nome': self.name.get(),
			'total_episodios': int(self.cap_total.get()),
			'total_temporadas': int(self.temp_total.get()),
			'tipo': 11
		}
		id_manga = Database().addManga(mangaBody)

		print(f'id_manga: {id_manga}')

		urlBody = {
			'url': self.url.get(),
			'id_manga': id_manga,
			'status': True
		}
		Database().addUrlManga(urlBody)

		userMangaBody = {
			'id_manga': id_manga,
			'episodio_atual': int(self.cap_atual.get()),
			'temporada_atual': int(self.temp_atual.get()),
			'id_user': 1
		}
		userManga = Database().addUserManga(userMangaBody)
		print(userManga)
