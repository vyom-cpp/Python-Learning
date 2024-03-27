# Chapter-2: Strings and Conditional Statements

# String: It is a datatype that stores a sequence of characters

# Concatenation

string = "Vyom" + " Sutariya"
print(string)

# This concatenation can also be done by taking two different strings

# String Length
length = len(string)
print(length)
print(string[5]) # Prints S

# Slicing: Accessing parts of a String
# string[starting_index : ending_index]
# ending_index is not included

str = "Vyom Sutariya"
print(str[2:4]) # om
print(str[:4]) # Vyom; it is same as str[0:4]
print(str[0:]) # Vyom Sutariya; it is same as str[0:len(str)]

# Slicing special case (Negative Indexes)
#  V     y    o    m   ^    S   u   t   a   r   i   y   a
# -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
print(str[-11:-9]) # om

# String Functions
print(str.endswith("ya")) # Return true if string ends with the sub string
print(str.capitalize()) # Capitalizes the 1st character
print(str.replace("Vyom", "Mahin")) # Replaces all occurences of old with new [str.replace(old, new)]
print(str.find("a")) # Returns 1st index of 1st occurence
print(str.count("a")) # Counts the occurences of substr in string

# Conditional Statements

light = "green"

if(light == "red"):
    print("Stop") # 4 spaces here given are indentation (proper spacing)
elif(light == "green"):
    print("Go") 
elif(light == "yellow"):
    print("Look")
else:
    print("Traffic Signal is not working")

# Grading System
marks = int(input("Enter the marks of a student: "))

if(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B"
elif(marks < 80 and marks >= 70):
    grade = "C"
else:
    grade = "D"

print("Grade of the student is:", grade)

# Nesting
age = int(input("Enter your age: "))

if(age >= 18):
    if(age >= 80):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")