#!/usr/bin python3
# title           :exercise 15
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 15:
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order. For example, say I type the string:
    My name is Michele
Then I would see the string:
    Michele is name My
shown back to me.
"""


def revesed_string(a):
    l1 = a.split()
    l2 = l1[::-1]
    return ' '.join(l2)


if __name__ == '__main__':
    print('\n=====')
    user = input('Please enter a long string: ')
    print('Original string:', user)
    print('Reversed string:', revesed_string(user))
    print('=====\n')
