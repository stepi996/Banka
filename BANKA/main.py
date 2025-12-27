from bank import *

oBank = Bank()

oBank.openAccount("Pavel", "123", 1000)
oBank.openAccount("Marie", "321", 5000)

while True:
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    choice = input().capitalize()
    if choice == "B":
        oBank.balance(input("Enter the account number: "))
    elif choice == "C":
        oBank.closeAccount(input("Enter the number of the account you would like to close: "))
    elif choice == "D":
        oBank.deposit(input("Enter the account number: "))
    elif choice == "O":
        oBank.openAccount(input("Create your account name: "), input("Create your password: "), input("Enter sum you would like to deposit to your new acccount (must be a whole positive number): "))
    elif choice == "Q":
        raise "Goodbye"
    elif choice == "S":
        oBank.show()
    elif choice == "W":
        oBank.withdraw(input("Enter the account number: "))
    else:
        print("Command not found")