from tkinter import Menu

class MyMenu:
	def __init__(self):
		print('Menu criado')

	"""
	Inicializa o menu e configura na janela principal.

	:param root: A janela principal (root ou Toplevel).
	:param open_add_manga_callback: Função para abrir a tela de "Adicionar Mangá".
	"""
	def createMenu(self, root, openPages):
		# criando barra de menu
		menu = Menu(root)

		# para adicionar um novo manga
		filemenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='File', menu=filemenu)
		filemenu.add_command(label='Add Manga', command=openPages[0])
		filemenu.add_command(label='Get Manga', command=openPages[1])
		filemenu.add_command(label='Open')
		filemenu.add_separator()
		filemenu.add_command(label='Exit', command=root.quit)

		helpMenu = Menu(menu, tearoff=0)
		menu.add_cascade(label='Help', menu=helpMenu)
		helpMenu.add_command(label='About')

		# display menu
		root.config(menu=menu)