
class User:

    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount

    def withdrawl(self, amount):
        self.account_balance -= amount



adrian = User("Adrian", "adog@aol.com", "handsomcoder123")
tyler = User("Tyler", "tmax@gail.com", "luvsCats")


