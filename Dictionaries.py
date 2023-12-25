products = {'face' : 'cleanser', 'hand' : 'cream'}
#print(products['face']) 
print("You just earned " + products['face'] + " points!")

# Modifying values:
print("The product is " + products['hand'] + ".")
products = {'hand' : 'santizier'}
print("Yhe new hand product is " + products['hand'] + ".")

alien = {'x_position' : 0, 'y_position' : 25, 'speed': 'medium'}
print("orginal x-position: " + str(alien['x_position']))

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 3
else:
    x_increment = 5
# assign the final result into variable
alien['x_position'] = alien['x_position'] + x_increment
#print result
print("new_position: " + str(alien['x_position']))

# LOOPING, and print all the items of the current dictionary (.items())
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite language is " + languages.title())

print("Use key function")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!" )

# Sorted Dictionaries:
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values
print("The following languages have been mentioned:")
for languages in favorite_languages.values():
    print(languages.title())

#Nested 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# empty list for storing aliens
aliens = []
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# Modify the dictionary with loop 
print("____________")
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

#show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("....")
print("Total number of aliens: " + str(len(aliens)))

# List in a Dictionary