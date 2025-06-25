"""
Date: 22-6-2025
Author: Subrato
Desc: for in -> count number of vowels and consonants
"""
from numbers import Number

text = input("Enter a string ")

no_of_vowels = 0
no_of_consonants =0

vowels = "aeiouAEIOU"

for char in text:
    if char.isalpha(): # check if character is a letter
        if char in vowels:
            no_of_vowels +=1
        else:
            no_of_consonants +=1

print(f'Number of consonants : {no_of_consonants}')
print(f'Number of vowels : {no_of_vowels}')