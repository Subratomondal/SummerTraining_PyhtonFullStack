"""
Date: 19-6-2025
Author: Subrato
Desc: for in -> for all iterators
"""


samplelist = [10,23,4,5,6,76]

'''
for elmt in samplelist:
    print(elmt)
'''

'''
for elmt in samplelist:
    print(elmt+10 , '\t', elmt**2)
'''

sampletuple = (23,43,56,34,70)
'''
for elmt in sampletuple:
    print(elmt+10 , '\t', elmt**2)
'''

sampleset = {23,43,56,34,70}
'''
for elmt in sampleset:
    print(elmt+10 , '\t', elmt**2)
'''

sampledict = {1:10, 2:20, 3:30, 4:40, 5:50}
for k,v in sampledict.items():
    print(k , '\t',v**2)