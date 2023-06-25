"""
Title: Applications of while loop
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/18
Last modified: 2023/06/25
Description: Applications of while loop.
"""

# prints out all the even numbers between two numbers that the user inputs
print('Prints out all the even numbers between two numbers.')
lower_number = int(input('Enter the lower number: '))
higher_number = int(input('Enter the higher number: '))
numbers_between = ''
count = lower_number

while count <= higher_number:

    if count % 2 == 0:
        numbers_between = numbers_between + str(count) + ' '
    count = count + 1

print(f'The even numbers between {lower_number}	and	{higher_number} are: {numbers_between}')

# prints out all the factors of a given positive integer
print('\nPrints out all the factors of a given positive integer.')
integer = int(input('Enter a positive integer: '))
divider = 1
factors = ''

while divider <= integer:

    if integer % divider == 0:
        factors = factors + str(divider) + ' '
    divider = divider + 1

print(f'The integers that are factors of {integer} are: {factors}')


# Euclidean algorithm
print('\nEuclidean algorithm.')


def greatest_common_divisor(x, y):
    if y < x:
        swap = y
        y = x
        x = swap
    while y != 0:
        rest = x % y
        x = y
        y = rest
    return x


num1 = int(input('Enter the first positive integer: '))
num2 = int(input('Enter the second positive integer: '))

print(f'GCD({num1}, {num2}) is {greatest_common_divisor(num1, num2)}')
