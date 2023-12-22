

def won():
    print("You win!")
    play_again = input("Play again? (yes / no): ")
    play_again = play_again.lower()
    return (play_again)

a = won()
print(a, a)

