"""
Date: 20-6-2025
Author: Subrato
Desc: Single Inheritance
"""

class College:
    def __init__(self,cname, caddr , noofdeprt):
        self.cname = cname
        self.caddr = caddr
        self.no_of_deprt = noofdeprt

    def display_collegeinfo(self):
        print(f'Name: {self.cname} \t Addr: {self.caddr} \t'
              f'Department count : {self.no_of_deprt}')

