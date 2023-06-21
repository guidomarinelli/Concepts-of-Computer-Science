"""
Title: Binary, Decimal, Hex
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/08/08
Last modified: 2023/04/09
Description: Use of Binary, Decimal, Hex values.
"""

# prints using the comma to separate inputs
print('Use of the comma in the print function to give it multiple inputs.')
print(21, 4 * 32, 'hello')

# prints the value of a variable in decimal, binary and hexadecimal form
print('\nPrint out the value of a variable in addition to its decimal form, in binary and hexadecimal form.')
x = 31
print(f'In this case we have assigned the variable x the decimal value {x}.')
print(f'x in decimal = {x}, x in binary = {bin(x)}, x in hex = {hex(x)}')

# assigning a binary or hex value to a variable
print('\nWe assign the variable y the binary value 0b1011 and the variable z the hexadecimal value 0xA3.')
y = 0b1011
z = 0xA3
print(f'y = {y}, z = {z}')

# we can add numbers in any representation
print("\nLet's add the variables x, y and z")
w = x + y + z
print('The sum is ', w)
