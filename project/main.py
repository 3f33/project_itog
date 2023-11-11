import sqlite3
import tkinter as tk
from tkinter import messagebox

# Создание таблицы сотрудников
def create_table():
    connection = sqlite3.connect('db.db')
    c = connection.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 phone TEXT,
                 email TEXT,
                 salary REAL)''')
    connection.commit()
    connection.close()

# Добавление сотрудника
def add_employee():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    salary = entry_salary.get()

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)",
              (name, phone, email, salary))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Сотрудник успешно добавлен")

# Изменение сотрудника
def update_employee():
    id = entry_id.get()
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    salary = entry_salary.get()

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("UPDATE employees SET name=?, phone=?, email=?, salary=? WHERE id=?",
              (name, phone, email, salary, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Сотрудник успешно обновлен")

# Удаление сотрудника
def delete_employee():
    id = entry_id.get()

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Сотрудник успешно удален")

# Поиск сотрудника
def search_employee():
    id = entry_id.get()

    conn = sqlite3.connect('db.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees WHERE id=?", (id,))
    employee = c.fetchone()
    conn.close()

    if employee:
        entry_name.delete(0, tk.END)
        entry_name.insert(tk.END, employee[1])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(tk.END, employee[2])
        entry_email.delete(0, tk.END)
        entry_email.insert(tk.END, employee[3])
        entry_salary.delete(0, tk.END)
        entry_salary.insert(tk.END, employee[4])
    else:
        messagebox.showinfo("Ошибка", "Сотрудник с таким ID не найден")

# Обновление интерфейса
def refresh():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

# Создание графического интерфейса
root = tk.Tk()
root.title("Управление сотрудниками")

label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

label_name = tk.Label(root, text="ФИО:")
label_name.grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

label_phone = tk.Label(root, text="Номер телефона:")
label_phone.grid(row=2, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1)

label_email = tk.Label(root, text="Адрес электронной почты:")
label_email.grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

label_salary = tk.Label(root, text="Заработная плата:")
label_salary.grid(row=4, column=0)
entry_salary = tk.Entry(root)
entry_salary.grid(row=4, column=1)

btn_add = tk.Button(root, text="Добавить", command=add_employee)
btn_add.grid(row=5, column=0)

btn_update = tk.Button(root, text="Изменить", command=update_employee)
btn_update.grid(row=5, column=1)

btn_delete = tk.Button(root, text="Удалить", command=delete_employee)
btn_delete.grid(row=6, column=0)

btn_search = tk.Button(root, text="Поиск", command=search_employee)
btn_search.grid(row=6, column=1)

btn_refresh = tk.Button(root, text="Обновить", command=refresh)
btn_refresh.grid(row=7, column=0)

# Добавление картинок
photo_add = tk.PhotoImage(file="add.png")
btn_add_img = tk.Button(root, image=photo_add, command=add_employee)
btn_add_img.grid(row=5, column=2)

photo_update = tk.PhotoImage(file="update.png")
btn_update_img = tk.Button(root, image=photo_update, command=update_employee)
btn_update_img.grid(row=5, column=3)

photo_delete = tk.PhotoImage(file="delete.png")
btn_delete_img = tk.Button(root, image=photo_delete, command=delete_employee)
btn_delete_img.grid(row=6, column=2)

photo_search = tk.PhotoImage(file="search.png")
btn_search_img = tk.Button(root, image=photo_search, command=search_employee)
btn_search_img.grid(row=6, column=3)

photo_refresh = tk.PhotoImage(file="refresh.png")
btn_refresh_img = tk.Button(root, image=photo_refresh, command=refresh)
btn_refresh_img.grid(row=7, column=2)

create_table()

root.mainloop()
