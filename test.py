# Class and Object in OOP
# class = form
# object = filled in form


# Creating a class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


# Creating an object
account1 = BankAccount("John", 10000)

print(account1.owner)
print(account1.balance)
