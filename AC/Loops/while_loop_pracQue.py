# Print numbers from 1 to 100
num = 1
while num <= 5:
    print(num)
    num += 1


# Print numbers from 100 to 1
numm = 5
while numm >= 1:
    print(numm)
    numm -= 1


# Print multiplication table of a number n
count = 1
mul = int(input("Enter the number: "))
while count <= 10:
    print(mul * count)
    count += 1

# Print the element of the following list using a loop
index = 0
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# while index < len(list):
#     print(list[index])
#     index += 1


# Search for a number x in this tuple using loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number you want to search: "))
while index < len(tup):
    if(x == tup[index]):
        print("Found at index:", index)
    index += 1


# Write a program to find the sum of first n numbers
sum = 0
i = 1
n = int(input("Enter the number: "))
while i <= n:
    sum += i
    i += 1
print("Sum of first", n, "natural numbers is:", sum)


# Write a program to find the factorial of the nnumber
factorial = 1
counter = 1
number = int(input("Enter the number: "))
if(number < 0):
    print("Factorial is not defined")
elif(number == 0):
    print("Factorial = 1")
elif(number == 1):
    print("Factorial = 1")
else:
    while counter <= number:
        factorial += counter
        counter += 1

    print("Factorial of", number, "is:", factorial)