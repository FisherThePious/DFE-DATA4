class Student:

    def __init__(self, name, age, test1, test2, test3):
        self.name = name
        self.age = age
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3

    def average_mark(self):
        totalscore = int((self.test1 + self.test2 + self.test3)/3)
        return int(totalscore)

John = Student("John", "21", 32, 50, 65)
Jane = Student("Jane", "22", 12, 50, 43)

print(John.name, John.age, John.average_mark())
print(Jane.name, Jane.age, Jane.average_mark()) 