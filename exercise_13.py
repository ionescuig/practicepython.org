#!/usr/bin python3
# title           :exercise 13
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 13:
Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence
to generate
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in
the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fib(n):
    l = [1, 1]
    for i in range(n-2):
        l.append(l[-1] + l[-2])
    print(l)


if __name__ == '__main__':
    print('\n=====')
    num = int(input('Please enter a number (bigger than 2): '))
    fib(num)
    print('=====\n')
