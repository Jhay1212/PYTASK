from customtkinter import CTkFrame, CTk
from customtkinter import *

import tkinter as tk
from tkinter import ttk

from canvas import Canvas

class Frame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        self.task = tk.StringVar()
        self.status = tk.StringVar(value='Not Done')
        super().__init__(master, *args, **kwargs, width=720)
        self.task = tk.StringVar()
        status = StringVar(value='Not Done')
        self.due = tk.StringVar()
        self.pack_propagate(False)
        self.pady = 30

        # self.place(relx=0.5, rely=0.5, anchor='center')
        self.pack()

            
    def clear_input(self, event):
        self.input_task.delete(0, 'end')
        
    def view_current_task(self):
        from db import sort_by_not_done
        print(sort_by_not_done())


    def setup(self):
            self.pack()

            self.title = CTkLabel(self, text="Task List", font=('Times New Roman', 17))
            self.title.pack()


            self.input_task  = CTkEntry(self, textvariable=self.task)
            self.input_task.insert(0, "Add a Task")
            self.input_task.pack()


            self.input_status  = CTkComboBox(self, values=["Done", "Not Done"], variable=self.status)
            # self.input_status.insert(0, "Ongiong")
            self.input_status.pack()
            # self.input_status = CTkEntry(self, text=textvariable=status)
            # self.input_status.pack()
            self.sort_frame = CTkFrame(self)
            self.sort_frame.pack()
            self.add_btn = CTkButton(self.sort_frame, command=self.add_task,
                                             text="Add Task",
                                            fg_color="#BF616A", 
                                            hover_color="#D08770",
                                            corner_radius=10)
            self.add_btn.pack()


            self.sort_frame = CTkFrame(self)
            self.sort_frame.pack()
            self.view_not_done = CTkButton(
            self.sort_frame, 
            text="View Not Done", 
            command=self.view_current_task, 
            fg_color="#BF616A", 
            hover_color="#D08770",
            corner_radius=10
        )
            self.view_not_done.pack(pady=10, padx=10)

            self.input_task.bind("<FocusIn>", self.clear_input)
        
        # canvas = Canvas(self)
        # canvas.pack()
    def add_task(self):
         from db import add_task
         add_task(self.task.get(),  self.status.get(), '2024-12-17')
        

class TaskFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        # pass

    def setup(self):
        self.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.sort_key = CTkComboBox(self, values=['Sort by not done', 'Sort by done', 'Sort by date'], command=self.sort_query)
        self.sort_key.grid(row=0, column=0, padx=40)
        update_btn = CTkButton(self, text='Update Task', command=print('kjau'))
        update_btn.grid(row=0, column=1, padx=40)
        delete_btn = CTkButton(self, text='Delete Task', command=lambda: print('k'))
        delete_btn.grid(row=0, column=2,  padx=40)

        # self.sort_key.bind('<<ComboboxSelected>>', self.sort_query)

   

    def view_current_task(self):
        from db import sort_by_not_done
        print(sort_by_not_done())

    def sort_query(self, choice):
        from db import sort_by_not_done, sort_by_date, sort_by_status
        # choice = self.sort_key.get()
        print(choice)
        if choice == 'Sort by not done':
            sort_by_not_done()
        elif choice == 'Sort by done':
            sort_by_status()
        else:
            sort_by_date()

        
class ViewFrame(CTkScrollableFrame):
    def __init__(self, master, *args, **kwargs):
        super  ().__init__(master, *args, **kwargs)
        # self.config(bg=''
        self.config(bg='#1c2322')
        self.tasks  = []


    def setup(self):
        from db import get_task_done
        self.pack()
        self.label1 = CTkLabel(self, text="History")
        self.label1.pack()
        


class HistoryFrame(CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, *kwargs)
        self.pack()

        def setup(self):
            self.config(bg='#FFFFF')
            self.label1 = CTkLabel(self, text="History")
            self.label1.pack()



if __name__ == '__main__':
    root = CTk()
    master_frame = CTkFrame(root, width=720, height=480)
    master_frame.place(x=10, y=20)

    frame = Frame(master_frame)
    frame.setup()
    view = ViewFrame(master_frame)
    view.setup()

    frame.place(relx=2, rely=2, anchor='center')
    view.place(relx=1, rely=0, anchor='center')


    
    root.mainloop()