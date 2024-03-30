# Loops: Used to repeat instructions

# While Loop
# Print Hello 5 times
num = 1
while num <= 5:
    print("Hello World")
    num += 1

# Print number from 1 to 5
numm = 1
while numm <= 5:
    print(numm)
    numm += 1


# Break and Continue

# Break: Used to terminate a loop when encountered.
# Continue: Terminates execution in the current iteration and continues execution of the loop with the next iteration
    
# Using Continue
i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue    # acts as skip
    print(i)
    i += 1


j = 0
while j <= 10:
    if(j % 2 == 0):
        j += 1
        continue
    print(j)
    j += 1

# Printing odd numbers, if you want to print the even number then we can just add != to it