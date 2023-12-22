# For Loops examples and concepts

#fruits = ["apple", "banana", "pear"]

#for element in fruits:      # This says 'for each element in fruits, print each element
#    print(element)

# finding the sum
#b = [20, 10, 5]
#total = 0
#for e in b:
#    total = total + e
#print(total)

# finding the sum using range

#total2 = 0
#c = list(range(1, 5))
#print(c)
#for i in range(1, 5):
#    total2 += 1
#print(total2)

# checking whether numerical data is a multiple of something

#total3 = 0
#for i in range(1, 8):
#    if i % 3 == 0:
#        total3 += i
#print(total3)

# counting all the multiples of 3 and 5 that are less than 100

total = 0
for i in list(range(1, 100)):
    if i % 3 == 0 or i % 5 == 0:
        total += 1
print(total)
