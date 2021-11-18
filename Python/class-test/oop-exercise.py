from abc import ABC, abstractmethod

class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False
class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"
