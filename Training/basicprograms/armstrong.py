"""
Date: 19-6-2025
Author: Subrato
Desc: Armstrong Number
"""

user_value = int(input('Enter a number: '))
original = user_value
sum =0
while user_value>0:
    rem = user_value%10
    sum = sum +(rem**3)
    user_value = user_value//10

if sum==original:
    print('Armstrong number')
else:
    print('Not Armstrong number')