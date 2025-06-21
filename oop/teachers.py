"""
Date: 20-6-2025
Author: Subrato
Desc: Hierarchical Inheritance
"""

from oop.college import College


class Teachers(College):
    def __init__(self, cname, caddr, noofdeprt, eid, tname , tdept , tsal):
        super().__init__(cname, caddr, noofdeprt)
        self.empid = eid
        self.tname = tname
        self.tdept = tdept
        self.salary = tsal

    def dispaly_teacher_info(self):
        print(f'Employee Id: {self.empid} Name: {self.tname} Dept: {self.tdept} '
              f'Salary: {self.salary}')
