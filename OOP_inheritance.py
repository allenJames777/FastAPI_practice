# # Parent class
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount

# # Child class — gets everything BankAccount has, PLUS interest
# class SavingsAccount(BankAccount):
#     def __init__(self, owner:str, balance:float, interest_rate:float):
#         super().__init__(owner, balance)      # call parent's __init__
#         self.interest_rate = interest_rate     # new attribute, only for savings

#     def add_interest(self):                   # new method, only for savings
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         print(f"Interest added: ${interest:.2f}. New balance: ${self.balance:.2f}")

# acc = BankAccount("jeff",10000)
# print(f"Mr. Jeff's Bank balance is ${acc.balance}")
# acc.deposit(100)
# print(f"New Account Balance {acc.balance}")
# s_account = SavingsAccount("jeff",10000,.3)
# s_account.add_interest()

class Vehicle:
    def __init__(self,make:str,model:str):
        self.make = make
        self.model = model
        self.fuel = 100
        self.km_driven = 0
    
    def drive (self,km:int):
        if km > self.fuel:
           print("Not Enough Fuel")
        else:
             self.fuel -= km
             self.km_driven+=km
             print(f"Driving {km} Fuel left {self.fuel}")

    def show_info(self):
        print(f"Make:{self.make}, Model:{self.model}, Distance:{self.km_driven}KM")
        
class ElectricalVehicle(Vehicle):    
    def __init__(self,make, model):
        super().__init__(make,model)
        self.battery = 0

    def charge(self,amount:int):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"Battery Charged To {self.battery}")
    
    def drive (self,km:int):
        if km * 2 > self.battery or km * 0.5 > self.fuel:
            print(f" CANNOT DRIVE: Battery Percentage is {self.battery:.2f} and Fuel is {self.fuel:.2f}")
        else:
            self.battery -= 2*km
            self.fuel -= .5*km
            print(f"Driving... Battery left:{self.battery:.2f} Fuel left{self.fuel:.2f}")
            
    def show_info(self):
        print((f"Make:{self.make}, Vehicle:{self.model}"))



car1 = Vehicle("Bongo","Truck")
car1.drive(50)
car1.show_info()

car2 = ElectricalVehicle("BYD","BYDv1")
car2.show_info()
car2.charge(100)
car2.drive(20)


