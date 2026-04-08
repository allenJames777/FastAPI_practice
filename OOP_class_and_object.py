# Class and Object in OOP
# class = form
# object = filled in form

# Creating a class
# class BankAccount:
#     def __init__(self, owner:str, balance:int):
#         self.owner = owner
#         self.balance = balance

#     def withdraw(self, amount:int):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#             return amount
# #Creating an object
# account1 = BankAccount('John', 10000)
# print(account1.balance)      # 10000

# withdrawn = account1.withdraw(2000)
# print(f"Withdrawn amount: {withdrawn}")
# print(f"New balance: {account1.balance}")


# print("-----------------------------------------------------------")
# class Playlist:
#     def __init__(self, name:str):
#         self.name = name
#         self.songs = []

#     def add_song(self, song:str):
#         self.songs.append(song)

#     def remove_song(self, rem):
#         if rem in self.songs:
#             self.songs.remove(rem)
#             print(f"{rem} song is removed from the playlist")
#         else:
#             print(f"{rem} is not in the playlist")

#     def now_playing(self):
#         if self.songs:
#             return (f"Now playing {self.songs[0]}")
#         else:
#             print('Playlist is empty')

#     def show_playlist(self):
#         for i, song in enumerate(self.songs, 1):
#             print(f"{i}. {song}")


# playlist1 = Playlist("My Favorite Songs")
# playlist1.add_song("Bohemian Rhapsody")
# playlist1.add_song("Hotel California")
# playlist1.add_song("Stairway to Heaven")
# playlist1.add_song("Pompeii")

# playlist1.remove_song("Bohemian Rhapsody")
# playlist1.remove_song("Pompeii")
# playlist1.show_playlist()

# print(playlist1.now_playing())

# print("-----------------------------------------------------------")


class ShoppingCart:
    def __init__(self, owner: str):
        self.owner = owner
        self.items = []
        self.total = 0

    def add_item(self, name: str, price: float):
        self.items.append({"name": name, "price": price})
        self.total += price

    def remove_item(self, rem):
        for item in self.items:
            if item["name"] == rem:
                self.items.remove(item)
                self.total -= item["price"]
                print(f"{rem} is removed from the Cart")
                return
        print(f"{rem} not found in Cart")

    def show_cart(self):
        for i, items in enumerate(self.items, 1):
            print(f"{i}. {items['name']} - ${items['price']}")

    def checkout(self):
        print(f"{self.owner}, your total is ${self.total:.2f}. Thank you!")
        self.items = []
        self.total = 0


Shoppingcart1 = ShoppingCart("James Cart")
Shoppingcart1.add_item("Rice", 19.99)
Shoppingcart1.add_item("Fish", 30)
Shoppingcart1.add_item("Salad", 14.92)


print(Shoppingcart1.owner)
Shoppingcart1.remove_item("Salad")
Shoppingcart1.show_cart()
Shoppingcart1.checkout()
