#!/usr/bin/python3

"""
Simple Scissors, Rock, Paper game for command line
"""

import random
import sys


def sanitise_user_choice(choice_user):
    ''' Normalise user input to valid word from OPTIONS '''

    try:
        choice_user = int(choice_user)
        if choice_user == 4:
            sys.exit('Goodbye!')
        choice_user = OPTIONS[choice_user]
        return choice_user
    except AttributeError:
        str.capitalize(choice_user)
        if choice_user == 'Quit':
            sys.exit('Goodbye')
        if choice_user in OPTIONS.values():
            return choice_user
        else:
            print('Noob, try again!')


def evaluate_matchup(choice_user, choice_computer):
    ''' Compares the selection to determine the outcome of the current round.

    1 = draw
    2 = player victory
    3 = player loss
    '''
    print('You chose:', choice_user)
    print('computer chose:', choice_computer)
    if choice_user == choice_computer:
        outcome = 1
    elif choice_user == 'Scissors':
        if choice_computer == 'Paper':
            outcome = 2
        elif choice_computer == 'Rock':
            outcome = 3
    elif choice_user == 'Rock':
        if choice_computer == 'Scissors':
            outcome = 2
        elif choice_computer == 'Paper':
            outcome = 3
    elif choice_user == 'Paper':
        if choice_computer == 'Rock':
            outcome = 2
        elif choice_computer == 'Scissors':
            outcome = 3
    return outcome


def set_score(count_draw, count_player_win, count_computer_win, outcome):
    ''' Takes the outcome of the current round
            and adapts the running score. '''

    if outcome == 1:
        count_draw += 1
    elif outcome == 2:
        count_player_win += 1
    elif outcome == 3:
        count_computer_win += 1
    return [count_draw, count_player_win, count_computer_win]


def print_result(outcome, count_draw, count_player_win, count_computer_win):
    ''' Takes the output of the current round,
            prints the selectiong and the running score '''

    if outcome == 1:
        print("It's a draw")
    elif outcome == 2:
        print("You are victorious!")
    elif outcome == 3:
        print("You lost!")
    total_games = count_draw + count_player_win + count_computer_win
    print('Total count after', total_games, 'Games:')
    print('Draw:', count_draw)
    print('Win:', count_player_win)
    print('Loss:', count_computer_win)


def game():
    ''' Runs the game. '''

    count_draw = 0
    count_player_win = 0
    count_computer_win = 0
    while True:
        choice_user = input(
               'Please enter (1) Scissors, (2) Rock, (3) Paper or (4) quit. ')
        choice_user = sanitise_user_choice(choice_user)
        choice_computer = random.choice(list(OPTIONS.values()))
        outcome = evaluate_matchup(choice_user, choice_computer)
        [count_draw, count_player_win, count_computer_win] = \
            set_score(
                    count_draw, count_player_win, count_computer_win, outcome)
        print_result(outcome, count_draw, count_player_win, count_computer_win)


OPTIONS = {
    1: 'Scissors',
    2: 'Rock',
    3: 'Paper'
}

game()
