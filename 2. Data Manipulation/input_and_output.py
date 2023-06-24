"""
Title: Input and output
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/15
Last modified: 2023/06/24
Description: Using the input and print functions.
"""

# asks the user to enter their name. Then he says hello and repeats their name
print('Please enter your name so I can say hello.')
name = input('what is your name? ')
print('Hello ' + name)

# asks the user to enter their age. Print their age in 5 years
print('\nEnter your age and I will tell you your age in 5 years.')
age = int(input('what is your age? '))
print('In 5 years you will be ' + str(age + 5) + ' years old')

# calculates the weekly wage, asking the user to enter the number of hours worked and his hourly wages,
# and prints the output rounding it to 2 decimal places
print('\nCalculate the weekly paycheque.')
hours_worked = float(input('Enter the number of hours worked: '))
hourly_wage = float(input('Enter your hourly wage, without the $: '))

weekly_paycheck = hours_worked * hourly_wage

print(f'Your gross pay this week is $ {weekly_paycheck:.2f}')
