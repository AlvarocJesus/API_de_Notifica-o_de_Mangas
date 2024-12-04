from tkinter import *
from tkinter import ttk

class AddManga:
	def __init__(self):
		pass

	def addManga(self, parent):
		root = Toplevel(parent)
		root.title('Adicionar Manga')

		ttk.Label(root, text='Hello').pack() #.grid(column=0, row=0)
		ttk.Button(root, text='Quit', command=root.destroy).pack() #.grid(column=1, row=0)

		tipo = StringVar()
		ttk.Radiobutton(root, text='Manga', variable=tipo, value='Manga', command=self.alterTextTipo).pack() #.grid(column=0, row=0)
		ttk.Radiobutton(root, text='Anime', variable=tipo, value='Anime', command=self.alterTextTipo).pack() #.grid(column=1, row=0)
		ttk.Radiobutton(root, text='Filme', variable=tipo, value='Filme', command=self.alterTextTipo).pack() #.grid(column=2, row=0)

		nomeLabel = ttk.Label(root, text=f'Digite o nome do {tipo}:').pack() #.grid(column=0, row=1)
		nameEntry = ttk.Entry(root)
		nameEntry.pack() #.grid(column=1, row=1)
		name = nameEntry.get()

		ttk.Label(root, text='Digite o episodio em que esta: ').pack() #.grid(column=0, row=2)
		nome = ttk.Entry(root).pack() #.grid(column=1, row=2)

		ttk.Label(root, text='Digite o total de episodios: ').pack() #.grid(column=0, row=3)
		nome = ttk.Entry(root).pack() #.grid(column=1, row=3)

		ttk.Label(root, text='Digite a temporada em que esta: ').pack() #.grid(column=0, row=4)
		nome = ttk.Entry(root).pack() #.grid(column=1, row=4)

		ttk.Label(root, text='Digite o total de temporadas: ').pack() #.grid(column=0, row=5)
		nome = ttk.Entry(root).pack() #.grid(column=1, row=5)

		ttk.Label(root, text='Digite a url onde esta acompanhando:').pack() #.grid(column=0, row=6)
		nome = ttk.Entry(root).pack() #.grid(column=1, row=6)

		ttk.Label(root, text=f'Marque o status do {tipo}')
		status_manga = StringVar()
		ttk.Radiobutton(root, text='Em Andamento', variable=status_manga, value='Em Andamento').pack() #.grid(column=0, row=7)
		ttk.Radiobutton(root, text='Finalizado', variable=status_manga, value='Finalizado').pack() #.grid(column=1, row=7)

		ttk.Button(root, text='Adicionar', command=root.destroy).pack() #.grid(column=1, row=8)
	
	def alterTextTipo(self):
		print(self.tipo.get())
		if self.tipo.get() == 'Manga':
			self.nomeLabel.config(text='Digite o nome do Manga:')
		elif self.tipo.get() == 'Anime':
			self.nomeLabel.config(text='Digite o nome do Anime:')
		elif self.tipo.get() == 'Filme':
			self.nomeLabel.config(text='Digite o nome do Filme:')
		else:
			self.nomeLabel.config(text='Digite o nome do:')
		print(self.nomeLabel)
		print(self.nomeLabel.cget('text'))
