"""
Title: for loops with Strings with cryptography
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/12/19
Last modified: 2023/06/25
Description: Using the For loop with strings with encryption.
"""

# prints out the characters corresponding to the ASCII values between 60 and 70 inclusive
print('Print out the characters corresponding to the ASCII values between 60 and 70, inclusive.')
start_character = 60
end_character = 70

while start_character <= end_character:
    print(chr(start_character))
    start_character = start_character + 1


# it loops through each character of a string and it prints out both the letter and the ASCII value
print("\nPrints both the letter and the ASCII value of the word 'hello'.")
word = 'hello'
word = word.upper()  # change to upper

for letter in word:
    print(f'{letter} {ord(letter)}')


# Caesar cipher
print('\n          CAESAR CIPHER')
phrase_to_encode = input('Enter a phrase to encode: ')
shift = int(input('Enter the shift: '))
new_phrase = ''

for letter in phrase_to_encode:

    if letter == ' ':
        new_letter = ' '
    else:
        new_letter = chr(ord(letter) + shift)

    new_phrase = new_phrase + new_letter

print(f'The new phrase is: {new_phrase.upper()}')
