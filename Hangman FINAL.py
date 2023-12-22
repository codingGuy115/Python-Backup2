# This will be the final file for the hangman game, building from the ground up

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


# Function to reset gallows once new word is generated
def reset_gallows(a):
    a = [[' ', ' ', '+', '-', '-', '-', '+'],
                   [' ', ' ', 'V', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', '|'],
                   [' ', ' ', ' ', ' ', ' ', ' ', 'U']]
    return a


# function for choosing a random word
def choose_word():
    word_bank = ['apple', 'pear']
    word = random.choice(word_bank)
    return word


# function to show the blanks updated throughout the game
def print_display_word(display_word):
    print('          ' + ' '.join(display_word))


# Function to ask for letter that user enters
def ask_letter():
    guess = input('Guess a letter: ')
    while len(guess) > 1:
        guess = input('Guess a SINGLE letter: ')
    guess = guess.lower()
    return guess


# Function that asks user if they want to continue the game
def ask_continue():
    cont_game = input('Keep playing? (Y/N): ')
    while cont_game.lower() != 'y' and cont_game.lower() != 'n':
        cont_game = input('''Type 'y' or 'n' : ''')
    if cont_game == 'y':
        continue_game = True
    else:
        continue_game = False
    return continue_game


# Function to generate a new word after player chooses to play again
def generate_new_word():
    word = choose_word()
    display_word_key = []
    display_word_key[:0] = word
    counter = 0
    display_word = display_word_key
    for x in display_word:
        display_word[counter] = '_'
        counter += 1
    return word, display_word


# GAME LOGIC STARTS HERE
def main():
    # choosing word to start off the game
    word = choose_word()
    display_word_key = []
    display_word_key[:0] = word
    counter = 0
    display_word = display_word_key
    for x in display_word:
        display_word[counter] = '_'
        counter += 1

    # starting loop
    lives = 6
    continue_game = True
    while continue_game:
        print_gallows()
        print_display_word(display_word)
        guess = ask_letter()
        correct = True
        if guess in word:
            correct = True
        else:
            correct = False

        # Filling in the blanks
        index = 0
        for x in word:
            if x == guess:
                display_word[index] = guess
            index += 1
        # Checking to make sure that they did not win
        win = False
        for i in display_word:
            if i == '_':
                win = False
            else:
                win = True
        if win:
            print_gallows()
            print_display_word(display_word)
            print('You win!')
            continue_game = ask_continue()
            # able to generate new word here- due to fact that game will end if continue_game becomes false
            word, display_word = generate_new_word()
            lives = 6

        if not correct:
            # Drawing the body part
            if lives == 0:
                gallows_display[4][3] = 'L'
                print_gallows()
                print('You lose. The word was ', word, '.')
                continue_game = ask_continue()
                # able to generate new word here- due to fact that game will end if continue_game becomes false
                word, display_word = generate_new_word()
                lives = 6
            else:
                lives -= 1
                if lives == 5:
                    gallows_display[2][2] = 'o'
                elif lives == 4:
                    gallows_display[3][2] = '|'
                elif lives == 3:
                    gallows_display[3][1] = '-'
                elif lives == 2:
                    gallows_display[3][3] = '-'
                elif lives == 1:
                    gallows_display[4][1] = '/'
                elif lives == 0:
                    gallows_display[4][3] = 'L'
                    print_gallows()
                    print('You lose. The word was ', word, '.')
                    continue_game = ask_continue()
                    # able to generate new word here- due to fact that game will end if continue_game becomes false
                    word, display_word = generate_new_word()
                    lives = 6


main()

