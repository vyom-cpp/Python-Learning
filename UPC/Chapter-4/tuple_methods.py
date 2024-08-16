# Initialize a tuple
my_tuple = (1, 2, 3, 4, 5)

# Count: Return the number of occurrences of a value
count_of_2 = my_tuple.count(2)
print("Count of 2:", count_of_2)

# Index: Return the index of the first occurrence of a value
index_of_4 = my_tuple.index(4)
print("Index of 4:", index_of_4)

# Tuple Concatenation: Combine two tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated tuple:", concatenated_tuple)

# Tuple Repetition: Repeat the elements of a tuple
repeated_tuple = my_tuple * 2
print("Repeated tuple:", repeated_tuple)

# Slicing: Get a subset of the tuple
sliced_tuple = my_tuple[1:4]
print("Sliced tuple (from index 1 to 3):", sliced_tuple)

# Tuple Unpacking: Assign tuple elements to individual variables
a, b, c, d, e = my_tuple
print("Tuple unpacking:", a, b, c, d, e)

# Using tuples as keys in a dictionary
tuple_dict = {my_tuple: "value"}
print("Dictionary with tuple as a key:", tuple_dict)

# Converting a list to a tuple
my_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)

# Looping through a tuple
print("Looping through the tuple:")
for item in my_tuple:
    print(item)

# Checking membership
is_3_in_tuple = 3 in my_tuple
print("Is 3 in the tuple?", is_3_in_tuple)

# Length of the tuple
length_of_tuple = len(my_tuple)
print("Length of the tuple:", length_of_tuple)