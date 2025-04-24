
from _1_School import School


class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher  # Teacher Object
        self.max_mark = 100
        self.pass_mark = 40

        
    def exam(self, students):
        for st in students:
            mark = self.teacher.evaluate_exam()
            st.marks[ self.name ] = mark
            st.subject_grade[ self.name ] = School.calculate_grade(mark)


        

