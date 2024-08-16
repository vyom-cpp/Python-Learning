# Initialize a list
my_list = [1, 2, 3, 4, 5]

# Append: Add an element to the end of the list
my_list.append(6)
print("After append:", my_list)

# Insert: Insert an element at a specific position
my_list.insert(2, 'inserted')
print("After insert:", my_list)

# Remove: Remove the first occurrence of a value
my_list.remove('inserted')
print("After remove:", my_list)

# Pop: Remove and return the element at the given position (default is the last element)
popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

# Index: Return the index of the first occurrence of a value
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)

# Count: Return the number of occurrences of a value
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)

# Sort: Sort the list in ascending order
my_list.sort()
print("After sort:", my_list)

# Reverse: Reverse the elements of the list
my_list.reverse()
print("After reverse:", my_list)

# Extend: Extend the list by appending elements from an iterable
my_list.extend([7, 8, 9])
print("After extend:", my_list)

# Clear: Remove all elements from the list
my_list.clear()
print("After clear:", my_list)

# Example list to demonstrate slicing
example_list = [10, 20, 30, 40, 50]

# Slicing: Get a subset of the list
sliced_list = example_list[1:4]
print("Sliced list (from index 1 to 3):", sliced_list)

# List Comprehension: Create a new list based on an existing list
squared_list = [x**2 for x in example_list]
print("Squared list:", squared_list)

# Copy: Create a shallow copy of the list
copied_list = example_list.copy()
print("Copied list:", copied_list)