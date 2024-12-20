import tkinter as tk
from tkinter import ttk
from customtkinter import *

class Menu(tk.Menu):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        