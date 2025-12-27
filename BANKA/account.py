class Account():
    def __init__(self, name: str, password: str, balance=0, accountNumber=0):
        self.name = name
        self.balance = balance
        self.password = password
        self.accountNumber = accountNumber

    def getPassword(self, heslo):
        while heslo != self.password:
            print("Password Incorrect")
            heslo = input("Please enter your password: ")

    def deposit(self):
        self.getPassword(input("Please enter your password: "))
        částka = input("Please enter a sum you would like like to deposit: ")
        positive_number = False
        while type(částka) != int or positive_number == False:
            try:
                int(částka)
            except ValueError:
                print("Please type a whole positive number")
            else:
                částka = int(částka)
                if částka < 0:
                    print("Please type a whole positive number")
                else:
                    positive_number = True
                    self.balance += částka
                    print(f"Your new balance: {self.balance}")
                    return
            částka = input("Please enter a sum you would like like to deposit: ")
        
    def withdraw(self):
        self.getPassword(input("Please enter your password: "))
        částka = input("Please enter a sum you would like like to withdraw: ")
        positive_number = False
        smaller_number = False
        while type(částka) != int or positive_number == False or smaller_number == False:
            try:
                int(částka)
            except ValueError:
                print("Please type a whole positive number")
            else:
                částka = int(částka)
                if částka < 0:
                    print("Please type a whole positive number")
                else:
                    positive_number = True
                    if částka >= self.balance:
                        print("You can't withdraw more than your current balance")
                    else:
                        smaller_number = True
                        self.balance -= částka
                        print(f"Your new balance: {self.balance}")
                        return
            částka = input("Please enter a sum you would like like to deposit: ")

    def getBalance(self):
        self.getPassword(input("Please enter your password: "))
        print(f"Your current balance: {self.balance}")

    def show(self):
        self.getPassword(input("Please enter your password: "))
        print(f"Name: {self.name}\nBalance: {self.balance}\nPassword: {self.password}\nAccount Number: {self.accountNumber}")