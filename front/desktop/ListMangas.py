from tkinter import *
from tkinter import ttk
from db.database import Database

class ListMangas:
	def __init__(self):
		print('list mangas')

	"""
		Inicializa a tela para listar todos os mangas
	"""
	def listMangas(self, parent):
		root = Toplevel(parent)
		root.title('Listar Mangas')

		ttk.Label(root, text='Listar Mangas').pack()
		ttk.Button(root, text='Quit', command=self.getDBMangas).pack()

	def getDBMangas(self, userId):
		db = Database().getMyMangas(userId)
		print(db)
