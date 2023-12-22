# Nick de Rezende - Hangman game w/ crude visuals - 7/17/22

import random

gallows_display = [[' ', ' ', '+', '-', '-', '-', '+'],
                   [' ', ' ', 'V', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', 'U']]


# function to display the gallows along with body parts as game progresses
def print_gallows():
    for x in gallows_display:
        print(''.join(x))


# function for choosing a random word
def choose_word():
    word_bank = ['apple']
    word = random.choice(word_bank)
    return word


# function for converting the randomly generated word into list_display
def word_to_display(a):
    display_word_key = []
    display_word_key[:0] = a
    counter = 0
    display_word = display_word_key
    for x in display_word:
        display_word[counter] = '_'
        counter += 1
    return display_word, display_word_key


# function to print the display_word as it is updated throughout the game
def print_display_word(b):
    print('          ' + ' '.join(b))


# function to ask for a letter input
def ask_letter():
    guess = input('Guess a letter: ')
    while len(guess) > 1:
        guess = input('Guess a SINGLE letter: ')
    guess = guess.lower()
    return guess


# function to determine if guess in word, returns true or false
def check_guess(c):
    correct = True
    if c in word:
        correct = True
    else:
        correct = False
    return correct


# Function to replace underscore with correct letter / letters
def fill_blanks(d):
    index = 0
    for x in word:
        if x == d:
            display_word[index] = d
        index += 1
    return display_word


# Function to add body part to gallows if guess is wrong


# Main function to encompass everything
def main():
    running = True
    while running:
        print_gallows()
        word = choose_word()
        print_display_word(word)
        # ask for user guess
        guess = ask_letter()
        correct = True
        if guess in word:
            correct = True
        else:
            correct = False
        if correct:
            # this updates the current display word
            display_word = fill_blanks(guess)
        else:
            print('body part added.')


main()

