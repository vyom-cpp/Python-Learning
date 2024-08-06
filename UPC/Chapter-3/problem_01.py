name = input("Enter the name of user: ")
print(f"Good Afternoon, {name}")

letter = '''Dear <|Name|>,
You are selected.
<|Date|>'''

print(letter.replace("<|Name|>", "Vyom").replace("<|Date|>", "Auguest 6, 2024"))

string = "Vyom  is  a great  guy"
print(string.replace("  ", " "))