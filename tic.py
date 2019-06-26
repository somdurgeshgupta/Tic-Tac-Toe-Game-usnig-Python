"""tictactoe game for 2 players
from blogpost: http://thebillington.co.uk/blog/posts/writing-a-tic-tac-toe-game-in-python by  BILLY REBECCHI,
slightly improved by Horst JENS"""
from __future__ import print_function

choices = []
start = True
for x in range (0, 9) :
    choices.append(str(x + 1))

playerOneTurn = True
winner = False

def printBoard() :
    print( '\n -----')
    print( '|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print( ' -----')
    print( '|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print( ' -----')
    print( '|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print( ' -----\n')

while not winner :
    printBoard()

    if playerOneTurn :
        print( "Player 1:")
    else :
        print( "Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if choices[choice - 1] == 'X' or choices [choice-1] == 'O':
        print("illegal move, plase try again")
        continue

    if playerOneTurn :
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O'

    playerOneTurn = not playerOneTurn

    for x in range (0, 3) :
        y = x * 3
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]) :
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]) :
            winner = True
            printBoard()
        if x < 2:
            if (choices[x] == choices[(x + 4)] and choices[x] == choices[(x + 8)]) :
                winner = True
                printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or 
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True
        printBoard()

    cont = False
    for i in range(0, len(choices)):
        if (choices[i] != 'X' and choices[i] != 'O'):
            cont = True
    if cont:
        continue
    else:
        print ("Match is draw!")
        start = False
        break

if start:
    print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
