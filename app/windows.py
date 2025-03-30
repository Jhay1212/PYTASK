import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import datetime

month, day, year = datetime.date.today().strftime("%B %d, %Y").split()
print(month, day, year)


class AddTaskWindow(ctk.CTkToplevel):
    def __init__(self, master: tk.Tk| None, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.title("Add Task")
        self.task_name_var = tk.StringVar()
        self.task_description_var = tk.StringVar()
        self.due_date_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.cal =   Calendar(master,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=int(year), month=month, day=day, text_variable=self.due_date_var, on_command=lambda: print(self.due_date_var.get()))


        self.geometry("600x600")

        self.label = ctk.CTkLabel(self, text="Add Task")
        self.label.pack()
        self.setup_ui()
    
    def setup_ui(self):
        # self.setup_style()
        self.frame = ctk.CTkFrame(self)
        self.frame.pack()
        self.task_name = ctk.CTkEntry(self.frame, placeholder_text="Task Name", textvariable=self.task_name_var)
        self.task_name.pack()
        self.description = ctk.CTkEntry(self.frame, placeholder_text="Description")
        self.description.pack()
        self.cal.pack()
        # self.due_date.pack()
        self.status = ctk.CTkRadioButton(self.frame, text="Not Started", variable=self.status_var, value="Not Started")
        self.status_started = ctk.CTkRadioButton(self.frame, text="Started", variable=self.status_var, value="Started")
        self.status_completed = ctk.CTkRadioButton(self.frame, text="Completed", variable=self.status_var, value="Completed")
        self.status.pack()
        self.status_started.pack()
        self.status_completed.pack()
    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", foreground="black", background="white", font=("Arial", 12, "bold"))




if __name__ == "__main__":
    app = ctk.CTk()
    window = AddTaskWindow(app)
    app.mainloop()