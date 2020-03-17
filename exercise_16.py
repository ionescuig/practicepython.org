#!/usr/bin python3
# title           :exercise 16
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 16:
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of
lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user
asks for a new password.
Include your run-time code in a main method.

Extra:
    Ask the user how strong they want their password to be. For weak passwords,
    pick a word or two from a list.
"""

import random
import string


def pass_gen(pass_len):
    l = []
    chars = string.ascii_letters + string.digits + string.punctuation
    l = [random.choice(chars) for i in range(pass_len)]
    return ''.join(l)


if __name__ == '__main__':
    print('\n=====')
    pass_len = int(input('Please enter how long the password should be: '))
    print('Password:', pass_gen(pass_len))
    print('=====\n')
