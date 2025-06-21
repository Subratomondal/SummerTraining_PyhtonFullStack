"""
Date: 19-6-2025
Author: Subrato
Desc: Simple menu driven calculator
"""



num1 = int(input('Enter First Num'))
num2 = int(input('Enter Second Num'))
user_choice = float(input('1.0 Add  2.0 Sub 3.0 Mul'))

'''
if user_choice == 1:
    print(f'Sum: {num1 +num2}')
elif user_choice == 2:
    print(f'Diff: {num1 - num2}')
elif user_choice == 3:
    print(f'Prod: {num1 * num2}')
'''


match user_choice:
    case 1.0:
        print(f'Sum: {num1 + num2}')
    case 2.0:
        print(f'Diff: {num1 - num2}')
    case 3.0:
        print(f'Prod: {num1 * num2}')
    case _:
        print('Enter between 1-3')

print('Done')
