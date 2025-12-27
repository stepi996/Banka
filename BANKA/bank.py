from account import *

class Bank():
    def __init__(self):
        self.accountDict = {}
        self.nextAccountNumber = 1000

    def createAccount(self, jméno, heslo, částka=0):
        oAccount = Account(jméno, heslo, částka, self.nextAccountNumber)
        self.nextAccountNumber += 1
        return oAccount
    
    def openAccount(self, jméno, heslo, částka=0):
        positive_number = False
        while type(částka) != int or positive_number == False:
            try:
                int(částka)
            except ValueError:
                print("Your balance must be a whole positive number")
                částka = input("Enter your new account balance: ")
            else:
                částka = int(částka)
                if částka < 0:
                    print("Your balance must be a whole positive number")
                    částka = input("Enter your new account balance: ")
                else:
                    positive_number = True
                    oAccount = self.createAccount(jméno, heslo, částka)
                    self.accountDict[oAccount.accountNumber] = oAccount

    def closeAccount(self, accountNumber):
        while type(accountNumber) != int or accountNumber not in self.accountDict.keys():
            try:
                int(accountNumber)
            except ValueError:
                accountNumber = input("Please type a NUMBER of the account: ")
            else:
                accountNumber = int(accountNumber)
                if accountNumber not in self.accountDict.keys():
                    accountNumber = input("Account number not found, try different: ")
                else:
                    choice = input(f"Are you sure you want to close account {accountNumber}? Y/N: ").capitalize()
                    while choice != "Y" and choice != "N":
                        choice = input("Invalid option, try again: ").capitalize()
                    if choice == "Y":
                        self.accountDict[accountNumber].getPassword(input("Please enter this account's password: "))
                        print(f"Account {accountNumber} will be paid off in the amount of {self.accountDict[accountNumber].balance}")
                        self.accountDict[accountNumber].balance -= self.accountDict[accountNumber].balance
                        self.accountDict.pop(accountNumber)
                        return
                    elif choice == "N":
                        return
                    
    def balance(self, accountNumber):
        while type(accountNumber) != int or accountNumber not in self.accountDict.keys():
            try:
                int(accountNumber)
            except ValueError:
                accountNumber = input("Please type a NUMBER of the account: ")
            else:
                accountNumber = int(accountNumber)
                if accountNumber not in self.accountDict.keys():
                    accountNumber = input("Account number not found, try different: ")
                else:
                    self.accountDict[accountNumber].show()

    def deposit(self, accountNumber):
        while type(accountNumber) != int or accountNumber not in self.accountDict.keys():
            try:
                int(accountNumber)
            except ValueError:
                accountNumber = input("Please type a NUMBER of the account: ")
            else:
                accountNumber = int(accountNumber)
                if accountNumber not in self.accountDict.keys():
                    accountNumber = input("Account number not found, try different: ")
                else:
                    self.accountDict[accountNumber].deposit()

    def withdraw(self, accountNumber):
        while type(accountNumber) != int or accountNumber not in self.accountDict.keys():
            try:
                int(accountNumber)
            except ValueError:
                accountNumber = input("Please type a NUMBER of the account: ")
            else:
                accountNumber = int(accountNumber)
                if accountNumber not in self.accountDict.keys():
                    accountNumber = input("Account number not found, try different: ")
                else:
                    self.accountDict[accountNumber].withdraw()

    def show(self):
        for i, j in self.accountDict.items():
            print(i, j.name)