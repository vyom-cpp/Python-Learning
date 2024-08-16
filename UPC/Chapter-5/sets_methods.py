# Initialize a set
my_set = {1, 2, 3, 4, 5}

# Add: Add an element to the set
my_set.add(6)
print("After add:", my_set)

# Remove: Remove an element from the set; raises KeyError if the element is not present
my_set.remove(6)
print("After remove:", my_set)

# Discard: Remove an element from the set if it is present
my_set.discard(5)
print("After discard:", my_set)

# Pop: Remove and return an arbitrary element from the set
popped_element = my_set.pop()
print("After pop:", my_set)
print("Popped element:", popped_element)

# Clear: Remove all elements from the set
my_set.clear()
print("After clear:", my_set)

# Union: Return a set containing all elements from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection: Return a set containing only elements present in both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference: Return a set containing elements present in the first set but not in the second
difference_set = set1.difference(set2)
print("Difference:", difference_set)

# Symmetric Difference: Return a set containing elements in either set but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)

# Update: Update the set with elements from another set
set1.update({6, 7})
print("After update:", set1)

# Intersection Update: Update the set with the intersection of itself and another set
set1.intersection_update(set2)
print("After intersection update:", set1)

# Difference Update: Update the set with the difference of itself and another set
set1 = {1, 2, 3}
set1.difference_update(set2)
print("After difference update:", set1)

# Symmetric Difference Update: Update the set with the symmetric difference of itself and another set
set1 = {1, 2, 3}
set1.symmetric_difference_update(set2)
print("After symmetric difference update:", set1)

# Set comprehension
example_set = {x**2 for x in range(5)}
print("Set comprehension:", example_set)