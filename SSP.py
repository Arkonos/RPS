"""
Simple Scissors, Rock, Paper
"""

import random

scoreUser = 0
scorePC = 0
anotherRound = True
choiceUser = 1
choicePC = 1
outcome = 1

counterDraw = 0
counterPlayerWin = 0
counterPCWin = 0

options = {
        1 : 'Scissors',
        2 : 'Rock',
        3 : 'Paper'
}

def sanitiseUserChoice(choiceUser):
    try:
        choiceUser = int(choiceUser)
        choiceUser = options[choiceUser]
        return choiceUser
    except AttributeError:
        str.capitalize(choiceUser)
        if(choiceUser == 'Scissors' or choiceUser == 'Rock' or choiceUser == 'Paper'):
            return choiceUser
        else:
            print('Noob, try again!')

def evaluateMatchup(choiceUser, choicePC):
    '''
    1 = draw
    2 = player victory
    3 = player loss
    '''
    print('You chose:',choiceUser)
    print('PC chose:',choicePC)
    if(choiceUser == choicePC):
        return 1
    elif(choiceUser == 'Scissors'):
        if(choicePC == 'Paper'):
            return 2
        elif(choicePC == 'Rock'):
            return 3
    elif(choiceUser == 'Rock'):
        if(choicePC == 'Scissors'):
            return 2
        elif(choicePC == 'Paper'):
            return 3
    elif(choiceUser == 'Paper'):
        if(choicePC == 'Rock'):
            return 2
        elif(choicePC == 'Scissors'):
            return 3


def setScore(counterDraw,counterPlayerWin,counterPCWin,outcome):
    if(outcome == 1):
        counterDraw += 1
    elif(outcome == 2):
        counterPlayerWin += 1
    elif(outcome == 3):
        counterPCWin += 1
    return [counterDraw,counterPlayerWin,counterPCWin]


def printResult(outcome, counterDraw, counterPlayerWin, counterPCWin):
    if(outcome == 1):
        print("It's a draw")
    elif(outcome == 2):
        print("You are victorious!")
    elif(outcome == 3):
        print("You lost!")
    totalGames = counterDraw + counterPlayerWin + counterPCWin
    print('Total count after',totalGames,'Games:')
    print('Draw:', counterDraw)
    print('Win:', counterPlayerWin)
    print('Loss:', counterPCWin)

def askForAnotherRound():
    anotherRoundQuery = str.capitalize(input('Another Round? (y/n)'))
    if(anotherRoundQuery == 'N'):
        return False

while(True):
    choiceUser = input('Please type in (1) Scissors, (2) Rock or (3) Paper. ')
    choiceUser = sanitiseUserChoice(choiceUser)
    choicePC = random.choice(list(options.values()))
    outcome = evaluateMatchup(choiceUser, choicePC)
    [counterDraw,counterPlayerWin,counterPCWin] = \
        setScore(counterDraw,counterPlayerWin,counterPCWin,outcome)
    printResult(outcome, counterDraw, counterPlayerWin, counterPCWin)
    anotherRound = askForAnotherRound()
    if(anotherRound == False):
        break