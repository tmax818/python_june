from bankAccount import BankAccount

class User:

    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def display_user_balance(self):
        self.account.display_account_info()


savings = BankAccount(.1, 10000)

Alden = User("Alden", "ac@aol.com", savings)