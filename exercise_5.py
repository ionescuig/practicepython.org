#!/usr/bin python3
# title           :exercise 5
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 5:
Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:
1. Randomly generate two lists to test this.
2. Write this in one line of Python
(don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

from random import randint
print('\n=====')
# Step 1
print('Step 1:')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for el in a:
    if el in b:
        if el not in c:
            c.append(el)
print(c)

# Extras 1
print('-----')
print('Extras 1:')
a = []
b = []
a_elements = randint(1, 50)
b_elements = randint(1, 50)
for el in range(a_elements):
    a.append(randint(1, 100))
for el in range(b_elements):
    b.append(randint(1, 100))
c = []
for el in a:
    if el in b:
        if el not in c:
            c.append(el)
print(c)

# Extras 2
print('-----')
print('Extras 2:')
# print([randint(1, 100) for i in range(randint(1, 50))])
print(list(set([el for el in [randint(1, 100) for i in range(
    randint(1, 50))] if el in [randint(1, 100) for i in range(randint(1, 50))]])))

print('=====\n')
