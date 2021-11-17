from dice import dicethrow


check = input("Would you like to roll the dice?\nPress 'Y' to roll or any key to exit\n")
if check.upper() == "Y":
    for i in range(2):
        print(dicethrow())

