import tkinter as tk
from tkinter import ttk


import os 
import json

from tkcalendar import Calendar
from customtkinter import *

from menu import Menu
from frame import Frame, ViewFrame, TaskFrame


from PIL import ImageTk, Image
base_path = os.getcwd()
print(base_path)





class App(tk.Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
       
        self.title('To Do App')
        self.geometry('720x480')
        self.set_ui()
        self.bind("<Escape>", lambda e:  self.quit())

    
    def window_config(self):
        self.attributes('')


    def add_task(self):
        
        from db import add_task

        add_task(self.task.get(),  self.status.get(), '2024-12-17')
        
    def view_current_task(self):
        from db import sort_by_not_done
        print(sort_by_not_done())
        
    def set_style(self):
        self.style = ttk.Style()
        self.style.configure("TButton",
                font=("Helvetica", 12),
                padding=10,
                background="#88C0D0",
                foreground="#2E3440",
                borderwidth=0)
        self.style.map("TButton",
          background=[("active", "#5E81AC")],
          foreground=[("active", "white")])

# Label Style
        self.style.configure("TLabel",
                font=("Helvetica", 14),
                foreground="white",
                background="#2E3440")


    def set_ui(self):
        self.configure(bg='#1c2322')
        self.title_label = CTkLabel(self, text="To Do App")
        self.columnconfigure(0, weight=1)
        self.task_parent = CTkFrame(self)
        self.main_frame = CTkFrame(self)      
        self.main_frame.pack()
        self.task_parent.pack()
        self.frame = Frame(self.main_frame)
        self.task = TaskFrame(self.task_parent)
        self.frame.setup()
        self.task.setup()



    def get_option(self, choice):
        self.status
        # print(choice)


    def run(self):
        self.mainloop()


app= App()
task = tk.StringVar()
status = tk.StringVar(value='Not Done')

app.run()