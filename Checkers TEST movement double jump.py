line_A = ['! ', 'W12', '', '! ', '   ', '', '! ', 'W11', '', '! ', '   ', '', '! ', 'W10', '', '! ', '   ', '', '! ',
          'W_9', '', '! ', '   ', '', '!', ]
line_B = ['! ', '   ', '', '! ', 'W_8', '', '! ', '   ', '', '! ', 'W_7', '', '! ', '   ', '', '! ', 'W_6', '', '! ',
          '   ', '', '! ', 'W_5', '', '!', ]
line_C = ['! ', 'W_4', '', '! ', '   ', '', '! ', 'W_3', '', '! ', '   ', '', '! ', 'W_2', '', '! ', '   ', '', '! ',
          'W_1', '', '! ', '   ', '', '!', ]
line_D = ['! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ',
          '   ', '', '! ', '   ', '', '!', ]
line_E = ['! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ', '   ', '', '! ',
          '   ', '', '! ', '   ', '', '!', ]
line_F = ['! ', '   ', '', '! ', 'B_1', '', '! ', '   ', '', '! ', 'B_2', '', '! ', '   ', '', '! ', 'B_3', '', '! ',
          '   ', '', '! ', 'B_4', '', '!', ]
line_G = ['! ', 'B_5', '', '! ', '   ', '', '! ', 'B_6', '', '! ', '   ', '', '! ', 'B_7', '', '! ', '   ', '', '! ',
          'B_8', '', '! ', '   ', '', '!', ]
line_H = ['! ', '   ', '', '! ', 'B_9', '', '! ', '   ', '', '! ', 'B10', '', '! ', '   ', '', '! ', 'B11', '', '! ',
          '   ', '', '! ', 'B12', '', '!', ]

# String separators for visual appeal
top_separator = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator1 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator2 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator3 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator4 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator5 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator6 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
separator7 = "+-------+-------+-------+-------+-------+-------+-------+-------+"
bottom_separator = "+-------+-------+-------+-------+-------+-------+-------+-------+"


def print_board():
    print(top_separator)
    print(' '.join(line_A))
    print(separator1)
    print(' '.join(line_B))
    print(separator2)
    print(' '.join(line_C))
    print(separator3)
    print(' '.join(line_D))
    print(separator4)
    print(' '.join(line_E))
    print(separator5)
    print(' '.join(line_F))
    print(separator6)
    print(' '.join(line_G))
    print(separator7)
    print(' '.join(line_H))
    print(bottom_separator)
    return


print_board()

# making lists to keep track of Black and White pieces
black_pieces = ['B_1', 'B_2', 'B_3', 'B_4', 'B_5', 'B_6', 'B_7', 'B_8', 'B_9', 'B10', 'B11', 'B12']
white_pieces = ['W_1', 'W_2', 'W_3', 'W_4', 'W_5', 'W_6', 'W_7', 'W_8', 'W_9', 'W10', 'W11', 'W12']

# black starts always
'''black_move_piece = input("Black's move. Which piece? (B_3 for example) > ")
while black_move_piece not in black_pieces:
    black_move_piece = input("Please type one of the black pieces on the board. > ")'''


# function to eliminate repeats


def ask_black():
    black_move_piece = input("Black's move. Which piece? (B_3 for example) > ")
    while black_move_piece not in black_pieces:
        black_move_piece = input("Please type one of the black pieces on the board. > ")
    return (black_move_piece)


# (black_move_piece) = ask_black()


def ask_white():
    white_move_piece = input("White's move. Which piece? (W_3 for example) > ")
    while white_move_piece not in white_pieces:
        white_move_piece = input("Please type one of the white pieces on the board. > ")
    return (white_move_piece)


# (white_move_piece) = ask_white()
'''
print("Black piece chosen: ", black_move_piece)'''


# Locating black piece chosen and giving available moves


