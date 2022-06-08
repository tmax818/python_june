from bankAccount import BankAccount

class User:

    def __init__(self, name, email, savings, checking):
        self.name = name
        self.email = email
        # self.accounts = [savings, checking]
        self.accounts = {
            'savings': savings, 
            'checking': checking}

    def make_deposit(self, amount, type):
        self.accounts[type].deposit(amount)

    def make_withdrawl(self, amount, type):
        self.accounts[type].withdrawl(amount)

    def display_user_balance(self):
        self.account.display_account_info()


savings = BankAccount(.1, 10000)
checking = BankAccount(.1, 5000)

Alden = User("Alden", "ac@aol.com", savings, checking)