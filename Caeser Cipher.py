# Nick de Rezende 12/25/21

# Intro
print("""This is the Caesar Cipher. It will take a message consisting of letters and spaces ONLY and change each letter to a different character by cycling 
through the alphabet a set number of times. This is the cipher KEY. It will then return the encrypted message.
____________________________________________________________________________________________________________""")
'''
# Creating an alphabet to use later'''
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
'''alphabet_length = len(alphabet)

# Getting the string from the user
message = str(input("Enter the message you would like to encrypt: "))
message = message.upper()

message_length = len(message)

print(message[0])

# Determining the key
key = int(input("Enter key for message encryption (1-26): "))
while key not in range(1, 27, 1):
    key = int(input("Please enter a valid key (1-26): "))
'''

# Finding the index locations of the message letters IN the alphabet


def find_alphabet_locations(message, counter, index, message_index_locations):
    if counter == 25:
        counter = 0
    if index == 25:
        index = 0
    for letter in alphabet:
        if letter == message[counter]:
            print(message[counter], 'at index: ', index, 'in the alphabet.')
            index = str(index)
            message_index_locations += index
            index = int(index)

            print('index: ', index)

        index += 1
    return message, counter, index, message_index_locations



def main():
    # Creating an alphabet to use later
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    alphabet_length = len(alphabet)

    # Getting the string from the user
    message = str(input("Enter the message you would like to encrypt: "))
    message = message.upper()

    message_length = len(message)

    # Determining the key
    key = int(input("Enter key for message encryption (1-26): "))
    while key not in range(1, 27, 1):
        key = int(input("Please enter a valid key (1-26): "))

    message_index_locations = []
    index = 0
    counter = 0
    while message_length != 0:
        # initializing counter back to zero once it gets to the end of the alphabet
        if counter == 25:
            counter = 0
        if index == 25:
            index = 0

        message, counter, index, message_index_locations = find_alphabet_locations(message, counter, index, message_index_locations)
        message_length -= 1
        counter += 1
    print(message_index_locations)


main()

