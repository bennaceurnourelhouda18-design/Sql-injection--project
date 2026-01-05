# Sql-injection--project
SQL Injection mini-project for Security and Privacy module
SQL Injection Mini-Project
📌 Project Title
SQL Injection Attack and Prevention Techniques
📖 Description
This project was developed as part of the Security and Privacy module. It demonstrates how SQL
Injection attacks work on an insecure authentication system and how such attacks can be prevented
using secure coding practices.
The application provides two login modes: - Vulnerable Login: susceptible to SQL Injection attacks. -
Secure Login: protected using prepared statements (parameterized queries).
The goal of this project is educational: to understand the risks of SQL Injection and the importance of
secure database programming.
🛠️ Technologies Used
Programming Language: Python
Database: SQLite
Environment: Console-based application
📂 Project Structure
sql-injection-project/
│
├── app.py
├── database.py
├── login_vulnerable.py
├── login_secure.py
├── security.db
├── README.md
▶️ How to Run the Project
1️⃣ Requirements
Python 3.x installed on your system
12️⃣ Steps
Clone or download the repository:
git clone <repository-link>
Navigate to the project folder.
Run the database initialization script (only once):
python database.py
Run the main application:
python app.py
Choose between:
Vulnerable Login
Secure Login
🧪 Testing SQL Injection
Vulnerable Login Example
Username: ' OR '1'='1
Password: anything
✅ Login succeeds (authentication bypassed)
Secure Login Result
Using the same input: ❌ Login fails
This confirms that prepared statements effectively prevent SQL Injection attacks.
📊 Educational Outcomes
Understanding how SQL Injection attacks occur
Observing real exploitation on vulnerable code
Learning how prepared statements protect databases
Comparing insecure vs secure authentication mechanisms
2⚠️ Disclaimer
This project is for educational purposes only. The demonstrated attacks should not be used on real
systems without authorization.
👩🎓 Author
Name: Bennaceur Nour Elhouda
Module: Security and Privacy
Academic Year: 2025–2026
🔗 GitHub Repository
(Add your GitHub repository link here)
