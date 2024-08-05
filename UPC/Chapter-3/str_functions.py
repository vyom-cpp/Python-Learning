# Define the strings for each function
string1 = "Hello, World!"
string2 = "  Python Programming  "
string3 = "apple,banana,cherry"
string4 = "Hello, World!"
string5 = "Hello, World!"
string6 = "Hello"
string7 = "Hello, World!"
string8 = "Hello, World!"
string9 = "Hello, World!"
string10 = "Hello, World!"

# len() - Get the length of string1
length = len(string1)
print(f"Length of string1: {length}")

# lower() - Convert string1 to lowercase
lowercase = string1.lower()
print(f"Lowercase of string1: {lowercase}")

# upper() - Convert string1 to uppercase
uppercase = string1.upper()
print(f"Uppercase of string1: {uppercase}")

# strip() - Remove leading and trailing spaces from string2
stripped = string2.strip()
print(f"Stripped string2: '{stripped}'")

# split() - Split string3 into a list
split_list = string3.split(',')
print(f"Split string3: {split_list}")

# join() - Join elements of list into a string
joined_string = " ".join(split_list)
print(f"Joined list: {joined_string}")

# replace() - Replace 'World' with 'Python' in string4
replaced = string4.replace("World", "Python")
print(f"Replaced string4: {replaced}")

# find() - Find the position of 'World' in string5
found_index = string5.find("World")
print(f"Found 'World' in string5 at index: {found_index}")

# startswith() - Check if string6 starts with 'Hello'
starts_with = string6.startswith("Hello")
print(f"string6 starts with 'Hello': {starts_with}")

# endswith() - Check if string7 ends with 'World!'
ends_with = string7.endswith("World!")
print(f"string7 ends with 'World!': {ends_with}")

string = "sali chalti phirti \"cocaine\" hai"
print(string)