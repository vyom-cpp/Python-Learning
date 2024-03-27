# Lists:- A built-in data type that stores set of values. It can store elements of different types (integer, float, strings, etc) 

# marks = [87, 65, 33, 67.45, 34.22]    # marks[0], marks[1],...
# marks[3] = 54.23  # Allowed in Python

marks = [10, 20.9, 30, 23, 44.44]
print(marks)
print(type(marks))
print(len(marks)) # Return Length

# String are immutable(cannot be changed) while lists are mutable (can be changed) in Python

student = ["Rahul", 89.54, 21, "Gandhinagar"]
print(student[0])
student[3] = "Sargasan"
print(student)

# List Slicing (Similar to String Slicing)
# list_name[starting_idx : ending_idx]      ending_idx is not included

# marks = [10, 20.9, 30, 23, 44.44]
# marks[1:4] is [20.9, 30, 23]
# marks[:4] is same as marks[0:4]
# marks[1:] is same as marks[1:len(marks)]
# marks[-3:-1] is [30, 23]

# List Methods
list = [2, 1, 3]

print(list.append(4))  # add one element at the end    [2, 1, 3, 4]
print(list.sort()) # sorts in ascending order  [1, 2, 3, 4]
print(list.sort(reverse = True))   # sorts in descending order [4, 3, 2, 1]
print(list.reverse())  # reverse the list  [4, 3, 1, 2]
print(list.insert(1, 99))  # insert element 99 at index 1
print(list.remove(1))  # removes the first occurence of element    [2, 3]
print(list.pop(1))     # removes element at index 1    [2]

# Tuples:- A built-in data type that lets us create immutable sequences of values.

tup = (87, 4.556, 34, 2, 56, 2)    # tup[0], tup[1],...
# tup[0] = 34 is not allowed as tuples are immutable
# tup()     An empty tuple
# tup(1,)   Single valued tuple and comma is necessary to make it look like a tuple

# Tuple Methods:
print(tup.index(2))    # returns of the first occurence of the element 2    {tup.index(element)}
print(tup.count(2))     # counts total occurences of the element 2          {tup.index(element)}