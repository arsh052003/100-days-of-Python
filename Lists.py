fruits = ['apple', 'banana', 'organe', 'pineapple']
print(fruits)

#Accessing elements in a list
print(fruits[2])
#capitalize the first alphabet of elements at 1 index
print(fruits[1].title())

#Display the last element of list, start from right to left
print(fruits[-1])

# using individual values from lists
message = "My favourite fruit is " + fruits[0].title() + "."
print(message)

# Changing, adding, and removing elements:

# Modifying element in a list
fruits[3] = 'grape'
print(fruits)

# Adding element in a list (append)
fruits.append('pineapple')
print(fruits)

# Insert elements in a list (insert)
fruits.insert(1, 'kiwi')
print(fruits)

# Removing element in a list (remove)
fruits.remove('grape')
print(fruits)

# Removing the element in a list with index (del)
del fruits[0]
print(fruits)

# Pop (remove the last item in a list, but it lets you work with that item after removing it.)
poped_item = fruits.pop()
print(fruits)
print(poped_item)

print("I don’t like  " + poped_item.title() + ".")

# Organizing a list (sort)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Reverse the list (reverse)
cars.reverse()
print(cars)

# Convert the set of number into list
num = list(range(1,9))
print(num)
# To skip num in a given range(e.g. 2)add 2 repeatedly until it reaches or passes the end value, 11.
num = list(range(0,11,2))
print(num)

# Square of 1-10 in list
squares = []
for i in range(1,11):
    square = i**2
    squares.append(square) # squares.append(i**2) more concise
print(squares)

# List Comprehensions (one line code)
squares = [i**2 for i in range(1,11)]
print(squares)

# Slicing a list (start from 0 through 3 ( 0, 1, 2))
# [2:] start from 2 to end of the list
# [:3] start from 0 through 3 (0, 1, 2)
print(cars[0:3])

# Looping through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
for i in players[3:]:
    print(i)