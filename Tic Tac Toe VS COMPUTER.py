# Nick de Rezende -- TicTacToe vs Computer (with varying difficulty perhaps)
import random

# Intro
print("""Hello! In this game you will play against a computer in Tic Tac Toe. It is an adaptation from the two player
tic tac toe game, and one meant to be played when you don't have a person to compete against. You can choose to either 
play normally, or against a challenging computer. Have fun!""")

# Determining whether or not to activate challenge bot
answers = ['Y', 'N']
challenge = input("Play against a challenging bot? (Y/N): ")
challenge = challenge.upper()
while challenge not in answers:
    challenge = input("Type 'y' or 'n': ")
    challenge = challenge.upper()

if challenge == 'Y':
    hard_bot = True
else:
    hard_bot = False


# Creating visual moveset for players
board = """TL ! TC ! TR
---+---+----
ML ! MC ! MR
---+---+----
BL ! BC ! BR """
print(board)

toprow = [' ', '', '! ', ' ', '', '!', '   ']


lines1 = "---+-----+---"

midrow = [' ', '', '! ', ' ', '', '!', '   ']


lines2 = "---+-----+---"

bottomrow = [' ', '', '! ', ' ', '', '!', '   ']


valid_moves = ['TL', 'TC', 'TR', 'ML', 'MC', 'MR', 'BL', 'BC', 'BR']

x = 'X'
o = 'O'


def print_structure():
    print(' '.join(toprow))
    print(lines1)
    print(' '.join(midrow))
    print(lines2)
    print(' '.join(bottomrow))
    return


# Randomizing who goes first
numbers = [1, 2]
current_player = random.choice(numbers)


win = False
counter = 0
while counter < 9 and not win:
    counter += 1

    if current_player == 1:
        player1_move = input("Human's turn: ")
        player1_move = player1_move.upper()

        while player1_move not in valid_moves:
            player1_move = input("That is not a valid move. ")
            player1_move = player1_move.upper()

        if player1_move == 'TL':
            toprow[0] = x
            print_structure()
            valid_moves.remove('TL')
            current_player = 2

        elif player1_move == 'TC':
            toprow[3] = x
            print_structure()
            valid_moves.remove('TC')
            current_player = 2

        elif player1_move == 'TR':
            toprow[6] = x
            print_structure()
            valid_moves.remove('TR')
            current_player = 2

        elif player1_move == 'ML':
            midrow[0] = x
            print_structure()
            valid_moves.remove('ML')
            current_player = 2

        elif player1_move == 'MC':
            midrow[3] = x
            print_structure()
            valid_moves.remove('MC')
            current_player = 2

        elif player1_move == 'MR':
            midrow[6] = x
            print_structure()
            valid_moves.remove('MR')
            current_player = 2

        elif player1_move == 'BL':
            bottomrow[0] = x
            print_structure()
            valid_moves.remove('BL')
            current_player = 2

        elif player1_move == 'BC':
            bottomrow[3] = x
            print_structure()
            valid_moves.remove('BC')
            current_player = 2

        elif player1_move == 'BR':
            bottomrow[6] = x
            print_structure()
            valid_moves.remove('BR')
            current_player = 2
    else:
        computer_move = random.choice(valid_moves)
        print("Computer's move: ", computer_move)

        if computer_move == 'TL':
            toprow[0] = o
            print_structure()
            valid_moves.remove('TL')
            current_player = 1

        elif computer_move == 'TC':
            toprow[3] = o
            print_structure()
            valid_moves.remove('TC')
            current_player = 1

        elif computer_move == 'TR':
            toprow[6] = o
            print_structure()
            valid_moves.remove('TR')
            current_player = 1

        elif computer_move == 'ML':
            midrow[0] = o
            print_structure()
            valid_moves.remove('ML')
            current_player = 1

        elif computer_move == 'MC':
            midrow[3] = o
            print_structure()
            valid_moves.remove('MC')
            current_player = 1

        elif computer_move == 'MR':
            midrow[6] = o
            print_structure()
            valid_moves.remove('MR')
            current_player = 1

        elif computer_move == 'BL':
            bottomrow[0] = o
            print_structure()
            valid_moves.remove('BL')
            current_player = 1

        elif computer_move == 'BC':
            bottomrow[3] = o
            print_structure()
            valid_moves.remove('BC')
            current_player = 1

        elif computer_move == 'BR':
            bottomrow[6] = o
            print_structure()
            valid_moves.remove('BR')
            current_player = 1

    # Win Checker
    if toprow[0] == x and toprow[3] == x and toprow[6] == x:
        win = True
    elif midrow[0] == x and midrow[3] == x and midrow[6] == x:
        win = True
    elif bottomrow[0] == x and bottomrow[3] == x and bottomrow[6] == x:
        win = True
    elif toprow[0] == x and midrow[0] == x and bottomrow[0] == x:
        win = True
    elif toprow[3] == x and midrow[3] == x and bottomrow[3] == x:
        win = True
    elif toprow[6] == x and midrow[6] == x and bottomrow[6] == x:
        win = True
    elif toprow[0] == x and midrow[3] == x and bottomrow[6] == x:
        win = True
    elif toprow[6] == x and midrow[3] == x and bottomrow[0] == x:
        win = True
    elif toprow[0] == o and toprow[3] == o and toprow[6] == o:
        win = True
    elif midrow[0] == o and midrow[3] == o and midrow[6] == o:
        win = True
    elif bottomrow[0] == o and bottomrow[3] == o and bottomrow[6] == o:
        win = True
    elif toprow[0] == o and midrow[0] == o and bottomrow[0] == o:
        win = True
    elif toprow[3] == o and midrow[3] == o and bottomrow[3] == o:
        win = True
    elif toprow[6] == o and midrow[6] == o and bottomrow[6] == o:
        win = True
    elif toprow[0] == o and midrow[3] == o and bottomrow[6] == o:
        win = True
    elif toprow[6] == o and midrow[3] == o and bottomrow[0] == o:
        win = True

if current_player == 1:
    current_player = 2
else:
    current_player = 1


if win and current_player == 1:
    print("HUMAN WINS!")

elif win and current_player == 2:
    print("COMPUTER WINS!")

else:
    print("GAME ENDED IN A TIE.")
