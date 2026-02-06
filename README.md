# 🏦 Bank Management System using Python & MySQL

A menu-driven **Bank Management System** built using **Python**, **MySQL**, and **Object-Oriented Programming (OOP)** concepts.  
This project simulates basic banking operations such as account creation, deposit, withdrawal, and account deletion.

---

## 🚀 Features

- Create a new bank account
- Deposit money
- Withdraw money with balance validation
- Delete an existing account
- Persistent data storage using MySQL
- Random account number generation
- Simple and interactive CLI interface

---

## 🛠️ Technologies Used

- **Python**
- **MySQL**
- **MySQLdb Connector**
- **OOP Concepts**
- **SQL (CRUD Operations)**

---

## 🧠 Concepts Covered

- Object-Oriented Programming (Classes & Methods)
- Database Connectivity in Python
- SQL Queries (CREATE, INSERT, UPDATE, DELETE, SELECT)
- Transaction Management (`commit`)
- Input validation & business logic
- Menu-driven program design

---

## 📂 Database Structure

**Database Name:** `pdbc_2_bank`  
**Table:** `holder_details`

| Column Name    | Data Type     |
|---------------|---------------|
| Holder_name   | VARCHAR(50)   |
| aadhar_no     | BIGINT        |
| mobile        | BIGINT        |
| ifsc          | VARCHAR(20)   |
| account_type  | VARCHAR(20)   |
| account_no    | BIGINT        |
| balance       | INT           |

---

## ▶️ How to Run the Project

1. Install MySQL and start the server
2. Install MySQLdb connector:
   ```bash
   pip install mysqlclient
3. Update MySQL credentials in the code
4. Run the Script :
   ```bash
   python bank.py

## Sample Output

1. Create Account
2. Deposit
3. Withdraw
4. Delete Account
5. Exit
Enter Your Choice : 

<br>
👨‍💻 Author

Samba Siva Rao Ch <br>
Aspiring Software Engineer | Python | MySQL | Backend Development
