#!/usr/bin python3
# title           :exercise 2
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 2:
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message
to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check).
If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.
"""

print('\n==========')
num = int(input('Please enter a number: '))
check = int(input('Please enter a second number: '))

print('\n----------')
if num % 4 == 0:
    print('Your number can be divided by 4.')
elif num % 2 == 0:
    print('Your number is even.')
else:
    print('Your number is odd.')

if num % check == 0:
    print('Your first number ({}) can be divided by the second number ({}).'.format(
        num, check))
else:
    print('Your first number ({}) can not be divided by the second number ({}).'.format(num, check))
print('==========\n')
