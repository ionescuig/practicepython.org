#!/usr/bin python3
# title           :exercise 8
# description     :Exercises from https://www.practicepython.org
# author          :Gabriel Ionescu
# date            :2020/03/17
# version         :1.0
# notes           :
# python_version  :3.7.5
# ==============================================================================

"""
Exercise 8:
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a
message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""


def get_choices():
    while True:
        try:
            player_a = int(input('Player 1: '))
            if player_a in [1, 2, 3]:
                break
        except:
            pass
    while True:
        try:
            player_b = int(input('Player 2: '))
            if player_b in [1, 2, 3]:
                break
        except:
            pass
    return(player_a, player_b)


def play_round(a, b):
    if a == 1:
        if b == 1:
            return 0
        elif b == 2:
            return 2
        else:
            return 1
    elif a == 2:
        if b == 1:
            return 1
        elif b == 2:
            return 0
        else:
            return 2
    else:
        if b == 1:
            return 2
        elif b == 2:
            return 1
        else:
            return 0


if __name__ == '__main__':
    print('\nWelcome to Rock-Paper-Scissors')

    score = [0, 0]
    while True:
        print('\nPlease input:')
        print('\t1 - for Rock')
        print('\t2 - for Paper')
        print('\t3 - for Scissors\n')

        player_a, player_b = get_choices()
        result = play_round(player_a, player_b)
        print('------------------------------')
        if result == 0:
            print('Tie')
        elif result == 1:
            print('Player 1 wins')
            score[0] += 1
        else:
            print('Player 2 wins')
            score[1] += 1
        print('Score: {}-{}'. format(score[0], score[1]))

        print('==============================')
        new_game = input('Play again (Yes: y or 1): ')
        if new_game in ['y', '1']:
            print('------------------------------')
        else:
            break
