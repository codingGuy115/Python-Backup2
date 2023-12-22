# This is a model of the famous Collatz, or '3x+1' conjecture
# If an integer is even, divide by 2
# If an integer is odd, add 1

import sys
print("This is the Collatz Conjecture. Essentially, if a number is odd, iterate to 3x+1. If it is even, divide by 2. The goal is to find a whole integer that does not get to '1, -1, -5'. Good luck!")
n = int(input("Enter any whole number other than 1, -1, -17 and -5: "))
# Valid checker
#while number != int:
#    number = int(input("You have to enter a positive whole number for this to work: "))

# Logic/Main loop
iterations = 0
# Negative number checker
if n < 0:
    while n != -1 and n != -5 and n != -17:
        if (n % 2) == 0:
            n = n / 2
            n = int(n)
            print(n)
            iterations += 1
        else:
            n = (3 * n) + 1
            n = int(n)
            print(n)
            iterations += 1
    print("Iterations:", iterations)
    sys.exit()

while n != 1:
    # Checks if number is even
    if (n % 2) == 0:
        n = n/2
        n = int(n)
        print(n)
        iterations += 1
    else:
        n = (3 * n) + 1
        n = int(n)
        print(n)
        iterations += 1
print("Steps:", iterations)

# If it somehow works
if n != 1 and n != -1 and n != -5 and n != -17:
    print("You have just solved a problem that has plagued mathematicians for ages.")
