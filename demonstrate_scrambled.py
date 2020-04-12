# -*- coding: utf-8 -*-
"""
Finalised on 10.04.2020

@author: Alina Podschun

A short script to demonstrate the functions defined in the module
scrambled_text.py on basis of user-generated input.
    
"""
from scrambled import scramble_without_firstlast
from scrambled import scramble_all
from scrambled import scramble_shortwords
from scrambled import random_uppercase

example = input('Please enter a sentence or some words of your choice.')
short = input('How many letters do you think long words have at the minimum? '
               'Please enter a whole number.')
short = int(short)

print('\n')
print('This is your sentence:', example)
print('\n')
print('Function scramble_all scrambles every word:', scramble_all(example))
print('\n')
print('Function scramble_without_firstlast instead leaves the first and last '
      'letter of each word in place:', scramble_without_firstlast(example))
print('\n')
print('Function scramble_shortwords scrambles only short words: ', 
      scramble_shortwords(example, short))
print('\n')
print('Function random_uppercase creates random capitals in the words: ', 
      random_uppercase(example))