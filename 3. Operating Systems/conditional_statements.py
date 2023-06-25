"""
Title: if statements with else and elif
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/16
Last modified: 2023/06/25
Description: Using the conditional if statement with else and elif.
"""

# determines whether an integer is divisible by 5 or by 2
print("It's a multiple of 2 or 5! Let's find out!")
number = int(input("Enter an integer: "))
if number % 5 == 0:
    print(str(number) + ' is divisible by 5')
else:
    print(str(number) + ' is not divisible by 5')

if number % 2 == 0:
    print(str(number) + ' is divisible by 2')
else:
    print(str(number) + ' is not divisible by 2')

# asks the user to enter a State/Province name, and print out the capital of that state
print('\nCapital from State.')
state = input('Enter a State/Province name: ')
if state == 'Wisconsin':
    print('Denver')
elif state == 'Colorado':
    print('Denver')
elif state == 'Nevada':
    print('Carson City')
elif state == 'Kansas':
    print('Topeka')
elif state == 'New Mexico':
    print('Santa Fe')
else:
    print('I do not know that one')


# determines the entrance prices into a determinate public swimming pool based on age
def pool_admission(age):
    """Return the price based on the age entered."""
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 61:
        return 6
    else:
        return 4


print('\nPrices of public swimming pools')
client_age = int(input('Enter the client age: '))
entrance_price = float(pool_admission(client_age))
print(f'For {client_age} year olds the price is ${entrance_price:.2f}')
