import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import simpledialog
import os
import re

DATA_FILE = "user_records.txt"

def save_user_data(first_name, middle_name, last_name, birthday, gender):
    try:
        with open(DATA_FILE, "a") as file:
            file.write(f"{first_name},{middle_name},{last_name},{birthday},{gender}\n")
        messagebox.showinfo("Success", "Record saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save record: {e}")

def is_valid_birthday(birthday):
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", birthday))

def view_all_records():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                records = file.readlines()
            if not records:
                messagebox.showinfo("No Records", "No records found.")
            else:
                display_records(records)
        else:
            messagebox.showinfo("No Records", "No records found.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read records: {e}")

def display_records(records):
    records_window = tk.Toplevel(window)
    records_window.title("All Records")
    records_window.geometry("600x400")
    records_window.configure(bg="#f0f0f0")

    title_label = tk.Label(records_window, text="All User Records", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
    title_label.pack(pady=10)

    tree = ttk.Treeview(records_window, columns=("First Name", "Middle Name", "Last Name", "Birthday", "Gender"), show="headings", height=10)
    
    tree.heading("First Name", text="First Name")
    tree.heading("Middle Name", text="Middle Name")
    tree.heading("Last Name", text="Last Name")
    tree.heading("Birthday", text="Birthday")
    tree.heading("Gender", text="Gender")

    tree.column("First Name", width=100, anchor="center")
    tree.column("Middle Name", width=100, anchor="center")
    tree.column("Last Name", width=100, anchor="center")
    tree.column("Birthday", width=100, anchor="center")
    tree.column("Gender", width=100, anchor="center")

    for record in records:
        first_name, middle_name, last_name, birthday, gender = record.strip().split(",")
        tree.insert("", "end", values=(first_name, middle_name, last_name, birthday, gender))

    vsb = ttk.Scrollbar(records_window, orient="vertical", command=tree.yview)
    vsb.pack(side="right", fill="y")
    tree.configure(yscrollcommand=vsb.set)
    
    hsb = ttk.Scrollbar(records_window, orient="horizontal", command=tree.xview)
    hsb.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=hsb.set)

    tree.pack(pady=20)

def sign_up():
    first_name = entry_first_name.get()
    middle_name = entry_middle_name.get()
    last_name = entry_last_name.get()
    birthday = entry_birthday.get()
    gender = entry_gender.get()

    if not (first_name and middle_name and last_name and birthday and gender):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if not is_valid_birthday(birthday):
        messagebox.showerror("Error", "Invalid birthday format! Please use YYYY-MM-DD format.")
        return

    save_user_data(first_name, middle_name, last_name, birthday, gender)

def search_record():
    surname = simpledialog.askstring("Search Record", "Enter the surname to search:")
    if surname:
        found = False
        try:
            with open(DATA_FILE, "r") as file:
                records = file.readlines()
                for record in records:
                    first_name, middle_name, last_name, birthday, gender = record.strip().split(",")
                    if last_name.lower() == surname.lower():
                        found = True
                        messagebox.showinfo("Search Result", f"Record Found: {first_name} {middle_name} {last_name}, Birthday: {birthday}, Gender: {gender}")
                        break
                if not found:
                    messagebox.showinfo("Search Result", "Record not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to search record: {e}")

def delete_record():
    surname = simpledialog.askstring("Delete Record", "Enter the surname to delete:")
    if surname:
        found = False
        try:
            with open(DATA_FILE, "r") as file:
                records = file.readlines()
            with open(DATA_FILE, "w") as file:
                for record in records:
                    first_name, middle_name, last_name, birthday, gender = record.strip().split(",")
                    if last_name.lower() != surname.lower():
                        file.write(record)
                    else:
                        found = True
                if found:
                    messagebox.showinfo("Success", f"Record with surname {surname} deleted successfully.")
                else:
                    messagebox.showinfo("Delete Result", "Record not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete record: {e}")

def clear_all_records():
    confirm = messagebox.askyesno("Clear All Records", "Are you sure you want to delete all records?")
    if confirm:
        try:
            open(DATA_FILE, "w").close()  
            messagebox.showinfo("Success", "All records have been deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear records: {e}")

def exit_program():
    window.quit()

window = tk.Tk()
window.title("User Registration System")
window.title("GUI Program made by Khalid Saverola")
window.geometry("400x550")
window.configure(bg="#f0f0f0")

title_label = tk.Label(window, text="User Registration", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

form_frame = tk.Frame(window, bg="#f0f0f0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="First Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
entry_first_name = tk.Entry(form_frame, font=("Arial", 12))
entry_first_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Middle Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
entry_middle_name = tk.Entry(form_frame, font=("Arial", 12))
entry_middle_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Last Name:", font=("Arial", 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5)
entry_last_name = tk.Entry(form_frame, font=("Arial", 12))
entry_last_name.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Birthday (YYYY-MM-DD):", font=("Arial", 12), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5)
entry_birthday = tk.Entry(form_frame, font=("Arial", 12))
entry_birthday.grid(row=3, column=1, padx=10, pady=5)

tk.Label(form_frame, text="Gender:", font=("Arial", 12), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5)
entry_gender = tk.Entry(form_frame, font=("Arial", 12))
entry_gender.grid(row=4, column=1, padx=10, pady=5)

button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Sign Up", command=sign_up, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="View All Records", command=view_all_records, width=20, height=2, bg="#2196F3", fg="white", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Search Record", command=search_record, width=20, height=2, bg="#FFC107", fg="white", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Delete Record", command=delete_record, width=20, height=2, bg="#f44336", fg="white", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Clear All Records", command=clear_all_records, width=20, height=2, bg="#9E9E9E", fg="white", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Exit", command=exit_program, width=20, height=2, bg="#f44336", fg="white", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=10)


window.mainloop()
