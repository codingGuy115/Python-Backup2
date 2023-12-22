# Test file


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

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

# IMPORTANT -- Tried and tested - works and gives the indexes for each letter in alphabet from message
while message_length != 0:

    for letter in alphabet:
        if counter == 26:
            #print('counter reached 26')
            counter = 0
        if index == 26:
            #print('index reached 26')
            index = 0

        if letter == message[counter]:
            #print(message[counter], 'at index: ', index, 'in the alphabet.')
            message_index_locations.append(index)

            #print('index: ', index)

        index += 1
    counter += 1

    message_length -= 1

#print(message_index_locations)

# Taking the indexes and building an encrypted message
for i in message_index_locations:
    number = i
    # removing index location in sequential order
    message_index_locations.remove(message_index_locations[0])
    # Check
    print('message index locations: ', message_index_locations)
    compiled = number + key
    # Check
    print('compiled: ', compiled)

    if compiled > message_length:
        compiled = compiled - message_length
        print(alphabet[compiled])
    else:
        print(alphabet[compiled])

