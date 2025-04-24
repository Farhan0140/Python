

from _1_School import School
from _2_Person import Person



class Student( Person ) :
    def __init__(self, name, classroom):
        self.classroom = classroom
        super().__init__(name)
        self.__id = None
        self.marks = {} # {'DSA': 85, 'DBMS': 80}
        self.subject_grade = {} # {'DSA': 'A+', 'DBMS': 'A+'}
        self.grade = None # total grade


    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value


    def calculate_final_grade(self):
        total_grade = 0
        gpa = 0

        for key, val in self.subject_grade.items():
            total_grade += School.grad_to_value(val)

        if total_grade == 0:
            gpa = 0.00
            self.grade = 'F'
        else:
            gpa = total_grade / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)

        # print(f'Name: {self.name} Final Grade: {self.grade} with CGPA: {gpa}')

