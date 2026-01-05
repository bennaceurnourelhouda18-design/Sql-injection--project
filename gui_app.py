import tkinter as tk
from tkinter import messagebox
import login_vulnerable
import login_secure

def login_vul():
    user = entry_user.get()
    pwd = entry_pass.get()

    if login_vulnerable.login(user, pwd):
        messagebox.showinfo("Result", "✅ Login successful (Vulnerable)")
    else:
        messagebox.showerror("Result", "❌ Login failed (Vulnerable)")

def login_sec():
    user = entry_user.get()
    pwd = entry_pass.get()

    if login_secure.login(user, pwd):
        messagebox.showinfo("Result", "✅ Login successful (Secure)")
    else:
        messagebox.showerror("Result", "❌ Login failed (Secure)")

# ----- GUI -----
root = tk.Tk()
root.title("SQL Injection Demo")
root.geometry("300x220")

tk.Label(root, text="Username").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login Vulnerable", command=login_vul).pack(pady=10)
tk.Button(root, text="Login Secure", command=login_sec).pack()

root.mainloop()

