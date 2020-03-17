
#!/usr/bin python3
# title           :exercise 1
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 1:
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that
they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and
printing out that many copies of the previous message.
(Hint: order of operations exists in Python)
2.Print out that many copies of the previous message on separate lines.
(Hint: the string "\n is the same as pressing the ENTER button)
"""

from datetime import date
year_current = date.today().year

name = input('Please enter your name: ')
while True:
    try:
        age = int(input('Please enter your age (as a number): '))
        break
    except:
        pass
year_100 = year_current + 100 - age

while True:
    try:
        copies = int(input('Please enter a number: '))
        break
    except:
        pass

print(('Hi {}, you will turn 100 years old in {}.\n'.format(name, year_100)) * copies)
