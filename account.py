class Account:
    is_active = False

    def __init__(self, account_number, balance, account_name):
        self.account_number = account_number
        self.balance = balance
        self.account_name = account_name
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
    def details(self):
        print( f"The account {self.account_number} with a balance of {self.balance} " )       
    
account1 = Account("123456789", 1000, "Rita khaseyi")
account2 = Account("987654321", 5000, "kimberlyy natalie")

account1.deposit(500)
account2.withdraw(1000)
account1.details()
account2.details()