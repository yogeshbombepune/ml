from datetime import date
import numpy as np

# class Greeting:
#     def __int__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print("Destructor Started")
#
#     def say_hello(self):
#         print("Name : ", self.name)
#
#
# gr = Greeting()
# gr.say_hello()

dt1 = date(2019, 9, 28)
dt2 = date(2012, 1, 1)
print(type(dt1))
print(type(dt2))
print(dt1)
print(dt2)
print(dt1.month)
print(type(dt1.day))
print(type(type(dt2.__format__)))
print(dir(dt1))


class PartyAnimal:
    x = 0
    name = ''

    def __init__(self, name):
        self.name = name
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "Party Count : ", self.x)

    def __del__(self):
        print(self.name, " Destructed")


an = PartyAnimal("X")
an.party()
an.party()
an.party()
PartyAnimal.party(an)
print("Type ", type(an))
print("Dir ", dir(an))
print("Type ", type(an.x))
print("Type ", type(an.party))


class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)

    def __del__(self):
        print(self.name, " Destructed")


s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
j = 10

list1 = [1, 2, 3, 4, 5]
x = np.array(list1)
print(x)
