"""
Date: 20-6-2025
Author: Subrato
Desc: Overloading
"""

# Python do not allow Method overloading

class Operations:
    '''def sub(self,num1):
        return -num1'''

    def sub(self,num1,num2=0):
        return num1-num2


op = Operations()
print(op.sub(num1=10))
print(op.sub(num1 = 10, num2 = 5))