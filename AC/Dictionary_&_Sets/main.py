# Dictionary
# Dictionaries are use to store data values in key:value pairs
# They are unordered, mutable(changable) & don't allow duplicate keys

dict = {
    "name": "Vyom",
    "cpga": 9.5,
    "marks": [90, 98, 96]
}

print(dict["marks"])
dict["age"] = 21    # To assign or add a new value
print(dict)

# Nested Dictionaries
student = {
    "name": "Vyom",
    "score": {
        "maths": 98,
        "chem": 90,
        "phy": 96
    }
}

print(student["score"]["maths"])

# Dictionary Methods
print(student.keys())   # returns all keys

print(student.values())     # returns all values

print(student.items())      # returns all (key, val) pairs as tuples and we can change it from tuples to list by type casting

print(student.get("score"))     # returns the key according to value and if there is any error in this one then also the code below it will be executed

new_dict = {
    "age": 21
}
student.update(new_dict)
print(student)


# Sets 
# Set is the collection of the unordered items.               
# Each element in the set must be unique and immutable

nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}
# repeated elements stored only once, so it resolved to {1, 2}
null_set = set()    # empty set syntax
print(type(nums))
print(set2)
print(len(set2))
# List and Dictionaries are never stored in the Sets

# Set Methods
# Set is mutable but the elements of the set are immutable
# In set elements we can only pass tuples

# 1. set.add(el)    adds an element el
null_set.add(1)
null_set.add(2)
null_set.add(2)
null_set.add(3)
null_set.add("Vyom")    # String
null_set.add((1, 2, 3))     # Tuple
# null_set.add([1, 2, 3])   # List adding is not allowed and it will throw an error
print(len(null_set))
print(null_set)


# 2. set.remove(el)     removes the element el
null_set.remove(2)
# null_set.remove(7)    It will trow error as there is not 7
print(null_set)


# 3. set.clear()        empties the set
# null_set.clear()      It will empty the set and the length of the set will be zero


# 4. set.pop()      Pops the random element
null_set.pop()
null_set.pop()
print(null_set)


# 5. set.union(set2)    Combines both set values and returns new
setOne = {1, 2, 3}
setTwo = {2, 3, 4}
print(setOne.union(setTwo))     # {1, 2, 3, 4}


# 6. set.intersection(set2)     Combines common values and return new
print(setOne.intersection(setTwo))      # {2, 3}