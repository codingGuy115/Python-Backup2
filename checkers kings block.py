# This file is meant to serve as a sandbox for writing the KING code

import sys

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


# Simulating the input
black_move_piece = input("Black's turn. Which piece? : ")

# Finding the king piece
black_pieces = ['B_1', 'B_2', 'B_3', 'B_4', 'B_5', 'B_6', 'B_7', 'B_8', 'B_9', 'B10', 'B11', 'B12']
white_pieces = ['W_1', 'W_2', 'W_3', 'W_4', 'W_5', 'W_6', 'W_7', 'W_8', 'W_9', 'W10', 'W11', 'W12']

black_king_pieces = ['KB1', 'KB2', 'KB3', 'KB4', 'KB5', 'KB6']
white_king_pieces = ['KW1', 'KW2', 'KW3', 'KW4', 'KW5', 'KW6']

# IMPORTANT
lines = [line_A, line_B, line_C, line_D, line_E, line_F, line_G, line_H]

vertical_direction = input("Would you like to move (u)p or (d)own? ")


def king_move_UP():

    if current_player == 'black':
        king_piece = black_move_piece
        opposing_pieces = white_pieces
    else:
        king_piece = white_move_piece
        opposing_pieces = black_pieces
    for e in lines:
        if king_piece in e:
            king_loc_line = e

    print(king_loc_line)

    # creating overall variable to be used later in function
    line = king_loc_line

    # Finding the king location in the lines list
    finder = 0
    for t in lines:
        if t == line:
            marker = finder
        finder += 1
    print(marker)

    # REMEMBER -- if the king is in line A, there is no outside line or eat line.
    # REMEMBER -- if the king is in line B, there is no eat line.
    if king_loc_line == line_A:
        outside_line = 'NONE'
        eat_line = 'NONE'
    elif king_loc_line == line_B:
        outside_line = lines[marker - 1]
        eat_line = 'NONE'
    else:
        outside_line = lines[marker - 1]
        eat_line = lines[marker - 2]

    # Temp Identifier
    print('line:', line, 'outside line', outside_line, 'eat line', eat_line)

    a_u_list = []
    index = 0
    allowed_line = [line[1], line[4], line[7], line[10], line[13], line[16], line[19], line[22]]
    allowed = allowed_line
    for e in line:
        if e not in allowed_line:
            continue
        if e != '! ' and e != '   ' and e != '' and e != '!':
            a_u_list.append('unavailable')
        else:
            a_u_list.append('available')

    # LOGIC AFTER LINE VALUES FOUND

        # Displaying the location as a row 1-8
        banned = ['!', '! ', '']

        locations = []
        for i in line:
            if i not in banned:
                locations.append(i)
        # print(locations)

        row = 1
        for x in locations:
            if x == king_piece:
                captured_row = row
                # print("piece chosen is in row", row)
            row += 1

        # Finding actual indexes in line that will be changed per move --IMPORTANT --
        counter = 0
        for c in line:
            if c == king_piece:
                playable_king_piece_location = counter
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
        left_move_loc = playable_king_piece_location - 3
        right_move_loc = playable_king_piece_location + 3

        # eat LOCATION possibilities
        eat_left_loc = playable_king_piece_location - 6
        eat_right_loc = playable_king_piece_location + 6

        # Checking left and right move location in outside_line- to determine if an eat is possible
        # Making sure that the landing spot is actually on the board
        if eat_left_loc >= 1:
            SKIP_L = False
        else:
            SKIP_L = True
            EAT_LEFT = False

        if eat_line != 'NONE':
            if not SKIP_L:
                if outside_line[left_move_loc] in opposing_pieces and eat_line[eat_left_loc] == '   ':
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
                if outside_line[right_move_loc] in opposing_pieces and eat_line[eat_right_loc] == '   ':
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
            for element in opposing_pieces:
                if element == outside_line[left_move_loc]:
                    possible_left_eaten_piece = element
        if EAT_RIGHT:
            for element in opposing_pieces:
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
                outside_line[left_move_loc] = king_piece
                line[playable_king_piece_location] = '   '

            elif direction == 'r' and MOVE_RIGHT:
                outside_line[right_move_loc] = king_piece
                line[playable_king_piece_location] = '   '

        # eat sequence

        if direction == 'l' and EAT_LEFT:
            # Placing piece on new position
            eat_line[eat_left_loc] = king_piece
            # Finding the landing location to use for double jump
            landing_location = eat_line[eat_left_loc]
            # putting space where piece used to be
            line[playable_king_piece_location] = '   '
            # removing opposing piece off board and from list
            outside_line[left_move_loc] = '   '
            opposing_pieces.remove(possible_left_eaten_piece)
            # making a variable to track what happened
            eat_left_executed = True

        if direction == 'r' and EAT_RIGHT:
            # Placing piece on new position
            eat_line[eat_right_loc] = king_piece
            # Finding the landing location to use for double jump
            landing_location = eat_line[eat_right_loc]
            # putting space where piece used to be
            line[playable_king_piece_location] = '   '
            # removing opposing piece off board and from list
            outside_line[right_move_loc] = '   '
            opposing_pieces.remove(possible_right_eaten_piece)
            # making a variable to track what happened
            eat_right_executed = True

    return(MOVE_RIGHT, MOVE_LEFT, EAT_RIGHT, EAT_LEFT, landing_location, eat_right_executed, eat_left_executed)



