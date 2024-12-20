import tkinter as tk
from tkinter import ttk


import os 
import json

from tkcalendar import Calendar
from customtkinter import *

from menu import Menu
from frame import Frame, ViewFrame


from PIL import ImageTk, Image
base_path = os.getcwd()
print(base_path)




class App(tk.Tk):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
       
        self._title = 'To Do App'
        self.geometry('720x480')
        self.task = tk.StringVar()
        self.status = StringVar(value='Not Done')
        self.due = tk.StringVar()
        self.frame = Frame(self)
        self.bind("<Escape>", lambda e:  self.quit())

        self.set_ui()


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
    
        button_image = CTkImage(Image.open(os.path.join(base_path, 'add.png')))


        self.configure(bg='#1c2322')

        # self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
  
        self.frame.pack()

        self.title = CTkLabel(self.frame, text="Task List", font=('Times New Roman', 17))
        self.title.place(relx=1, rely=1, anchor='center')
        self.title.pack()

        self.input_task  = CTkEntry(self.frame, textvariable=self.task)
        self.input_task.insert(0, "Add a Task")
        self.input_task.pack()


        self.input_status  = CTkComboBox(self.frame, values=["Done", "Not Done"], variable=self.status)
        # self.input_status.insert(0, "Ongiong")
        self.input_status.pack()
        # self.input_status = CTkEntry(self.frame, text=textvariable=self.status)
        # self.input_status.pack()

        self.add_btn = CTkButton(self.frame, text='Add Task',  command=self.add_task, image=button_image)
        self.add_btn.pack()


        self.sort_frame = CTkFrame(self)
        self.sort_frame.pack()
        self.view_not_done = CTkButton(self.sort_frame, text='View Not Done', command=self.view_current_task)
        self.view_not_done.pack()
        self.input_task.bind("<FocusIn>", self.clear_input)

    def clear_input(self, event):
        self.input_task.delete(0, 'end')


    def get_option(self, choice):
        self.status
        # print(choice)
    

   
   
    

    def run(self):
        self.mainloop()


app= App()
app.run()