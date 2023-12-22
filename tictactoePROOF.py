# Nick de Rezende

print("""WELCOME TO TIC TAC TOE (with crude visuals)! This is designed for two players, or you can play against yourself. Player1 is X, 
and Player2 is O. For the sake of convenience, the columns are marked as L C and R, meaning left, center and right. The
 rows are marked as T M and B, meaning top, middle and bottom. On your turn, input a combination of these, such as TL 
 if you wish to go top left. Enjoy!
 _____________________________________
 """)

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


current_player = int(input("Who goes first, player (1) or player (2): "))


win = False
counter = 0
while counter < 9 and not win:
    counter += 1

    if current_player == 1:
        player1_move = input("Player1's turn: ")
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
        player2_move = input("Player2's move: ")
        player2_move = player2_move.upper()

        while player2_move not in valid_moves:
            player2_move = input("That is not a valid move. ")
            player2_move = player2_move.upper()

        if player2_move == 'TL':
            toprow[0] = o
            print_structure()
            valid_moves.remove('TL')
            current_player = 1

        elif player2_move == 'TC':
            toprow[3] = o
            print_structure()
            valid_moves.remove('TC')
            current_player = 1

        elif player2_move == 'TR':
            toprow[6] = o
            print_structure()
            valid_moves.remove('TR')
            current_player = 1

        elif player2_move == 'ML':
            midrow[0] = o
            print_structure()
            valid_moves.remove('ML')
            current_player = 1

        elif player2_move == 'MC':
            midrow[3] = o
            print_structure()
            valid_moves.remove('MC')
            current_player = 1

        elif player2_move == 'MR':
            midrow[6] = o
            print_structure()
            valid_moves.remove('MR')
            current_player = 1

        elif player2_move == 'BL':
            bottomrow[0] = o
            print_structure()
            valid_moves.remove('BL')
            current_player = 1

        elif player2_move == 'BC':
            bottomrow[3] = o
            print_structure()
            valid_moves.remove('BC')
            current_player = 1

        elif player2_move == 'BR':
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
if win:
    print("Player", current_player, 'WINS!')
else:
    print("GAME ENDED IN A TIE.")
