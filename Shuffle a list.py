# Creating a function that, given a list, shuffles it randomly and returns new shuffled list
# (might already be a method, but still good to think through the problem)
import random

letters = ['a', 'b', 'c', 'd', 'e']

'''
def shuffle_list(list1):
    # defining list that will be returned
    shuffled_list = list1
    # defining list that keeps track of used indexes
    used_indexes = []
    # creating a loop which will take each element of list1, assign random integer to it, then place in shuffled_list
    for x in list1:
        print(used_indexes)
        index = random.randrange(0, len(list1))
        if index in used_indexes:
            while index in used_indexes:
                index = random.randrange(0, len(list1))
        else:
            pass
        # assuring same index is not used more than once
        used_indexes.append(index)
        shuffled_list[index] = x
    # shuffled list should be complete by now
    print(shuffled_list)
    return shuffled_list


# testing
shuffle_list(letters)'''


# different approach
random_integers = list(range(0, len(letters)))
random.shuffle(random_integers)
print(random_integers)

counter = 0
new_list = letters
for x in letters:
    letters[random_integers[counter]] = x
    counter += 1

print(letters)








