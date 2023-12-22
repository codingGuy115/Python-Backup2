#Nick de Rezende -- Hangman Game Legitimate

#print("Welcome to Legitimate Hangman!")

import random

animals = ['dog', 'cat', 'hamster', 'horse', 'dolphin', 'whale', 'tiger']
places = ['america', 'europe', 'asia', 'australia', 'antarctica']

word = random.choice(animals + places)
print(word)

#giving number of checks
if len(word) == 3:
    checks = 3
elif len(word) == 4:
    checks = 4
elif len(word) == 5:
    checks = 5
elif len(word) == 6:
    checks = 6
elif len(word) == 7:
    checks = 7
elif len(word) == 8:
    checks = 8
elif len(word) == 9:
    checks = 9
elif len(word) == 10:
    checks = 10

#Making while loop for checking system
while checks <= len(word):
    checks = checks-1
    if checks == -1:
        break
    guess = input("Give letter:")
    if guess in word:
        print("Correct.")
    else:
        print("wrong.")
print("Loop ended")

#Final Chance part
fguess = input("You're out of guesses. What do you think the word was? :")
if fguess.lower() == word:
    print("Yay! You win! The word was", word, 'and you said', fguess.lower())
else:
    print("You lose.")
