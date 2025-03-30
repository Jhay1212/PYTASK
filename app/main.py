import  tkinter as tk
from tkinter import ttk
import customtkinter
import sqlite3
import sys
import customtkinter as ctk

from windows import AddTaskWindow

class App(ctk.CTk):
    def __init__(self, title):
        super().__init__()
        self.title('Todo App')
        self.geometry("500x500")
        self.bind("<Escape>", lambda e: self.destroy)
        self.setup_ui()
    
        # self.menu = tk.Menu(self)
        # self.add_task = tk.Menu(self.menu)
        # self.menu.add_cascade(label="File", menu=self.add_task)
        # self.add_task.add_command(label="Add Task")


        # self.update_task = tk.Menu(self.menu)
        # self.menu.add_cascade(label="Update", menu=self.update_task)
        # self.update_task.add_command(label="Update Task")

        
        # self.config(menu=self.menu)

    def setup_ui(self):
        
        self.add_task = customtkinter.CTkButton(self, text="Add Task", command=self.show_add_task_window)
        self.update_task = customtkinter.CTkButton(self, text="Update Task", command=self.show_update_task_window)

        self.add_task.pack(side=tk.LEFT)
        self.update_task.pack(side=tk.LEFT)

    def show_add_task_window(self):
        add = AddTaskWindow(self)

    def show_update_task_window(self):
        pass

    def connect_to_db(self):
        conn = sqlite3.connect("todo.db")
        return conn


    def destroy(self):
        sys.exit()
        return super().destroy()
    

if __name__ == "__main__":
    app = App("Todo App")
    app.mainloop()