import sqlite3
from datetime import datetime
import os 

base_path = os.getcwd()
if not os.path.exists('database.db'):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE new_task(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT, due DATE)")
    conn.commit()
    print("Database Created")
else:
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()


def sort_by_date():
    res = conn.execute("SELECT * FROM new_task ORDER BY due DESC")
    print(res.fetchall())
    return res.fetchall()

def sort_by_not_done():
    res = conn.execute("SELECT * FROM new_task WHERE status = 'Not Done'")
    print(res.fetchall())
    return res.fetchall()

def sort_by_status():
    res = conn.execute("SELECT * FROM new_task ORDER BY status")
    print(res.fetchall())
    return res.fetchall()
def fetch_result():
    res = conn.execute("SELECT  id, task, status, due FROM new_task")
    print(res.fetchall())
    return res.fetchall()

def add_task(task, status, date):
    data = [(task,  status, date)]
    conn.executemany("INSERT INTO new_task (task, status, due) VALUES (?, ?, ?)", data)
    print("Data Committed")
    conn.commit()


def update_task(task_id, task):
    query = f"UPDATE new_task SET task = {task} WHERE id = {task_id}"
    conn.execute(query)
    conn.commit()
    

def get_task_done():
    res = conn.execute("SELECT * FROM new_task WHERE status = 'Done'")
    return res.fetchall()
# cursor.execute("CREATE TABLE task(task, status, date)")
# print(cursor)

if __name__ == '__main__':
    print(get_task_done())
    add_task('jhay', 'jhay', 'jhay')
    fetch_result()

# update_task()