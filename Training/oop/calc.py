"""
Date: 20-6-2025
Author: Subrato
Desc: Error Handling
"""

num1 = int(input())
num2 = int(input())
nums = [1,2,3]
ans = 0
try:
    ans = num1 // num2
    elmt = nums[5]

except ZeroDivisionError:
    print("Don't give 0 in num2")
except IndexError:
    print(f'Watch the error')
except:
    print('OOPs something went wrong !!')

else:
    print(f'Quo : {ans}')
    print(f'Element : {elmt}')

finally:
    print('Done')