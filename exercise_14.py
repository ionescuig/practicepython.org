#!/usr/bin python3
# title           :exercise 14
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 14:
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
1. Write two different functions to do this - one using a loop and
constructing a list, and another using sets.
2. Go back and do Exercise 5 using sets, and write the solution for that
in a different function.
"""


def sol_1(a):
    l = set(a)
    return list(l)


def sol_2(a):
    l = []
    for el in a:
        if el not in l:
            l.append(el)
    return l


if __name__ == '__main__':
    print('\n=====')
    a = [1, 2, 3, 4, 3, 4, 3, 4, 5, 3, 7, 6, 5, 8, 12, 11, 10]
    print('Original:  ', a)
    print('Solution 1:', sol_1(a))
    print('Solution 2:', sol_2(a))
    print('=====\n')
