from customtkinter import CTkFrame
from customtkinter import *

import tkinter as tk
from tkinter import ttk

from canvas import Canvas
class Frame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.place(relx=0.5, rely=0.5, anchor='center')
    

        
        # canvas = Canvas(self)
        # canvas.pack()
class ViewFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super  ().__init__(master, *args, **kwargs)


    def menu(self):
        menubar = tk.Menu(self)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label='Menu', command=lambda: print('k'))
        file_menu.add_command(label='Menudo', command=lambda: print('k'))
        file_menu.add_command(label='Menuthree', command=lambda: print('k'))
        menubar.add_cascade(label='Edit', command=lambda: print('edit'))