def find_black_piece():
    landing_location = 0
    if black_move_piece in line_A:
        print("piece in line A, king spot")
        # EVENTUALLY will be KING scenario

    elif black_move_piece in line_B:
        # creating overall variable to be used later in function
        line = line_B

        outside_line = line_A

        # IMPORTANT-- THIS RAISED AN ERROR-- EAT_LINE was NOT assigned anything (Assign it something that will work)
        eat_line = 'NONE'

        # print("piece in line B")
        a_u_list = []
        index = 0
        allowed_A = [line_A[1], line_A[4], line_A[7], line_A[10], line_A[13], line_A[16], line_A[19], line_A[22]]
        allowed = allowed_A
        for e in line_A:
            if e not in allowed_A:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_C:
        # creating overall variable to be used later in function
        line = line_C

        outside_line = line_B

        eat_line = line_A

        # print("piece in line C")
        a_u_list = []
        index = 0
        allowed_B = [line_B[1], line_B[4], line_B[7], line_B[10], line_B[13], line_B[16], line_B[19], line_B[22]]
        allowed = allowed_B
        for e in line_B:
            if e not in allowed_B:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_D:
        # creating overall variable to be used later in function
        line = line_D

        outside_line = line_C

        eat_line = line_B

        # print("piece in line D")
        a_u_list = []
        index = 0
        allowed_C = [line_C[1], line_C[4], line_C[7], line_C[10], line_C[13], line_C[16], line_C[19], line_C[22]]
        allowed = allowed_C
        for e in line_C:
            if e not in allowed_C:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_E:
        # creating overall variable to be used later in function
        line = line_E

        outside_line = line_D

        eat_line = line_C

        # print("piece in line E")
        a_u_list = []
        index = 0
        allowed_D = [line_D[1], line_D[4], line_D[7], line_D[10], line_D[13], line_D[16], line_D[19], line_D[22]]
        allowed = allowed_D
        for e in line_D:
            if e not in allowed_D:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_F:
        # creating overall variable to be used later in function
        line = line_F

        outside_line = line_E

        eat_line = line_D

        # print("piece in line F")
        a_u_list = []
        index = 0
        allowed_E = [line_E[1], line_E[4], line_E[7], line_E[10], line_E[13], line_E[16], line_E[19], line_E[22]]
        allowed = allowed_E
        for e in line_E:
            if e not in allowed_E:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_G:
        # creating overall variable to be used later in function
        line = line_G

        outside_line = line_F

        eat_line = line_E

        # print("piece in line G")
        a_u_list = []
        index = 0
        allowed_F = [line_F[1], line_F[4], line_F[7], line_F[10], line_F[13], line_F[16], line_F[19], line_F[22]]
        allowed = allowed_F
        for e in line_F:
            if e not in allowed_F:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif black_move_piece in line_H:
        # creating overall variable to be used later in function
        line = line_H

        outside_line = line_G

        eat_line = line_F

        # print("piece in line H")
        a_u_list = []
        index = 0
        allowed_G = [line_G[1], line_G[4], line_G[7], line_G[10], line_G[13], line_G[16], line_G[19], line_G[22]]
        allowed = allowed_G
        for e in line_G:
            if e not in allowed_G:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    # Displaying the location as a row 1-8
    banned = ['!', '! ', '']

    locations = []
    for i in line:
        if i not in banned:
            locations.append(i)
    # print(locations)

    row = 1
    for x in locations:
        if x == black_move_piece:
            captured_row = row
            # print("piece chosen is in row", row)
        row += 1

    # Finding actual indexes in line that will be changed per move --IMPORTANT --
    counter = 0
    for c in line:
        if c == black_move_piece:
            playable_black_piece_location = counter
        counter += 1

    # print(a_u_list)

    # FINALLY - Telling what options player has diagonally, available or unavailable
    index = captured_row - 1

    if captured_row == 1:
        if a_u_list[index + 1] == 'available':
            MOVE_RIGHT = True
            MOVE_LEFT = False
        else:
            MOVE_RIGHT = False
            MOVE_LEFT = False

    elif captured_row == 8:
        if a_u_list[index - 1] == 'available':
            MOVE_LEFT = True
            MOVE_RIGHT = False
        else:
            MOVE_LEFT = False
            MOVE_RIGHT = False

    elif captured_row == 2 or captured_row == 3 or captured_row == 4 or captured_row == 5 or captured_row == 6 or captured_row == 7:
        if a_u_list[index - 1] == 'available':
            MOVE_LEFT = True
        else:
            MOVE_LEFT = False
        if a_u_list[index + 1] == 'available':
            MOVE_RIGHT = True
        else:
            MOVE_RIGHT = False

    # Motion
    left_move_loc = playable_black_piece_location - 3
    right_move_loc = playable_black_piece_location + 3

    # eat LOCATION possibilities
    eat_left_loc = playable_black_piece_location - 6
    eat_right_loc = playable_black_piece_location + 6

    # Checking left and right move location in outside_line- to determine if an eat is possible
    # Making sure that the landing spot is actually on the board
    if eat_left_loc >= 1:
        SKIP_L = False
    else:
        SKIP_L = True
        EAT_LEFT = False

    if eat_line != 'NONE':
        if not SKIP_L:
            if outside_line[left_move_loc] in white_pieces and eat_line[eat_left_loc] == '   ':
                EAT_LEFT = True
                MOVE_LEFT = False
            else:
                EAT_LEFT = False
    else:
        EAT_LEFT = False
        EAT_RIGHT = False

    # Making sure that the landing spot is actually on the board
    if eat_right_loc <= 22:
        SKIP_R = False
    else:
        SKIP_R = True
        EAT_RIGHT = False

    if eat_line != 'NONE':
        if not SKIP_R:
            if outside_line[right_move_loc] in white_pieces and eat_line[eat_right_loc] == '   ':
                EAT_RIGHT = True
                MOVE_RIGHT = False
            else:
                EAT_RIGHT = False
    else:
        EAT_LEFT = False
        EAT_RIGHT = False

    print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
    print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)

    # Getting possible eaten locations
    if EAT_LEFT:
        for element in white_pieces:
            if element == outside_line[left_move_loc]:
                possible_left_eaten_piece = element
    if EAT_RIGHT:
        for element in white_pieces:
            if element == outside_line[right_move_loc]:
                possible_right_eaten_piece = element

    # Moving the piece

    direction = input("Which way, (l)eft or (r)ight, would you like to move? >")
    while direction != 'l' and direction != 'r':
        direction = input("Type 'l' or 'r' > ")

    eat_left_executed = False
    eat_right_executed = False

    # Move sequence

    print("double jump: ", DOUBLE_JUMP)
    if not DOUBLE_JUMP:
        if direction == 'l' and MOVE_LEFT:
            outside_line[left_move_loc] = black_move_piece
            line[playable_black_piece_location] = '   '

        elif direction == 'r' and MOVE_RIGHT:
            outside_line[right_move_loc] = black_move_piece
            line[playable_black_piece_location] = '   '

    # eat sequence

    if direction == 'l' and EAT_LEFT:
        # Placing piece on new position
        eat_line[eat_left_loc] = black_move_piece
        # Finding the landing location to use for double jump
        landing_location = eat_line[eat_left_loc]
        # putting space where piece used to be
        line[playable_black_piece_location] = '   '
        # removing opposing piece off board and from list
        outside_line[left_move_loc] = '   '
        white_pieces.remove(possible_left_eaten_piece)
        # making a variable to track what happened
        eat_left_executed = True

    if direction == 'r' and EAT_RIGHT:
        # Placing piece on new position
        eat_line[eat_right_loc] = black_move_piece
        # Finding the landing location to use for double jump
        landing_location = eat_line[eat_right_loc]
        # putting space where piece used to be
        line[playable_black_piece_location] = '   '
        # removing opposing piece off board and from list
        outside_line[right_move_loc] = '   '
        white_pieces.remove(possible_right_eaten_piece)
        # making a variable to track what happened
        eat_right_executed = True

    # Pulling move_right and move_left out of the function to use later
    return (MOVE_RIGHT, MOVE_LEFT, playable_black_piece_location, outside_line, line, eat_line, captured_row,
            EAT_LEFT, EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed)


