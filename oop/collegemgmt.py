"""
Date: 20-6-2025
Author: Subrato
Desc: Single Inheritance , multilevel , hierarchical
"""
from oop.elective import Elective
from oop.student import Student
from oop.teachers import Teachers

# Taking info from user
cnm = input('College name ')
cad = input('College address ')
depts = int(input('Department '))

rno = int(input('Roll no '))
snm = input('Student Name ')
sdept = input('Student Department ')
phno = int(input('Phone No '))
m1 = int(input('Mark 1 '))
m2 = int(input('Mark 2 '))
m3 = int(input('Mark 3 '))

e1 = int(input('Elective 1 '))
e2 = int(input('Elective 2 '))

eid = int(input('Emp Id '))
tnm = input('Teacher Name ')
tdept = input('Teacher department')
salary = int(input('Salary '))

# Object creation

#Below object is for student class which is Single inheritance
'''stud = Student(noofdeprt=depts,cname=cnm , rno=rno, caddr=cad ,sdept=sdept ,
               sname=snm, sph=phno,m3=m3,m2 = m2, m1=m1)
'''

# Below object is for elective class which is Multilevel Inheritance
'''stud = Elective(noofdeprt=depts,cname=cnm , rno=rno, caddr=cad ,sdept=sdept ,
               sname=snm, sph=phno,m3=m3,m2 = m2, m1=m1 ,e2=e2 ,e1=e1)
'''


'''stud.display_collegeinfo()
print(f'Student Rno: {stud.rollno} Name: {stud.sname} Department: {stud.sdept} '
      f'Average Score: {stud.calc_avg()}')
'''

# Below obj  is for Teacher class which is an example of Hierarchical inheritance
teacher = Teachers(noofdeprt=depts,cname=cnm,caddr=cad,
                   tname=tnm, tdept=tdept, tsal=salary,eid=eid)

teacher.dispaly_teacher_info()
