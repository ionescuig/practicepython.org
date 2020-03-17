#!/usr/bin python3
# title           :exercise 7
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 7:
Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has
only the even elements of this list in it.

"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print('\n=====')

print([el for el in a if el % 2 == 0])

print('=====\n')
