
# class BankAccount:
#     def __init__(self, owner:str, balance:int):
#         self.owner = owner
#         self.__balance = balance

#     def withdraw(self, amount:int):
#         if amount > self.__balance:
#             print("Insufficient funds")
#         else:
#             self.__balance -= amount
#             return amount
    
#     def get_balance(self):
#         return self.__balance
    
# #Creating an object
# account1 = BankAccount('John', 10000)
# print(account1.get_balance())      # 10000

# withdrawn = account1.withdraw(2000)
# print(f"Withdrawn amount: {withdrawn}")
# print(f"New balance: {account1.get_balance()}")

class UserAccount:
    def __init__(self,username:str,password:str):
        self.username = username
        self.__password = password

    def login(self,password:str):
        if self.username is None:
            print("Account Deleted, Cannot Login")
        elif self.__password == password:
            print("Login Successful")
        else: 
            print("Wrong Password")
    
    def delete_account(self,acc):
        if acc == self.username:
            self.username = None
            self.__password = None
            print("Account Deleted!")
        else:
            print("Account Not Found!")

    def change_password(self,old_password:str, new_password:str):
        if old_password == self.__password and len(new_password) > 6:
            self.__password = new_password
            print("password changed!")
        elif len(new_password) < 6:
            print("Password must be 6 characters or above")
        else:
            print("Check if old password is correct!")

    def get_password(self):
        return self.__password
    


acc2 = UserAccount("Allen", "passpass")
acc2.login("passpass")

acc2.change_password("passpass","gr23333")
acc2.login("gr23333")
print(f"password is:{acc2.get_password()}")
