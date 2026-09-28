# Python OOP Bank Account System - Version 4

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount:.2f}")
            print(f"₹{amount:.2f} deposited successfully.")
        else:
            print("Please enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Please enter a valid amount.")
        elif amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew ₹{amount:.2f}")
            print(f"₹{amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def show_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


account = BankAccount("Naina", 1000)

print(f"Account Holder: {account.account_holder}")
account.show_balance()

# Version 4: Take transaction amounts from the user
deposit_amount = float(input("Enter deposit amount: ₹"))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: ₹"))
account.withdraw(withdraw_amount)

account.show_balance()
account.show_transactions()
