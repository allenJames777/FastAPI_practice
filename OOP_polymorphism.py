# class Notification:
#     def __init__(self, message):
#         self.message = message

#     def send(self):
#         print("Sending notification...")

# class Email(Notification):
#     def send(self):
#         print(f"Sending EMAIL: {self.message}")

# class SMS(Notification):
#     def send(self):
#         print(f"Sending SMS: {self.message}")

# class Push(Notification):
#     def send(self):
#         print(f"Sending PUSH: {self.message}")

# # Create objects
# a = Email("Welcome!")
# b = SMS("Code: 1234")
# c = Push("New message")
# d = Notification("Hello")

# # Call one by one
# a.send()    # Sending EMAIL: Welcome!
# b.send()    # Sending SMS: Code: 1234
# c.send()    # Sending PUSH: New message
# d.send()


class payment:
    def __init__(self,payment_amount:int):
        self.payment_amount = payment_amount
    def process (self):
        print("processing payment")

class credit_card(payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number
    def process(self):    # same level as __init__, not inside it
        print(f"Paid ${self.payment_amount} with Credit Card ending in {self.card_number[-4:]}")

class Gcash(payment):
    def __init__(self, amount, phone_number):
        super().__init__(amount)
        self.phone_number = phone_number

    def process(self):
        print(f"Paid ${self.payment_amount} via GCash to {self.phone_number[-3:]}")

payments = [
    credit_card(500, "4532015112830366"),
    Gcash(200, "09171234567"),
]

for p in payments:
    p.process()