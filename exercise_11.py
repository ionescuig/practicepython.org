#!/usr/bin python3
# title           :exercise 11
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 11:
Ask the user for a number and determine whether the number is prime or not.
(| prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions.
"""


def get_number():
    while True:
        try:
            num = int(input('Please enter a number: '))
            return num
        except:
            pass


def prime(n):
    answer = True
    for i in range(2, int(n/2)+1):
        if num % i == 0:
            answer = False
            break
    return answer


if __name__ == '__main__':
    print('\n=====')
    num = get_number()
    is_prime = prime(num)
    if is_prime:
        print('{} is a prime number'.format(num))
    else:
        print('{} is NOT a prime number'.format(num))

    print('=====\n')
