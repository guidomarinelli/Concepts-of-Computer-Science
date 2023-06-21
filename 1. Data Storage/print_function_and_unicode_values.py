"""
Title: Print Function and Unicode Values
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/13
Last modified: 2023/04/09
Description: Use of the print function and Unicode values.
"""

# print my name to the console
print('Hi everyone! I am Guido and Welcome to my Program!')

# print my city of birth and where I currently live
print('I was born in Milan, but I currently live in Trieste.')

# print out the number of seconds in the current month
print('\nHere some simple questions:')
print('QUESTION 1:')
print('How many seconds are there in April?')
print('ANSWER:')
print(f'{60 * 60 * 24 * 30}s')

# calculate how many full dozens are made by 403 eggs, and how many eggs you have remaining
print('\nQUESTION 2:')
print('How many full dozen are made from 403 eggs and how many eggs do you have left?')
print('ANSWER:')
print(f'Number of complete dozens {403 // 12}')
print('Number of remaining eggs', 403 % 12)

# I assign two values, one that is an integer and one that is a string,
# to two variables and then insert them inside the print function
age = 39
job_title = 'student'
print('\nOther personal information:')
print(f'I am {age} years old')
print(f'and I am a {job_title}.')

# prints 6 different Unicode values and
# use + operator to concatenate the value and the name of the character
print('\nI display 6 different Unicode values and their names, some of them little known')
print('\u03A9' + ' Greek capital letter omega')
print('\u0975' + ' Devanagari letter aw')
print('\u26F3' + ' Flag in hole')
print('\U0001f47e' + ' Alien monster')
print('\U0001F602' + ' Face with tears of joy')
print('\U0001F648' + ' See-no-evil monkey')
