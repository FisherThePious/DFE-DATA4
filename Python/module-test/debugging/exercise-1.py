#import pdb
#pdb.set_trace()

user_funds = 10.31
item_price = 3.00

if item_price < user_funds:
    print("You have enough money!")
elif item_price == user_funds:
    print("You have the precise amount of money")
elif item_price > user_funds:
    print("Sorry you don't have enough money")

#==========================================================================
#   Original function which needed debugging                              |
#==========================================================================
# user_funds = 10.31
# item_price = price["Burger"]

# if item_price < user_funds:
#     Print("You have enough money!")
# if item_price = user_funds:
#     print("You have the precise amount of money")
# if item_price < user_funds:
#     print(Sorry you don't have enough money)