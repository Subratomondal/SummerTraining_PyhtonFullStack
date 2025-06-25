"""
Date: 20-6-2025
Author: Subrato
Desc: Error Handling
"""
from myexceptions.prjexceptions import AgelimitError

per_name = input('Name: ')
per_age = int(input('Age : '))

try:
    if per_age < 18:
        raise AgelimitError('Not Eligible')

except AgelimitError as ale:
    print(ale)

else:
    print('Eligible!! ')


