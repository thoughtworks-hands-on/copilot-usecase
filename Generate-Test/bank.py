class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")

    def withdraw(self, amount):
        """Withdraw the specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")

    def get_balance(self):
        """Get the current account balance."""
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\nBalance: ${self.balance}"
