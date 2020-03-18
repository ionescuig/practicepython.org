#!/usr/bin python3
# title           :exercise 17
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 17:
Use the BeautifulSoup and requests Python packages to print out a list of
all the article titles on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print('\n=====')

    page = requests.get("https://www.nytimes.com/").content
    soup = BeautifulSoup(page, "html.parser")
    articles = soup.find_all("h2", class_="esl82me0")
    for article in articles:
        print(article.text)

    print('=====\n')
