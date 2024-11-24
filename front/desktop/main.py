from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Gerenciador de Manga')
# root.geometry('500x500')
addManga = ttk.Frame(root, padding=10)
addManga.grid()

ttk.Label(addManga, text='Hello').grid(column=0, row=0)
ttk.Button(addManga, text='Quit', command=root.destroy).grid(column=1, row=0)


root.mainloop()