class Student:
    def __init__(self, id, name, current_class):
        self.id = id
        self.name = name
        self.current_class = current_class

    def __repr__(self):
        return f'Student with ID: {self.id}, Name: {self.name}, Class: {self.current_class}'
    

class Teacher:
    def __init__(self, id, name, dept, subject):
        self.id = id
        self.name = name
        self.dept = dept
        self.subject = subject

    def __repr__(self):
        return f'Teacher Name: {self.name} from Department: {self.dept}, with ID: {self.id}'
    
class School:
    def __init__(self, s_name):
        self.name = s_name
        self.Teachers = []
        self.students = []

    def enroll(self, name, fee, curr_class):
        if fee < 6500:
            print( f'You Poor {name}, Not enough fee, please provide an extra {6500 - fee} taka' )
            return
        
        id = len( self.students ) + 1
        new_student = Student(id, name, curr_class)

        self.students.append( new_student )

    def recruit_a_new_teacher(self, name, dept, sub):
        id = len( self.Teachers ) + 101
        new_teacher = Teacher(id, name, dept, sub)

        self.Teachers.append(new_teacher)

    def __repr__(self):
        print(f'________ Welcome to {self.name} ________')
        print()

        print(f'-------- Our Teachers --------')
        for tec in self.Teachers:
            print(tec)
        print()

        print(f'-------- Our Students --------')
        for st in self.students:
            print(st)
        print()

        return f'Thanks for visiting our {self.name} school'


uits = School('UITS')
uits.recruit_a_new_teacher('Safi', 'CSE', 'CN')
uits.recruit_a_new_teacher('Sadman', 'CSE', 'DSA')
uits.recruit_a_new_teacher('Ratri', 'BBA', 'CA')
uits.recruit_a_new_teacher('Sultana', 'EEE', 'CA')
uits.recruit_a_new_teacher('Murad', 'CSE', 'DBMS')


uits.enroll('Farhan', 7000, 12)
uits.enroll('Safa', 500, 20)
uits.enroll('Tamim', 1000, 9)
uits.enroll('Fahim', 100000, 50)

print(uits)






"""
You Poor Safa, Not enough fee, please provide an extra 6000 taka
You Poor Tamim, Not enough fee, please provide an extra 5500 taka
________ Welcome to UITS ________

-------- Our Teachers --------
Teacher Name: Safi from Department: CSE, with ID: 101
Teacher Name: Sadman from Department: CSE, with ID: 102
Teacher Name: Ratri from Department: BBA, with ID: 103
Teacher Name: Sultana from Department: EEE, with ID: 104
Teacher Name: Murad from Department: CSE, with ID: 105

-------- Our Students --------
Student with ID: 1, Name: Farhan, Class: 12
Student with ID: 2, Name: Fahim, Class: 50

Thanks for visiting our UITS school
"""