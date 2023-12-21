# use these () brackets in Tuple
names = ('arsh', 'gopi', 'baljeet')
print(names)

# We cannot change values in tuple (for example)
#  names[0] = 'deep'
#  print(names)

# Looping 
for i in names:
    print(i)

# Over Write
print("orginal names:")
for i in names:
    print(i)
names = ('deep', 'preet', 'jeet')
print("new names:")
for i in names:
    print(i)