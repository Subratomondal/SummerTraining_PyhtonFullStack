"""
Date: 19-6-2025
Author: Subrato
Desc: Sum of squares
"""

num = int(input('Enter the number : '))

sum=0
for n in range( 1 ,num+1):
    sum += n**2

print(f'Sum of sq : {sum}')