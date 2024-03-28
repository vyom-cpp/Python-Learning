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