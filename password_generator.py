
import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)


def copy_password():
    password = result_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

title = tk.Label(root, text="Password Generator",
                 font=("Arial", 18, "bold"))
title.pack(pady=15)

tk.Label(root, text="Enter Password Length").pack()

length_entry = tk.Entry(root)
length_entry.pack(pady=5)
length_entry.insert(0, "12")

generate_btn = tk.Button(root, text="Generate Password",
                         command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(root, width=35)
result_entry.pack(pady=10)

copy_btn = tk.Button(root, text="Copy Password",
                     command=copy_password)
copy_btn.pack(pady=10)

root.mainloop()
