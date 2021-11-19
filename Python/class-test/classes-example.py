dog_dict = {"Scooby": "Scared", "Snoopy": "Fighting the Red Baron"}

class Dog:

    
    def __init__(self, inputenergy):
        self.energy = inputenergy

    def speak(self):
        print(self.energy)
        print("woof")
    
    def manyspeak(self):
        for i in range(5):
            self.speak()
                

dog_dict = Dog(dog_dict)
dog_dict.speak()
scooby = Dog("Scared")
scooby.speak()
snoopy = Dog("fighting the red barron")
snoopy.speak()

