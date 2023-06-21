"""
Title: Concatenate and Replicate Operators
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/08/13
Last modified: 2023/04/09
Description: Print out a textual representation of the picture using concatenate and replicate operators.
"""

# strings concatenated with the + operator
print('Strings concatenated.')
print('@' + '.' + '')

# strings replicated with the * operator
print('\nStrings replicated.')
print('@@@' * 3)

# single print statement that prints out strings concatenate and replicated
print('\nStrings concatenated and replicated.')
print('&&&&..' * 4 + '+' * 5)

# print out a textual representation of the picture using concatenate and replicate operators
print('\nRepresentation of two octagons inside each other using the concatenate and replicate operators.')
print('.' * 3 + '@' * 4 + '.' * 3)
print('.' * 2 + '@' + '.' * 4 + '@' + '.' * 2)
print('.' + '@' + '.' * 6 + '@' + '.')
print('@' + '.' * 3 + '@' * 2 + '.' * 3 + '@')
print('@' + '.' * 2 + '@' + '.' * 2 + '@' + '.' * 2 + '@')
print('@' + '.' * 2 + '@' + '.' * 2 + '@' + '.' * 2 + '@')
print('@' + '.' * 3 + '@' * 2 + '.' * 3 + '@')
print('.' + '@' + '.' * 6 + '@' + '.')
print('.' * 2 + '@' + '.' * 4 + '@' + '.' * 2)
print('.' * 3 + '@' * 4 + '.' * 3)
