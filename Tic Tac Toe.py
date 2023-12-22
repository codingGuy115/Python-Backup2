# Nick de Rezende - 12/30/21

import sys
import random
from itertools import cycle

print("""WELCOME TO TIC TAC TOE! This is designed for two players, or you can play against yourself. Player1 is X, 
and Player2 is O. For the sake of convenience, the columns are marked as L C and R, meaning left, center and right. The
 rows are marked as T M and B, meaning top, middle and bottom. On your turn, input a combination of these, such as LT 
 if you wish to go top left. Enjoy!
 _____________________________________
 """)

# string board layout
#board = """ a ! b ! c
#---+---+---
# d ! e ! f
#---+---+---
# g ! h ! i """
#print(board)

# LIST board layout-- (MUST contain list values or else will break program)
toprow = [' ', '', '! ', ' ', '', '!', '   ']
fancy_toprow = (' '.join(toprow))

lines1 = "---+-----+---"

midrow = [' ', '', '! ', ' ', '', '!', '   ']
fancy_midrow = (' '.join(midrow))

lines2 = "---+-----+---"

bottomrow = [' ', '', '! ', ' ', '', '!', '   ']
fancy_bottomrow = (' '.join(bottomrow))

#print(fancy_toprow, lines1,  fancy_midrow, lines2, fancy_bottomrow, sep='\n')
#print("Your available moves are as follows: TL TC TR ML MC MR BL BC BR")

#print(len(board))
# Indexes of playable spaces
#print(board[57])

# Deciding who goes first
#nums = [1, 2]
#turn = random.choice(nums)
#if turn == 1:
#    player1_move = input("Player1 goes first: ")
#    player1_move = player1_move.upper()
#    player1_moved_first = True
#elif turn == 2:
#    player2_move = input("Player2 goes first: ")
#    player2_move = player2_move.upper()
#    player1_moved_first = False

# Creating a list of valid moves
valid_moves = ['TL', 'TC', 'TR', 'ML', 'MC', 'MR', 'BL', 'BC', 'BR']

#player1_move = input("PLayer one moves")

# Checking for valid input
#if player1_moved_first:
#while player1_move not in valid_moves:
#    player1_move = input("That is not a valid move. Please type one of the following: TL TC TR ML MC MR BL BC BR: ")
#    player1_move = player1_move.upper()

#if not player1_moved_first:
#while player2_move not in valid_moves:
#    player2_move = input("That is not a valid move. Please type one of the following: TL TC TR ML MC MR BL BC BR: ")
#    player2_move = player2_move.upper()

# Printing an X or an O to the screen (first turn)
# Creating variables for X and O
x = 'X'
o = 'O'

#if player1_moved_first and player1_move == 'TL':
#    #toprow.insert(0, x)
#    toprow[0] = x
#    print(' '.join(toprow))
#    print(lines1)
#    print(fancy_midrow)
#    print(lines2)
#    print(fancy_bottomrow)
#    # Removing the move from moves so it can't be used twice in the same game
#    valid_moves.remove('TL')

