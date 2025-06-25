"""
Date: 20-6-2025
Author: Subrato
Desc: Multilevel Inheritance
"""
from math import expm1

from oop.student import Student


class Elective(Student):
    def __init__(self, cname, caddr, noofdeprt, rno, sname, sdept, sph, m1, m2, m3 ,e1,e2):
        super().__init__(cname, caddr, noofdeprt, rno, sname, sdept, sph, m1, m2, m3)

        self.elective1= e1
        self.elective2 = e2

    def calc_total(self):
        return self.mark1 + self.mark2 + self.mark3+ self.elective1+ self.elective2

    def calc_avg(self):
        return self.calc_total() / 5