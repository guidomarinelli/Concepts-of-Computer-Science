"""
Title: Python's string operations
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/19
Last modified: 2023/06/25
Description: Perform operations on strings.
"""

# asks the user to enter a phrase. If the phrase equals the same phrase in uppercase,
# it tells the user 'Stop shouting please!'
print("'STOP SHOUTING PLEASE!'")
word = input('Enter a phrase: ')

if word == word.upper():
    print('Stop shouting please!')


# asks the user to enter a string, it counts the number of different vowels ( a, e, i, o, u) that are in the string
# and print out the total
print('\nCount the number of different vowels in a word.')
string = input('Enter a string: ')
string.lower()
count = 0

if 'a' in string:
    count = count + 1
if 'e' in string:
    count = count + 1
if 'i' in string:
    count = count + 1
if 'o' in string:
    count = count + 1
if 'u' in string:
    count = count + 1

print(f'{string} has {count} different vowels')

# asks the user to enter two strings and print out the string that comes first in alphabetical order
print('\nWhich word comes first in alphabetical order?')
string1 = input('Enter a string: ')
string2 = input('Enter another string: ')

if string1.lower() > string2.lower():
    temp = string1
    string1 = string2
    string2 = temp

print(f'{string1} comes before {string2}')

# asks the user to enter their email address twice. If the two strings are not equal,
# it prints out a message stating that the two inputs are not equal, and ask the user to enter each again.
# Print out 'Thank You!' at the end of the program
print('\nVerify e-mail address.')
check = False

while not check:
    email_address = input('Enter your email address: ')
    email_address_check = input('Enter your email address again: ')

    if email_address != email_address_check:
        print('The two inputs did not match.')
    else:
        check = True

print('Thank you!')
