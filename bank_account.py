# Python OOP Bank Account System - Version 1

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")


account = BankAccount("Naina", 1000)

print(f"Account Holder: {account.account_holder}")
account.show_balance()

account.deposit(500)
account.withdraw(300)

account.show_balance()
