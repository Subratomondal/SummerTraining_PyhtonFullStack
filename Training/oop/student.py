"""
Date: 20-6-2025
Author: Subrato
Desc: Single Inheritance
"""

from oop.college import College

class Student(College):
    def __init__(self,cname, caddr, noofdeprt, rno, sname, sdept, sph, m1,m2,m3 ):
        super().__init__(cname, caddr, noofdeprt)
        self.rollno = rno
        self.sname = sname
        self.sdept = sdept
        self.contact = sph
        self.mark1 =m1
        self.mark2 = m2
        self.mark3 = m3

    def calc_total(self):
        return self.mark1 + self.mark2 +self.mark3

    def calc_avg(self):
        return self.calc_total() / 3

