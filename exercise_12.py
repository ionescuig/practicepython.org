#!/usr/bin python3
# title           :exercise 12
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 12:
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""


def new_list(a):
    new = [a[0], a[-1]]
    print(new)


if __name__ == '__main__':
    print('\n=====')
    a = [5, 10, 15, 20, 25]
    new_list(a)
    print('=====\n')
