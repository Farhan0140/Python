


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # {'DSA' : teacher_obj}
        self.classrooms = {}    # {'11': classroom_obj}

    
    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom


    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher


    def student_admission(self, student):
        class_room = student.classroom.name
        self.classrooms[class_room].add_student( student )


    @staticmethod
    def calculate_grade(mark):
        if mark >= 80 and mark <= 100:
            return 'A+'
        elif mark >= 75 and mark <  80:
            return 'A' 
        elif mark >= 70 and mark < 75 : 
            return 'A-'
        elif mark >= 65 and mark < 70 : 
            return 'B+'
        elif mark >= 60 and mark < 65 : 
            return 'B'
        elif mark >= 55 and mark < 60 : 
            return 'B-'
        elif mark >= 50 and mark < 55 : 
            return 'C+'
        elif mark >= 45 and mark < 50 : 
            return 'C'
        elif mark >= 40 and mark < 45 : 
            return 'D'
        else:
            return 'F'
        
        
    @staticmethod
    def grad_to_value(grade): # 
        grade_map = {
            'A+' : 4.00,
            'A' : 3.75,
            'A-' : 3.50,
            'B+' : 3.25,
            'B' : 3.00,
            'B-' : 2.75,
            'C+' : 2.50,
            'C' : 2.25,
            'D' : 2.00,
            'F' : 00
        }

        return grade_map[grade]
    

    @staticmethod
    def value_to_grade(value):
        if value > 3.75 and value <= 4.00:
            return 'A+'
        elif value > 3.50 and value <= 3.75 :
            return 'A'
        elif value > 3.25 and value <= 3.50 :
            return 'A-'
        elif value > 3.00 and value <= 3.25 :
            return 'B+'
        elif value > 2.75 and value <= 3.00 :
            return 'B'
        elif value > 2.50 and value <= 2.75 :
            return 'B-'
        elif value > 2.25 and value <= 2.50 :
            return 'C'
        elif value > 2.00 and value <= 2.25 :
            return 'D'
        else:
            return 'F'


    def __repr__(self):

        print(' * ____ All Classrooms ____ * ')
        for key in self.classrooms.keys():
            print(key)
        print()


        print(' * ____ All Subjects ____ * ')
        sub = ""
        for key, value in self.classrooms.items():
            sub += f'  Class {key.capitalize()} _____ \n'

            for subject in value.subjects:
                sub += f'{subject.name}\n'
        print(sub)


        # All Teachers
        print(' * ____ All Teachers ____ * ')
        for key, val in self.teachers.items():
            print(f'> {val.name}')



        print(' * ____ All Students ____ * ')
        result = ""
        for key, value in self.classrooms.items():
            result += f'  From {key.upper()} ____ \n'
            for student in value.students:
                result += f'{student.name}\n'
        print(result)


        print(' * _____ Students Results ____ * ')
        for key, value in self.classrooms.items():
            for student in value.students:
                print(f' -> {student.name}')
                for sub_name, grade in student.marks.items():
                    print(f'-- {sub_name}: {grade} --> {student.subject_grade[ sub_name ]}')
                print(student.grade)

        return ''


        

