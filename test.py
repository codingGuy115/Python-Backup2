# Quadratic Formula: -b +- root(b^2 - 4ac)
#                    ---------------------
#                              2a
#import math

#print(math.sqrt(9))

# Checking whether using whole numbers or decimals + gathering base number data for later usage
#operation = input("Are you using whole numbers or decimals? Type 'whole' or 'deci': ")
#if operation.lower() == 'whole':
#    a = int(input("a= "))
#    b = int(input("b= "))
#    c = int(input("c= "))

#elif operation.lower() == 'deci':
#    a = float(input("a= "))
#    b = float(input("b= "))
#    c = float(input("c= "))


# Calculations part

#neg_b = b * -1

#b_squared = b ^ 2

#four_ac = 4 * (a*c)

#quantity = b_squared - four_ac

#root = math.sqrt(quantity)

#two_a = a * 2

#top1 = neg_b + root
#top2 = neg_b - root

#answer1 = top1 / two_a
#answer2 = top2 / two_a

#print("Answer 1:", answer1, " Answer 2:", answer2)
# Doesnt work so far, might have to research the 'math' library a bit more to understand capabilities/rules.

# -------------------------------------------------------------------------------------------------------------

# Open new window using tkinter
#from tkinter import *

#def create_window():
#    new_window = Tk()
#    old_window.destroy()

#old_window = Tk()

#Button(old_window, text="create new window", command=create_window).pack()

#old_window.mainloop()
# ---------------------------------------------------------------------------------------------------------------
#

'''
import pygame
import sys
from pygame.locals import *


def main():

    pygame.init()

    white = (255, 255, 255)
    black = (0, 0, 0)

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
    DISPLAY.fill(white)


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()'''

line_A = ['a', 'b', 'c']
line_B = ['d', 'e', 'f']

lines = [line_A, line_B]

selection = input("Choose letter: ")

for e in lines:
    if selection in e:
        print("Letter in line", e)

