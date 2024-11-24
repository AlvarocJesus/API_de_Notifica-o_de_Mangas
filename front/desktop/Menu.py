from tkinter import Menu

class MyMenu:
	def __init__(self):
		print('Menu criado')

	"""
	Inicializa o menu e configura na janela principal.

	:param root: A janela principal (root ou Toplevel).
	:param open_add_manga_callback: Função para abrir a tela de "Adicionar Mangá".
	"""
	def createMenu(self, root, openPageAddManga):
		# criando barra de menu
		menu = Menu(root)

		# para adicionar um novo manga
		filemenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='File', menu=filemenu)
		filemenu.add_command(label='New', command=openPageAddManga)
		filemenu.add_command(label='Open')
		filemenu.add_separator()
		filemenu.add_command(label='Exit', command=root.quit)

		helpMenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='Help', menu=helpMenu)
		helpMenu.add_command(label='About')

		# display menu
		root.config(menu=menu)