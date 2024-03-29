# Store the following word meanings in a Python Dictionary
dict = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

print(dict)

# Assume one classroom is required for one subject. How many classrooms are needed
subject = {
    "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
}

print(subject)
print("No. of classrooms needed are:", len(subject))


# Write a Program to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value

marks = {}
x = int(input("Enter Physics Marks: "))
marks.update({"phy" : x})

y = int(input("Enter Chemistry Marks: "))
marks.update({"chem" : y})

z = int(input("Enter Maths Marks: "))
marks.update({"math" : z})

print(marks)


# Figure out a way to store 9 and 9.0 in a set
nums = {9, str('9.0')}
print(nums)