# function for white piece
def find_white_piece():
    landing_location = 0
    if white_move_piece in line_H:
        print("piece in line H, king spot")

    elif white_move_piece in line_B:
        # creating overall variable to be used later in function
        line = line_B

        outside_line = line_C

        eat_line = line_D

        # print("piece in line B")
        a_u_list = []
        index = 0
        allowed_C = [line_C[1], line_C[4], line_C[7], line_C[10], line_C[13], line_C[16], line_C[19], line_C[22]]
        allowed = allowed_C
        for e in line_C:
            if e not in allowed_C:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_C:
        # creating overall variable to be used later in function
        line = line_C

        outside_line = line_D

        eat_line = line_E

        # print("piece in line C")
        a_u_list = []
        index = 0
        allowed_D = [line_D[1], line_D[4], line_D[7], line_D[10], line_D[13], line_D[16], line_D[19], line_D[22]]
        allowed = allowed_D
        for e in line_D:
            if e not in allowed_D:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_D:
        # creating overall variable to be used later in function
        line = line_D

        outside_line = line_E

        eat_line = line_F

        # print("piece in line D")
        a_u_list = []
        index = 0
        allowed_E = [line_E[1], line_E[4], line_E[7], line_E[10], line_E[13], line_E[16], line_E[19], line_E[22]]
        allowed = allowed_E
        for e in line_E:
            if e not in allowed_E:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_E:
        # creating overall variable to be used later in function
        line = line_E

        outside_line = line_F

        eat_line = line_G

        # print("piece in line E")
        a_u_list = []
        index = 0
        allowed_F = [line_F[1], line_F[4], line_F[7], line_F[10], line_F[13], line_F[16], line_F[19], line_F[22]]
        allowed = allowed_F
        for e in line_F:
            if e not in allowed_F:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_F:
        # creating overall variable to be used later in function
        line = line_F

        outside_line = line_G

        eat_line = line_H


        # print("piece in line F")
        a_u_list = []
        index = 0
        allowed_G = [line_G[1], line_G[4], line_G[7], line_G[10], line_G[13], line_G[16], line_G[19], line_G[22]]
        allowed = allowed_G
        for e in line_G:
            if e not in allowed_G:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_G:
        # creating overall variable to be used later in function
        line = line_G

        outside_line = line_H

        # IMPORTANT-- THIS RAISED AN ERROR-- EAT_LINE was NOT assigned anything (Assign it something that will work)
        eat_line = 'NONE'


        # print("piece in line G")
        a_u_list = []
        index = 0
        allowed_H = [line_H[1], line_H[4], line_H[7], line_H[10], line_H[13], line_H[16], line_H[19], line_H[22]]
        allowed = allowed_H
        for e in line_H:
            if e not in allowed_H:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    elif white_move_piece in line_A:
        # creating overall variable to be used later in function
        line = line_A

        outside_line = line_B

        eat_line = line_C

        # print("piece in line H")
        a_u_list = []
        index = 0
        allowed_B = [line_B[1], line_B[4], line_B[7], line_B[10], line_B[13], line_B[16], line_B[19], line_B[22]]
        allowed = allowed_B
        for e in line_B:
            if e not in allowed_B:
                continue
            if e != '! ' and e != '   ' and e != '' and e != '!':
                # print('spot unavailable.')
                a_u_list.append('unavailable')
            else:
                # print('spot available.')
                a_u_list.append('available')

    # Displaying the location as a row 1-8
    banned = ['!', '! ', '']

    locations = []
    for i in line:
        if i not in banned:
            locations.append(i)
    # print(locations)

    row = 1
    for x in locations:
        if x == white_move_piece:
            captured_row = row
            # print("piece chosen is in row", row)
        row += 1

    # Finding actual indexes in [line](25 characters) that will be changed per move --IMPORTANT --
    counter = 0
    for c in line:
        if c == white_move_piece:
            playable_white_piece_location = counter
        counter += 1

    # print(a_u_list)

    # FINALLY - Telling what options player has diagonally, available or unavailable
    index = captured_row - 1

    if captured_row == 1:
        if a_u_list[index + 1] == 'available':
            MOVE_RIGHT = True
            MOVE_LEFT = False
        else:
            MOVE_RIGHT = False
            MOVE_LEFT = False

    elif captured_row == 8:
        if a_u_list[index - 1] == 'available':
            MOVE_LEFT = True
            MOVE_RIGHT = False
        else:
            MOVE_LEFT = False
            MOVE_RIGHT = False

    elif captured_row == 2 or captured_row == 3 or captured_row == 4 or captured_row == 5 or captured_row == 6 or captured_row == 7:
        if a_u_list[index - 1] == 'available':
            MOVE_LEFT = True
        else:
            MOVE_LEFT = False
        if a_u_list[index + 1] == 'available':
            MOVE_RIGHT = True
        else:
            MOVE_RIGHT = False

    # Motion
    left_move_loc = playable_white_piece_location - 3
    right_move_loc = playable_white_piece_location + 3

    # eat LOCATION possibilities
    eat_left_loc = playable_white_piece_location - 6
    eat_right_loc = playable_white_piece_location + 6

    # Checking left and right move location in outside_line- to determine if an eat is possible
    # Making sure that the landing spot is actually on the board
    if eat_left_loc >= 1:
        SKIP_L = False
    else:
        SKIP_L = True
        EAT_LEFT = False

    if eat_line != 'NONE':
        if not SKIP_L:
            if outside_line[left_move_loc] in black_pieces and eat_line[eat_left_loc] == '   ':
                EAT_LEFT = True
                MOVE_LEFT = False
            else:
                EAT_LEFT = False
    else:
        EAT_LEFT = False
        EAT_RIGHT = False

    # Making sure that the landing spot is actually on the board
    if eat_right_loc <= 22:
        SKIP_R = False
    else:
        SKIP_R = True
        EAT_RIGHT = False

    if eat_line != 'NONE':
        if not SKIP_R:
            if outside_line[right_move_loc] in black_pieces and eat_line[eat_right_loc] == '   ':
                EAT_RIGHT = True
                MOVE_RIGHT = False
            else:
                EAT_RIGHT = False
    else:
        EAT_RIGHT = False
        EAT_LEFT = False

    print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
    print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)

    # Getting possible eaten locations
    if EAT_LEFT:
        for element in black_pieces:
            if element == outside_line[left_move_loc]:
                possible_left_eaten_piece = element
    if EAT_RIGHT:
        for element in black_pieces:
            if element == outside_line[right_move_loc]:
                possible_right_eaten_piece = element
    # Moving the piece

    direction = input("Which way, (l)eft or (r)ight, would you like to move? > ")
    while direction != 'l' and direction != 'r':
        direction = input("Type 'l' or 'r' > ")

    eat_left_executed = False
    eat_right_executed = False

    # Move sequence
    print("double jump: ", DOUBLE_JUMP)

    if not DOUBLE_JUMP:
        if direction == 'l' and MOVE_LEFT:
            outside_line[left_move_loc] = white_move_piece
            line[playable_white_piece_location] = '   '

        elif direction == 'r' and MOVE_RIGHT:
            outside_line[right_move_loc] = white_move_piece
            line[playable_white_piece_location] = '   '

    # Eat sequence

    if direction == 'l' and EAT_LEFT:
        # Placing piece on new position
        eat_line[eat_left_loc] = white_move_piece
        # Finding the landing location to use for double jump
        landing_location = eat_line[eat_left_loc]
        # putting space where piece used to be
        line[playable_white_piece_location] = '   '
        # removing opposing piece off board and from list
        outside_line[left_move_loc] = '   '
        black_pieces.remove(possible_left_eaten_piece)
        # making a variable to track what happened
        eat_left_executed = True

    if direction == 'r' and EAT_RIGHT:
        # Placing piece on new position
        eat_line[eat_right_loc] = white_move_piece
        # Finding the landing location to use for double jump
        landing_location = eat_line[eat_right_loc]
        # putting space where piece used to be
        line[playable_white_piece_location] = '   '
        # removing opposing piece off board and from list
        outside_line[right_move_loc] = '   '
        black_pieces.remove(possible_right_eaten_piece)
        # making a variable to track what happened
        eat_right_executed = True

    # Pulling move_right and move_left out of the function to use later
    return (MOVE_RIGHT, MOVE_LEFT, playable_white_piece_location, outside_line, line, eat_line, captured_row, EAT_LEFT,
            EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed)


