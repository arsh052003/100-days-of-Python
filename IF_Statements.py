cars = ['audi', 'bmw', 'subaru', 'toyota']
for i in cars:
    if i == 'bmw':
        print(i.upper())
    else:
        print(i)

#While Loop
i = 1
while(i <= 10):
    print(i)
    i += 1



# While Loop
n = int(input("Enter the number: "))
i = 1
while(i<=n):
    j = 1
    while(j<=i):
        print(j, end = ' ')
        j+=1
    print( )
    i+=1

#For loop
print("enter number: ")
i = 1
for i in range(1,6):
    for j in range(1,i+1):
       print(j, end = ' ')
    print("")     