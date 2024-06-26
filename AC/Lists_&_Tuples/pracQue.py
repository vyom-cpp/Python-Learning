# Write a program to ask the user to enter names of their 3 favourite movies & store them in a list
movie1 = input("Enter the first movie: ")
movie2 = input("Enter the second movie: ")
movie3 = input("Enter the third movie: ")

movie_list = [movie1, movie2, movie3]
print(movie_list)

# Or we can append them into an empty list also

# Write a program to check if a list contains a palindrome of elements
list_1 = ["racecar"]
copy_list_1 = list_1.copy()
copy_list_1.reverse()
if(copy_list_1 == list_1):
    print("It is palindrome")
else:
    print("It is not palindrome")

# Write a program to count the number of students with the 'A' grade in the following tuple.    [C, D, A, A, B, B, A]
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# Write a program too store the above values in a list and sort them from A to D
grade1 = ["C", "D", "A", "A", "B", "B", "A"]
grade1.sort()
print(grade1)