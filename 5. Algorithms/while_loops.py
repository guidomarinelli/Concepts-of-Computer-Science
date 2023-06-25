"""
Title: while loops
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/18
Last modified: 2023/06/25
Description: Use of the while loops.
"""

# asks the user for an integer and the amount of the decrease: prints the interval up to 0,
# determining if the numbers are even or odd
print('Prints a range up to 0, determining whether the numbers are even or odd.')
x = int(input('Enter an integer: '))
decrease = int(input('Enter decrease: '))

while x > 0:

    if x % 2 == 0:
        print(str(x) + ' is even')
    else:
        print(str(x) + ' is odd')

    x = x - decrease

print('blastoff!!')

# print out words until the word has a length less than 5
print('\nPrint out words until the word has a length less than 5.')
word = input('Enter a word: ')

while len(word) > 4:
    print(word, 'has', len(word), 'letters')
    word = input('Enter a word: ')
print('goodbye')

# counts from 10 to 100 in decimal, binary, and hex
print('\nCounts from 10 to 100 in decimal, binary, and hex.')
i = 10
while i <= 100:
    print(i, bin(i), hex(i))
    i = i + 1