# KING MOVE DOWN-- VERTICAL DIRECTION = d


def king_move_DOWN():
    if current_player == 'black':
        king_piece = black_move_piece
        opposing_pieces = white_pieces
    else:
        king_piece = white_move_piece
        opposing_pieces = black_pieces
    for e in lines:
        if king_piece in e:
            king_loc_line = e

    print(king_loc_line)

    # creating overall variable to be used later in function
    line = king_loc_line

    # Finding the king location in the lines list
    finder = 0
    for t in lines:
        if t == line:
            marker = finder
        finder += 1
    print(marker)

    # REMEMBER -- if the king is in line H, there is no outside line or eat line.
    # REMEMBER -- if the king is in line G, there is no eat line.
    if king_loc_line == line_H:
        outside_line = 'NONE'
        eat_line = 'NONE'
    elif king_loc_line == line_G:
        outside_line = lines[marker + 1]
        eat_line = 'NONE'
    else:
        outside_line = lines[marker + 1]
        eat_line = lines[marker + 2]

    # Temp Identifier
    print('line:', line, 'outside line', outside_line, 'eat line', eat_line)

    a_u_list = []
    index = 0
    allowed_line = [line[1], line[4], line[7], line[10], line[13], line[16], line[19], line[22]]
    allowed = allowed_line
    for e in line:
        if e not in allowed_line:
            continue
        if e != '! ' and e != '   ' and e != '' and e != '!':
            a_u_list.append('unavailable')
        else:
            a_u_list.append('available')

        # LOGIC AFTER LINE VALUES FOUND

        # Displaying the location as a row 1-8
        banned = ['!', '! ', '']

        locations = []
        for i in line:
            if i not in banned:
                locations.append(i)
        # print(locations)

        row = 1
        for x in locations:
            if x == king_piece:
                captured_row = row
                # print("piece chosen is in row", row)
            row += 1

        # Finding actual indexes in line that will be changed per move --IMPORTANT --
        counter = 0
        for c in line:
            if c == king_piece:
                playable_king_piece_location = counter
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
        left_move_loc = playable_king_piece_location - 3
        right_move_loc = playable_king_piece_location + 3

        # eat LOCATION possibilities
        eat_left_loc = playable_king_piece_location - 6
        eat_right_loc = playable_king_piece_location + 6

        # Checking left and right move location in outside_line- to determine if an eat is possible
        # Making sure that the landing spot is actually on the board
        if eat_left_loc >= 1:
            SKIP_L = False
        else:
            SKIP_L = True
            EAT_LEFT = False

        if eat_line != 'NONE':
            if not SKIP_L:
                if outside_line[left_move_loc] in opposing_pieces and eat_line[eat_left_loc] == '   ':
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
                if outside_line[right_move_loc] in opposing_pieces and eat_line[eat_right_loc] == '   ':
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
            for element in opposing_pieces:
                if element == outside_line[left_move_loc]:
                    possible_left_eaten_piece = element
        if EAT_RIGHT:
            for element in opposing_pieces:
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
                outside_line[left_move_loc] = king_piece
                line[playable_king_piece_location] = '   '

            elif direction == 'r' and MOVE_RIGHT:
                outside_line[right_move_loc] = king_piece
                line[playable_king_piece_location] = '   '

        # eat sequence

        if direction == 'l' and EAT_LEFT:
            # Placing piece on new position
            eat_line[eat_left_loc] = king_piece
            # Finding the landing location to use for double jump
            landing_location = eat_line[eat_left_loc]
            # putting space where piece used to be
            line[playable_king_piece_location] = '   '
            # removing opposing piece off board and from list
            outside_line[left_move_loc] = '   '
            opposing_pieces.remove(possible_left_eaten_piece)
            # making a variable to track what happened
            eat_left_executed = True

        if direction == 'r' and EAT_RIGHT:
            # Placing piece on new position
            eat_line[eat_right_loc] = king_piece
            # Finding the landing location to use for double jump
            landing_location = eat_line[eat_right_loc]
            # putting space where piece used to be
            line[playable_king_piece_location] = '   '
            # removing opposing piece off board and from list
            outside_line[right_move_loc] = '   '
            opposing_pieces.remove(possible_right_eaten_piece)
            # making a variable to track what happened
            eat_right_executed = True

    return (MOVE_RIGHT, MOVE_LEFT, EAT_RIGHT, EAT_LEFT, landing_location, eat_right_executed, eat_left_executed)
