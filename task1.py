import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("665x400+550+250")
        master.configure(bg="#F0F0F0")
        self.create_widgets()
        self.conn = sql.connect('listOfTasks.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')
        self.retrieve_database()
        master.protocol("WM_DELETE_WINDOW", self.close)
    def create_widgets(self):
        self.functions_frame = tk.Frame(self.master, bg="#DDEEFF")
        self.functions_frame.pack(side="top", expand=True, fill="both")
        self.task_label = tk.Label(self.functions_frame, text="TO-DO LIST\nEnter the Task Title:",
                                   font=("arial", 14, "bold"), bg="#DDEEFF", fg="#4682B4")  # Label background color
        self.task_label.place(x=20, y=30)
        self.task_field = tk.Entry(self.functions_frame, font=("Arial", 14), width=42, fg="black", bg="white")
        self.task_field.place(x=180, y=30)
        self.add_button = tk.Button(self.functions_frame, text="Add", width=15, bg='#28A745', fg="#FFFFFF",
                                    font=("arial", 14, "bold"), command=self.add_task)
        self.add_button.place(x=18, y=80)
        self.del_button = tk.Button(self.functions_frame, text="Remove", width=15, bg='#DC3545', fg="#FFFFFF",
                                    font=("arial", 14, "bold"), command=self.delete_task)
        self.del_button.place(x=240, y=80)
        self.del_all_button = tk.Button(self.functions_frame, text="Delete All", width=15, bg='#FD7E14', fg="#FFFFFF",
                                        font=("arial", 14, "bold"), command=self.delete_all_tasks)
        self.del_all_button.place(x=460, y=80)
        self.task_listbox = tk.Listbox(self.functions_frame, width=70, height=9, font=("bold",),
                                        selectmode='SINGLE', bg="WHITE", fg="BLACK",
                                        selectbackground="#4682B4", selectforeground="WHITE")
        self.task_listbox.place(x=17, y=140)
        self.exit_button = tk.Button(self.functions_frame, text="Exit / Close", width=52, bg='#6C757D', fg="#FFFFFF",
                                     font=("arial", 14, "bold"), command=self.close)
        self.exit_button.pack(side="bottom", pady=10)  

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.cursor.execute('INSERT INTO tasks (title) VALUES (?)', (task_string,))
            self.conn.commit()
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            the_value = self.task_listbox.get(selected_task_index)
            self.tasks.remove(the_value)
            self.list_update()
            self.cursor.execute('DELETE FROM tasks WHERE title = ?', (the_value,))
            self.conn.commit()
        except IndexError:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            self.tasks.clear()
            self.cursor.execute('DELETE FROM tasks')
            self.conn.commit()
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        self.conn.close()
        self.master.destroy()

    def retrieve_database(self):
        self.tasks = []
        for row in self.cursor.execute('SELECT title FROM tasks'):
            self.tasks.append(row[0])
        self.list_update()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
