# implement a banking system

class Customer:
    def __init__(self, Amount, balance):
        self.Amount= Amount
        self.balance= balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds.")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance is {self.balance}.")

user1 = Customer(10000,10000)

user1.debit(100)
user1.credit(5000)