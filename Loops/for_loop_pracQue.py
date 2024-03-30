# Print the elements of the list using a for loop
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)


# Search for a number x in the tuple using a for loop
index = 0
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = int(input("Enter the number: "))
for num in tup:
    if(num == x):
        print("Element found at:", index, "index")
    index += 1


# Write a program to find the factorial of number n