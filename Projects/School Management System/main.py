
from _1_School import School
from _3_Teacher import Teacher
from _4_Student import Student
from _5_Subject import Subject
from _6_ClassRoom import ClassRoom



uits = School('UITS', 'Bot_Tola')

eee = ClassRoom('EEE')
cse = ClassRoom('CSE')
bba = ClassRoom('BBA')

uits.add_classroom(cse)
uits.add_classroom(eee)
uits.add_classroom(bba)


_1 = Student('Nadim', cse)
_2 = Student('Farhan', cse)
_3 = Student('Mitu', bba)
_4 = Student('Sadi', bba)
_5 = Student('Mahi', eee)
_6 = Student('Nafi', eee)
_7 = Student('Safa', cse)


uits.student_admission(_1)
uits.student_admission(_2)
uits.student_admission(_3)
uits.student_admission(_4)
uits.student_admission(_5)
uits.student_admission(_6)
uits.student_admission(_7)


__1 = Teacher('Safi')
__2 = Teacher('Sonia')
__3 = Teacher('Sadman')


dsa = Subject('DSA', __3)
dbms = Subject('DBMS', __1)
ged = Subject('History', __2)
java = Subject('JAVA', __3)
ca = Subject('CA', __1)

cse.add_subject(dsa)
cse.add_subject(dbms)
eee.add_subject(ca)
bba.add_subject(ged)
cse.add_subject(java)

uits.add_teacher(eee, __1)
uits.add_teacher(eee, __2)
uits.add_teacher(cse, __3)
uits.add_teacher(bba, __1)

cse.take_semester_final()
eee.take_semester_final()
bba.take_semester_final()


print( uits )
