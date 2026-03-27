import csv
import tkinter as tk
from tkinter import ttk
import os
from datetime import date

root = tk.Tk()
root.title("Expenses Tracker")
root.geometry("900x600")

title = tk.Label(root, text="My Expenses", font=("Arial", 20, "bold"))
title.pack(padx=20, pady=20)

columns = ("Id", "Date", "Category", "Amount", "Quantity")
table = ttk.Treeview(root, columns=columns, show="headings")

table.heading("Id", text="Id")
table.heading("Date", text="Date")
table.heading("Category", text="Category")
table.heading("Amount", text="Amount")
table.heading("Quantity", text="Quantity")

table.column("Id", width=50)
table.column("Date", width=120)
table.column("Category", width=150)
table.column("Amount", width=100)
table.column("Quantity", width=100)

entries = []

# ── Total Label ──
total_var = tk.StringVar(value="Total: PKR 0")
total_label = tk.Label(root, textvariable=total_var, font=("Arial", 12, "bold"), fg="green")
total_label.pack()

def get_next_id():
    if not os.path.exists("data.csv"):
        return 1
    with open("data.csv", "r") as file:
        rows = list(csv.reader(file))
        return len(rows) + 1

def update_total():
    if not os.path.exists("data.csv"):
        total_var.set("Total: PKR 0")
        return
    total = 0
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                total += float(row[3])
            except:
                pass
    total_var.set(f"Total: PKR {total:.2f}")

def read_expense():
    if not os.path.exists("data.csv"):
        return
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            table.insert("", "end", values=row)

def refresh_table():
    for row in table.get_children():
        table.delete(row)
    read_expense()
    update_total()

def add_expense(id, category, amount, quantity):
    P_date = date.today()
    row_data = [id, P_date, category, amount, quantity]
    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row_data)

def delete_expense():
    selected = table.selection()
    if not selected:
        return
    item = table.item(selected[0])
    deleted_id = str(item["values"][0])

    table.delete(selected[0])

    all_rows = []
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            all_rows.append(row)

    remaining_rows = []
    for row in all_rows:
        if row[0] != deleted_id:
            remaining_rows.append(row)

    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_rows)

    update_total()

def add_btn():
    id = get_next_id()
    category = entries[0].get()
    amount = entries[1].get()
    quantity = entries[2].get()

    if not category or not amount or not quantity:
        return

    add_expense(id, category, amount, quantity)
    refresh_table()

    for entry in entries:
        entry.delete(0, tk.END)

def delete_btn():
    delete_expense()

addBtn = tk.Button(root, text="Add", command=add_btn,
bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), padx=10)

deleteBtn = tk.Button(root, text="Delete Selected", command=delete_btn,
bg="#f44336", fg="white", font=("Arial", 10, "bold"), padx=10)

Sr = ["Category", "Amount", "Quantity"]
for sr in Sr:
    label = tk.Label(root, text=sr, font=("Arial", 10))
    label.pack()
    entry = tk.Entry(root, font=("Arial", 10), width=30)
    entry.pack(pady=2)
    entries.append(entry)

addBtn.pack(pady=5)
deleteBtn.pack(pady=5)
table.pack(fill="both", expand=True, padx=20, pady=10)

read_expense()
update_total()

root.mainloop()