#!/usr/bin python3
# title           :exercise 9
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 9:
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
1. Keep the game going until the user types “exit”.
2. Keep track of how many guesses the user has taken,
and when the game ends, print this out.
"""

from random import randint


def get_guess():
    while True:
        guess = input('Please enter your guess: ')
        if guess == 'exit':
            return guess
        try:
            guess = int(guess)
            return guess
        except:
            pass


def result(num, user):
    if num == user:
        print('Correct')
        return 1
    elif num > user:
        print('Too low.')
        return 0
    else:
        print('Too High')
        return 0


if __name__ == '__main__':
    tries = 0
    guesses = 0
    while True:
        num = randint(1, 9)

        guess = get_guess()
        if guess == 'exit':
            print('-' * 20)
            print('Tries:\t\t', tries)
            print('Guesses:\t', guesses)
            print('=' * 20)
            break
        else:
            tries += 1
            if result(num, guess) == 1:
                guesses += 1
