# Nick de Rezende -- Tic Tac Toe game with visuals using PyGame package -- taking tic tac toe logic and modifying

'''
# drawing a circle
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((225, 225, 225))
    pygame.draw.circle(screen, (0, 0, 225), (250, 250), 75)

    pygame.display.flip()
pygame.quit()'''
'''
# MousePosition and click detection example
from sys import exit
import pygame
pygame.init()

WIDTH = HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crash!')

# Draw Once
rectangle = pygame.draw.rect(window, (255, 0, 0), (100, 100, 100, 100))
pygame.display.update()

# Main Loop
while True:
    # Mouse position and button clicking
    pos = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

    # Check if rectangle collided with pos and if the left mouse button was pressed
    if rectangle.collidepoint(pos) and pressed1:
        print("You have opened a chest!")

    # Quit pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
'''

# Writing a message on the display
'''import pygame

# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.
text = font.render('GeeksForGeeks', True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

# set the center of the rectangular object.
textRect.center = (X // 2, Y // 2)

# infinite loop
while True:

    # completely fill the surface object
    # with white color
    display_surface.fill(white)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()'''

# Drawing a square wherever cursor is clicked
'''import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((800, 500))

class Cube:
    def update(self):
        self.cx, self.cy = pygame.mouse.get_pos()
        self.square = pygame.Rect(self.cx, self.cy, 50, 50)

    def draw(self): 
        pygame.draw.rect(screen, (255, 0, 0), self.square)

cube = Cube()
drawing_cube = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cube.update()
            drawing_cube = True     

    screen.fill((0, 255, 0))
    if drawing_cube:
        cube.draw()
    pygame.display.flip()


pygame.quit()
quit()'''


import pygame
import sys
from pygame.locals import *


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)


# functions to display whose turn it is
#    def ask_player1():

#    def ask_player2():



    DISPLAY.fill(white)
# ----------------------------------( distance from left side, distance from top, length, width)
    # Vertical lines
    pygame.draw.rect(DISPLAY, black, (165, 50, 10, 300))
    pygame.draw.rect(DISPLAY, black, (285, 50, 10, 300))
    # Horizontal lines
    pygame.draw.rect(DISPLAY, black, (80, 135, 300, 10))
    pygame.draw.rect(DISPLAY, black, (80, 250, 300, 10))

    # Creating spaces to be clicked on by mouse
    TL = pygame.draw.rect(DISPLAY, green, (80, 50, 78, 78))
    ML = pygame.draw.rect(DISPLAY, green, (80, 160, 78, 78))
    BL = pygame.draw.rect(DISPLAY, green, (80, 270, 78, 78))

    TC = pygame.draw.rect(DISPLAY, green, (190, 50, 78, 78))
    MC = pygame.draw.rect(DISPLAY, green, (190, 160, 78, 78))
    BC = pygame.draw.rect(DISPLAY, green, (190, 270, 78, 78))

    TR = pygame.draw.rect(DISPLAY, green, (302, 50, 78, 78))
    MR = pygame.draw.rect(DISPLAY, green, (302, 160, 78, 78))
    BR = pygame.draw.rect(DISPLAY, green, (302, 270, 78, 78))

    while True:
        for event in pygame.event.get():
            # using two parts to the variable since the 'get_pos()' returns x and y values
            px, py = pygame.mouse.get_pos()
            # fixed position
            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0]
            valid_moves = ['TL', 'TC', 'TR', 'ML', 'MC', 'MR', 'BL', 'BC', 'BR']

            def draw_x():
                pygame.draw.rect(DISPLAY, red, (px, py, 40, 40))
                return

            def draw_y():
                pygame.draw.circle(DISPLAY, red, (30, 100), 20)
                return

            if event.type == QUIT:
                pygame.quit()
                sys.exit()


# Checking which boxes are clicked on by mouse cursor and making sure only can be clicked on once
# Make it so each can only happen ONCE
            #if 'TL' in valid_moves and TL.collidepoint(mouse_position) and mouse_pressed:
            if 'TL' in valid_moves and TL.collidepoint(mouse_position) and mouse_pressed:
                print("You clicked on the top left box")
                pygame.draw.rect(DISPLAY, red, (100, 70, 40, 40))
                valid_moves.remove('TL')
                print(valid_moves)

            elif ML.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the middle left box")
                pygame.draw.rect(DISPLAY, red, (100, 180, 40, 40))

            elif BL.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the bottom left box")
                pygame.draw.rect(DISPLAY, red, (100, 290, 40, 40))

            elif TC.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the top center box")
                pygame.draw.rect(DISPLAY, red, (210, 70, 40, 40))

            elif MC.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the middle center box")
                pygame.draw.rect(DISPLAY, red, (210, 180, 40, 40))

            elif BC.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the bottom center box")
                pygame.draw.rect(DISPLAY, red, (210, 290, 40, 40))

            elif TR.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the top right box")
                pygame.draw.rect(DISPLAY, red, (322, 70, 40, 40))

            elif MR.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the middle right box")
                pygame.draw.rect(DISPLAY, red, (322, 180, 40, 40))

            elif BR.collidepoint(mouse_position) and mouse_pressed and MOUSEBUTTONUP:
                print("You clicked on the bottom right box")
                pygame.draw.rect(DISPLAY, red, (322, 290, 40, 40))

        pygame.display.update()


main()


'''
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
            player1_move = input("That is not a valid move. Please type one of the following")
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
    print("GAME ENDED IN A TIE.")'''
