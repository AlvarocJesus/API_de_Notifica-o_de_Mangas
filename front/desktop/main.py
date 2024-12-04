import os
from tkinter import *
from tkinter import ttk
from Menu import MyMenu
from AddManga import AddManga
from ListMangas import ListMangas

def openPageAddManga():
  AddManga().addManga(root)

def openPageListMangas():
  ListMangas().listMangas(root)

root = Tk()
root.title('Gerenciador de Manga')
root.geometry('500x500')

# criando barra de menu
menu = MyMenu().createMenu(root, [openPageAddManga, openPageListMangas])

main = ttk.Frame(root, padding=10)
main.grid()

ttk.Label(main, text='Hello').grid(column=0, row=0)
ttk.Button(main, text='Quit', command=root.destroy).grid(column=1, row=0)

root.mainloop()