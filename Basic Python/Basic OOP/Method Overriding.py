

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print("Eat junk food every day")


class Cricketer( Person ):
    def __init__(self, name, age, weight, height, team):
        self.team = team
        super().__init__(name, age, weight, height)


    # Override the Person eat method
    def eat(self):
        print("Eat healthy food every day")



p1 = Cricketer('Juari Sakib', 39, 80, 180, 'BD')
p2 = Cricketer('Tamim', 36, 76, 176, 'BD')


