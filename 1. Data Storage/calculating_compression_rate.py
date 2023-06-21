"""
Title: Calculating Compression Rate
Author: [Guido Marinelli](https://github.com/GuidoMarinelli/)
Date created: 2021/08/13
Last modified: 2023/04/09
Description: Program that calculate the percent of compression given the formula:
                Percent of compression = (Compressed Text Size + Dictionary size)
                divided by original size. Subtract this value from 100%.
"""

compressed_text_size = 148

original_size = 240
dictionary_size = 25

compr_text_size_plus_dict_size = compressed_text_size + dictionary_size
percent_of_compression = 1 - (compr_text_size_plus_dict_size / original_size)

print(f'Compressed text size: {compressed_text_size} characters')
print(f'     Dictionary size: {dictionary_size} characters')
print(f'               Total: {compr_text_size_plus_dict_size} characters')
print(f'  Original text size: {original_size} characters')
print(f'         Compression: {percent_of_compression:.2%}')