# MAIN GAME LOOP
WIN = False
current_player = 'black'

while not WIN:
    DOUBLE_JUMP = False
    if current_player == 'black':

        (black_move_piece) = ask_black()
        (MOVE_RIGHT, MOVE_LEFT, playable_black_piece_location, outside_line, line, eat_line, captured_row, EAT_LEFT,
         EAT_RIGHT, landing_location, eat_left_executed, eat_right_executed) = find_black_piece()
        # telling player if they chose a piece that cant be moved - TEMPORARY
        print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
        print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)
        print(landing_location)
        if EAT_LEFT or EAT_RIGHT:
            possible_eat = True
        else:
            possible_eat = False

        if MOVE_RIGHT or MOVE_LEFT:
            possible_move = True
        else:
            possible_move = False

        while not possible_move and not possible_eat:
            print("INVALID.")
            (black_move_piece) = ask_black()
            (MOVE_RIGHT, MOVE_LEFT, playable_black_piece_location, outside_line, line, eat_line,
             captured_row, EAT_LEFT, EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed) = find_black_piece()
            if EAT_LEFT or EAT_RIGHT:
                possible_eat = True
            else:
                possible_eat = False

            if MOVE_RIGHT or MOVE_LEFT:
                possible_move = True
            else:
                possible_move = False

        print_board()

        # Asking user if they are finished their move
        done_move = input("Are you done your move? (y/n) > ")
        while done_move != 'y' and done_move != 'n':
            done_move = input("Type 'y' or 'n' > ")

        if eat_left_executed or eat_right_executed:
            eat_executed = True
        else:
            eat_executed = False

        if done_move == 'n' and eat_executed:
            # Checking for double jump -- all standard move instances MUST BE FALSE
            landing_location = black_move_piece
            DOUBLE_JUMP = True

            (MOVE_RIGHT, MOVE_LEFT, playable_black_piece_location, outside_line, line, eat_line, captured_row,
             EAT_LEFT, EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed) = find_black_piece()
            MOVE_LEFT = False
            MOVE_RIGHT = False
            # telling player if they chose a piece that cant be moved - TEMPORARY
            print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
            print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)

            print_board()

        current_player = 'white'

    elif current_player == 'white':

        (white_move_piece) = ask_white()
        (MOVE_RIGHT, MOVE_LEFT, playable_white_piece_location, outside_line, line, eat_line, captured_row, EAT_LEFT,
         EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed) = find_white_piece()
        # telling player if they chose a piece that cant be moved - TEMPORARY
        print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
        print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)
        print(landing_location)
        if EAT_LEFT or EAT_RIGHT:
            possible_eat = True
        else:
            possible_eat = False

        if MOVE_RIGHT or MOVE_LEFT:
            possible_move = True
        else:
            possible_move = False

        while not possible_move and not possible_eat:
            print("INVALID.")
            (white_move_piece) = ask_white()
            (MOVE_RIGHT, MOVE_LEFT, playable_black_piece_location, outside_line, line, eat_line,
             captured_row, EAT_LEFT, EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed) = find_white_piece()
            if EAT_LEFT or EAT_RIGHT:
                possible_eat = True
            else:
                possible_eat = False

            if MOVE_RIGHT or MOVE_LEFT:
                possible_move = True
            else:
                possible_move = False

        print_board()

        # Asking user if they are finished their move
        done_move = input("Are you done your move? (y/n) > ")
        while done_move != 'y' and done_move != 'n':
            done_move = input("Type 'y' or 'n' > ")

        if eat_left_executed or eat_right_executed:
            eat_executed = True
        else:
            eat_executed = False

        if done_move == 'n' and eat_executed:
            # Checking for double jump
            landing_location = white_move_piece
            DOUBLE_JUMP = True

            (MOVE_RIGHT, MOVE_LEFT, playable_white_piece_location, outside_line, line, eat_line, captured_row,
             EAT_LEFT, EAT_RIGHT, landing_location, eat_right_executed, eat_left_executed) = find_white_piece()
            MOVE_LEFT = False
            MOVE_RIGHT = False
            # telling player if they chose a piece that cant be moved - TEMPORARY
            print('eat left: ', EAT_LEFT, 'eat right: ', EAT_RIGHT)
            print('move left: ', MOVE_LEFT, 'move right: ', MOVE_RIGHT)

            print_board()

        current_player = 'black'
