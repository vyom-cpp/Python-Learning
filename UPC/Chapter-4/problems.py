# Add the fruits name entered by user
fruits = []

f1 = input("Enter the fruit's name: ")
fruits.append(f1)

f2 = input("Enter the fruit's name: ")
fruits.append(f2)

f3 = input("Enter the fruit's name: ")
fruits.append(f3)

f4 = input("Enter the fruit's name: ")
fruits.append(f4)

f5 = input("Enter the fruit's name: ")
fruits.append(f5)

print(fruits)

# Accept the marks of students and display in sorted manner
student = []

s1 = int(input("Enter marks: "))
student.append(s1)

s2 = int(input("Enter marks: "))
student.append(s2)

s3 = int(input("Enter marks: "))
student.append(s3)

s4 = int(input("Enter marks: "))
student.append(s4)

s5 = int(input("Enter marks: "))
student.append(s5)

student.sort()
print(student)

# Sum of list
list = [1, 334, 34, 12]

print(sum(list))

# Count the number of zeroes in the tuple
tuple = (7, 0, 8, 0, 0, 9)

count = tuple.count(0)
print(count)