#!/usr/bin python3
# title           :exercise 3
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 3:
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
1. Instead of printing the elements one by one, make a new list that has
all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from
the original list a that are smaller than that number given by the user.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print('\n=====')
# Step 1
print('Step 1:')
for el in a:
    if el < 5:
        print(el)

# Extras 1
print('-----')
print('Extras 1:')
b = []
for el in a:
    if el < 5:
        b.append(el)
print(b)

# Extras 2
print('-----')
print('Extras 2:')
print([el for el in a if el < 5])

# Extras 3
print('-----')
print('Extras 3:')
num = int(input('Please enter a number: '))
print([el for el in a if el < num])

print('=====\n')
