# app.py

import login_vulnerable
import login_secure

while True:
    print("\n==== SQL Injection Demo App ====")
    print("1. Login (Vulnerable)")
    print("2. Login (Secure)")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        login_vulnerable.login()
    elif choice == "2":
        login_secure.login()
    elif choice == "0":
        print("Bye 👋")
        break
    else:
        print("Invalid choice, try again.")


