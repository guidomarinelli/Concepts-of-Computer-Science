"""
Title: Defining functions
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/15
Last modified: 2023/06/24
Description: Using the input and print functions.
"""


# It defines a function that returns the average of 3 numbers and testing it
def average(num1=0.0, num2=0.0, num3=0.0):
    """Calculate the average of three numbers.

    Keyword arguments:
    num1 -- first value entered (default 0.0)
    num2 -- second value entered (default 0.0)
    num3 -- third value entered (default 0.0)
    """
    return (num1 + num2 + num3) / 3


print('Prints the average of three numbers: (7, 5, 9) and (6, 6, 7).')
print(average(7, 5, 9))
print(average(6, 6, 7))


# It defines a function that converts a dog's age into human years and testing it
def converts_dogs_age_in_human_age(dog_age=0):
    """Converts a dog's age into human years.

        Rule: dog's age in human years = 24 + (dog's age - 2) x 4

    Keyword arguments:
    dog_age -- age of the dog (default 0)
    """
    return 24 + (dog_age - 2) * 4


print('\nAge converter of dogs in human age.')
ages_your_dog = int(input('Enter the age of your dog: '))
print(f'{ages_your_dog} dog years is equivalent to {converts_dogs_age_in_human_age(ages_your_dog)} human years.')


# It defines a function that calculate the price of an ice cream cone and testing it
def price_ice_cream_con(num_scoops=0):
    """Calculate the price of an ice cream cone.

        Rule: price = number of scoops x $1.15 + $2.25

    Keyword arguments:
    num_scoops -- number of scoops (default 0)
    """
    return num_scoops * 1.15 + 2.25


print('\nIce cream cone price calculator: ')
number_scoops = int(input('How many scoops would you like? '))
price = price_ice_cream_con(number_scoops)

print(f'A {number_scoops}-scoop cone will cost ${price:.2f}')
