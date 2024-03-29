# Write a program to input user's first name and print its length
firstName = str(input("Enter the first name: "))
print(len(firstName))

# Write a program to find occurence of '$' in a string
str = "Vyom earns $120000 per annum and spends $60000 every year"
print(str.find("$")) # Found '$' at index 11
print(str.count("$")) # Found '$' two times

# Write a program to check if the number entered is even or odd
numberOne = int(input("Enter the number: "))
if(numberOne % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# Write a program to find the greatest of 3 number entered by the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if(a >= b and a >= c):
    largest = "First number"
elif(b >= a and b >= c):
    largest = "Second number"
else:
    largest = "Third number"
print(largest, "is the largest one.")

# Write a program to check if the number is a multiple of 7 or not
numberTwo = int(input("Enter the number: "))
if(numberTwo % 7 == 0):
    print("Yes, it is multiple of 7")
else:
    print("No, it is not multiple of 7")