"""
elif not player1_moved_first and player2_move == 'TL':
    #toprow.insert(0, o)
    toprow[0] = o
    print(' '.join(toprow))
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('TL')

# 2nd instance
if player1_moved_first and player1_move == 'TC':
    toprow[3] = x
    print(' '.join(toprow))
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('TC')

elif not player1_moved_first and player2_move == 'TC':
    toprow[3] = o
    print(' '.join(toprow))
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('TC')
# 3rd instance
if player1_moved_first and player1_move == 'TR':
    toprow[6] = x
    print(' '.join(toprow))
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('TR')

elif not player1_moved_first and player2_move == 'TR':
    toprow[6] = o
    print(' '.join(toprow))
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('TR')
# 4th instance
if player1_moved_first and player1_move == 'ML':
    midrow[0] = x
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('ML')

elif not player1_moved_first and player2_move == 'ML':
    midrow[0] = o
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('ML')
# 5th instance
if player1_moved_first and player1_move == 'MC':
    midrow[3] = x
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('MC')

elif not player1_moved_first and player2_move == 'MC':
    midrow[3] = o
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('MC')
# 6th instance
if player1_moved_first and player1_move == 'MR':
    midrow[6] = x
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('MR')

elif not player1_moved_first and player2_move == 'MR':
    midrow[6] = o
    print(fancy_toprow)
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(fancy_bottomrow)
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('MR')
# 7th instance
if player1_moved_first and player1_move == 'BL':
    bottomrow[0] = x
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BL')

elif not player1_moved_first and player2_move == 'BL':
    bottomrow[0] = o
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BL')
# 8th instance
if player1_moved_first and player1_move == 'BC':
    bottomrow[3] = x
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BC')

elif not player1_moved_first and player2_move == 'BC':
    bottomrow[3] = o
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BC')
# 9th instance
if player1_moved_first and player1_move == 'BR':
    bottomrow[6] = x
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BR')

elif not player1_moved_first and player2_move == 'BR':
    bottomrow[6] = o
    print(fancy_toprow)
    print(lines1)
    print(fancy_midrow)
    print(lines2)
    print(' '.join(bottomrow))
    # Removing the move from moves so it can't be used twice in the same game
    valid_moves.remove('BR')


#Main loop for rest of game
OVER = False
while not OVER:
    print(valid_moves)

"""

#Creating a function to alternate between 1 and 2 in order to switch turns between players
alternator = cycle((1, 2))


def print_structure():
    print(' '.join(toprow))
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(' '.join(bottomrow))
    return


counter = 0
while counter < 10:
    counter += 1

    # Creating cycler to alternate player moves
    alternator = cycle((1, 2))
    if alternator == 1:
        player1_move = input("Player1's turn: ")
        player1_move = player1_move.upper()
        while player1_move not in valid_moves:
            player1_move = input("That is not a valid move. Please type one of the following")
            player1_move = player1_move.upper()
        if player1_move == 'TL':
            # toprow.insert(0, x)
            toprow[0] = x
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TL')
        elif player1_move == 'TC':
            toprow[3] = x
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TC')
        elif player1_move == 'TR':
            toprow[6] = x
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TR')
        elif player1_move == 'ML':
            midrow[0] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('ML')
        elif player1_move == 'MC':
            midrow[3] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('MC')
        elif player1_move == 'MR':
            midrow[6] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('MR')
        elif player1_move == 'BL':
            bottomrow[0] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BL')
        elif player1_move == 'BC':
            bottomrow[3] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BC')
        elif player1_move == 'BR':
            bottomrow[6] = x
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BR')

    else:
        player2_move = input("Player2's move: ")
        player2_move = player2_move.upper()
        while player2_move not in valid_moves:
            player2_move = input("That is not a valid move. Please type one of the following")
            player2_move = player2_move.upper()
        if player2_move == 'TL':
            # toprow.insert(0, o)
            toprow[0] = o
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TL')
        elif player2_move == 'TC':
            toprow[3] = o
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TC')
        elif player2_move == 'TR':
            toprow[6] = o
            print_structure()
            '''
            print(' '.join(toprow))
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('TR')
        elif player2_move == 'ML':
            midrow[0] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('ML')
        elif player2_move == 'MC':
            midrow[3] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('MC')
        elif player2_move == 'MR':
            midrow[6] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(' '.join(midrow))
            print(lines2)
            print(fancy_bottomrow)'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('MR')
        elif player2_move == 'BL':
            bottomrow[0] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BL')
        elif player2_move == 'BC':
            bottomrow[3] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BC')
        elif player2_move == 'BR':
            bottomrow[6] = o
            print_structure()
            '''
            print(fancy_toprow)
            print(lines1)
            print(fancy_midrow)
            print(lines2)
            print(' '.join(bottomrow))'''
            # Removing the move from moves so it can't be used twice in the same game
            valid_moves.remove('BR')
print("GAME ENDED.")

# Main Loop
#counter = 0
#while counter < 10:
#    playing()
#    counter += 1
#print("GAME ENDED.")
