import MySQLdb
import random

con = MySQLdb.connect(user='root',
                      host='localhost',
                      password='sambasivarao@1')

cursor=con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS pdbc_2_bank")
cursor.execute("use pdbc_2_bank")

cursor.execute("Create table if not exists holder_details (Holder_name varchar(50), aadhar_no bigint, mobile bigint, " \
"ifsc varchar(20),account_type varchar(20), account_no bigint, balance int)")

class Bank:
    def create_account(self):
        Holder_name=input('Enter Holder Name : ')
        Aadhar_no= int(input("Enter AAdhar no : "))
        Mobile = int(input("Enter Mobile no : "))
        IFSC = "IFSC0123"
        Account_Type = input("Select one (saving/zero) : ")
        Account_no= random.randint(00000000000,99999999999)

        Balance = 500 if Account_Type=='saving' else 100

        sql="insert into holder_details values('%s',%s,%s,'%s','%s',%s,%s)"
        cursor.execute(sql%(Holder_name,Aadhar_no,Mobile,IFSC,Account_Type,Account_no,Balance))
        print("Account Created Successfully !")
        con.commit()

    def deposit(self):
        Acc_no = int(input("Enter the account number : "))
        D_amount = int(input("Enter the Deposite Amount : "))
        sql="update holder_details set balance=balance+%s where account_no=%s"
        cursor.execute(sql%(D_amount,Acc_no))
        print("Amount Deposited successfully")
        con.commit()

    def withdraw(self):
        Acc_no = int(input("Enter the account number : "))
        W_amount = int(input("Enter the Withdraw Amount : "))
        
        cursor.execute(f'select Balance from holder_details where Account_no={Acc_no}')
        data=cursor.fetchone()
        
        if W_amount<=data[0]:
            cursor.execute(f"update holder_details set balance=balance-{W_amount} where account_no={Acc_no}")
            print("Withdraw was Successfully")
        else:
            print("Insuffcient Balance")
        con.commit()
 
    def delete_account(self):
        Acc_no=int(input("Enter the account number : "))
        cursor.execute(f'delete from holder_details where account_no={Acc_no}')
        print("Account deleted Successfully")
        con.commit()

obj=Bank()

while True:
    choice=int(input("1.Create Account\n2.Deposit\n3.Withdraw\n4.Delete Account\n5.Exit\nEnter your choice : "))
    match choice:

        case 1:
            obj.create_account()
        case 2:
            obj.deposit()
        case 3:
            obj.withdraw()
        case 4:
            obj.delete_account()
        case 5:
            break

con.close()