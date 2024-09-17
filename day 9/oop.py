# class House:
#     window=1
#     door=1
#     color="red"
    
#     def set_color(self,color):
#         self.color=color
    
# ram_ko_ghar=House()
# ram_ko_ghar.set_color("blue")
# print(ram_ko_ghar.color)
# print(ram_ko_ghar.door)


#Here's a Python program demonstrating Object-Oriented Programming (OOP) with class attributes, methods, and magic methods (also known as dunder methods):

# Program: Managing a Bank Account

class BankAccount:
    # Class attribute (shared by all instances)
    bank_name = "Global Bank"
    
    # Constructor (Magic method: __init__)
    def __init__(self, owner, balance=0):
        self.owner = owner        # Instance attribute
        self.balance = balance    # Instance attribute
    
    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
    
    # Magic method to represent the object as a string
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}\nBank: {self.bank_name}"
    
    # Magic method to add two BankAccount balances together
    def __add__(self, other):
        return self.balance + other.balance

# Creating two BankAccount objects (instances)
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 1500)

# Interacting with the objects
print(account1)  # Uses __str__ magic method
account1.deposit(500)  # Depositing money
account1.withdraw(200)  # Withdrawing money

print(account2)  # Uses __str__ magic method
account2.withdraw(2000)  # Attempt to withdraw more than the balance

# Adding balances using the __add__ magic method
total_balance = account1 + account2
print(f"Total balance of both accounts: {total_balance}")


    