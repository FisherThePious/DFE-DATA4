# Create a Budget class that can instantiate objects based on different budget categories like 
# food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds 
# from each category, as well computing category balances and transferring balance amounts between 
# categories
balance = 1500
food = 0
clothing = 0
leisure = 0
navigation = 0
navigation1 = 0
navigation2 = 0
class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self):
        if self.category == "food":
            self.category += self.amount
        elif self.category == "clothing":
            self.category += self.amount
        elif self.category == "leisure":
            self.category += self.amount

    def withdraw(self):
        if self.category == "food":
            self.category -= self.amount
        elif self.category == "clothing":
            self.category -= self.amount
        elif self.category == "leisure":
            self.category -= self.amount

    def balance(self):
        if self.category == "food":
            return self.category
        elif self.category == "clothing":
            return self.category
        elif self.category == "leisure":
            return self.category
while True:

    print(str("=========================================\nWelcome to the Budget Calculator\n========================================="))
    print(str("This script should allow you to check your balance, and allocate a pool of money to three categories: food, clothing and leisure."))
    navigation = int(input("What would you like to do?\n[1]Add money to a pool\n[2]Remove money from a pool\n[3]Check the current balance of a pool\n"))
    