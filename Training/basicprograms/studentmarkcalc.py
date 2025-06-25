"""
Date: 19-6-2025
Author: Subrato
Desc: Student marks calculation
"""

def calc_tot_avg(m1 ,m2, m3):
    total = m1 +m2+m3
    avg = total/3
    return total, avg

sname = input('Enter name: ')
mark1 = int(input('Mark 1: '))
mark2 = int(input('Mark 2: '))
mark3 = int(input('Mark 3: '))

total , avg = calc_tot_avg(m3 = mark3, m1 = mark1 , m2 = mark2)
print(f'Name: {sname} Total: {total} Avg: {avg}')