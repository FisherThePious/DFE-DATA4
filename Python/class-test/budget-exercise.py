# Create a Budget class that can instantiate objects based on different budget categories like 
# food, clothing, and entertainment. These objects should allow for depositing and withdrawing funds 
# from each category, as well computing category balances and transferring balance amounts between 
# categories

food =0
clothing = 0
entertainment = 0


class Budget:

    def __init__(self) -> None:
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
    