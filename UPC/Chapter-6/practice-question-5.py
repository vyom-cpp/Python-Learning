# Predefined list of names
names_list = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Input the name from the user
name_to_check = input("Enter a name: ")

# Check if the name is in the list
if name_to_check in names_list:
    print(f"{name_to_check} is in the list.")
else:
    print(f"{name_to_check} is not in the list.")
