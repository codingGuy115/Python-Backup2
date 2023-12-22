# Try to get the functions win() lose() and tie() to work- might be interesting
import random
import sys

running = input("Would you like to play rock paper scissors? ")
running = running.upper()

# Valid input checker
while running != 'YES' and running != 'NO':
    running = input("Please type 'yes' or 'no': ")
    running = running.upper()

# This is the overall loop controller
if running == 'YES':
    running = True
else:
    running = False

# Creating list of choices for both computer and player
choices = ['rock', 'paper', 'scissors']


play_again = ''
# initializing round and player win counter to zero for easier use
round_counter = 0
player_win_count = 0

# Making the main game loop
while running:
    # Creating functions in order to eliminate repeated code

    def tied():
        print("It's a tie.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        return


    def lost():
        print("You lost.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        return


    def won():
        print("You win!")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        return (play_again)

    a = won()
    print(a)



    player = input("Choose rock, paper, or scissors: ")
    player = player.lower()

    # making sure choice is valid
    while player not in choices:
        player = input("Sorry that is not an option. Choose rock, paper, or scissors: ")
        player = player.lower()

    # Computer's move
    computer = random.choice(choices)
    print("Computer:", computer)

    # Logic
    if player == 'rock' and computer == 'rock':
        print("It's a tie.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()

    elif player == 'rock' and computer == 'paper':
        print("You lose.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1

    elif player == 'rock' and computer == 'scissors':
        print(a)
        '''print("You win!")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1
        player_win_count += 1'''

    elif player == 'paper' and computer == 'rock':
        print("You win!")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1
        player_win_count += 1

    elif player == 'paper' and computer == 'paper':
        print("It's a tie.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()

    elif player == 'paper' and computer == 'scissors':
        print("You lose.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1

    elif player == 'scissors' and computer == 'rock':
        print("You lose.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1

    elif player == 'scissors' and computer == 'paper':
        print("You win!")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()
        round_counter += 1

    elif player == 'scissors' and computer == 'scissors':
        print("It's a tie.")
        play_again = input("Play again? (yes / no): ")
        play_again = play_again.lower()

    # checking for play_again == 'no'
    if play_again == 'no':
        print("You won", player_win_count, "out of", round_counter, '.')
        running = False
    else:
        running = True

