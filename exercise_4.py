#!/usr/bin python3
# title           :exercise 4
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 4:
Create a program that asks the user for a number and then prints out
a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly
into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

print('\n=====')
num = int(input('Please enter a number: '))
l = []
for i in range(2, int(num/2)+1):
    if num % i == 0:
        l.append(i)
print(l)
print('=====\n')
