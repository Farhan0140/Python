import random


from _2_Person import Person


class Teacher( Person ):
    def __init__(self, name):
        super().__init__(name)

    
    def evaluate_exam(self):
        return random.randint(50, 100)
    
    

