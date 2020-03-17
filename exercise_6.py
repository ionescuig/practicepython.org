#!/usr/bin python3
# title           :exercise 6
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 6:
Ask the user for a string and print out whether this string
is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

print('\n=====')

string = input('Please enter a string: ')

# Solution 1
print('-----')
print('Solution 1:')
palindrome = True
for el in range(int(len(string)/2)):
    if string[el] != string[len(string)-1-el]:
        palindrome = False
print(palindrome)

# Solution 2
print('-----')
print('Solution 2:')
print(string == string[::-1])

print('=====\n')
