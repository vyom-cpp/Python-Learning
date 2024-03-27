print("Hello World")
print("Vyom Sutariya")
print("My name is Vyom", "I am 21 years old.")
print(69) # Numbers alone can be printed without any quotes
print(100-4)

# A variable is a name given to a memory location in a program
name = "Vyom"
age = 21
applePrice = 25.99
old = False
# a = None
ab = 500
ba = 100
sum = ab + ba
# Declared variables named as name, age, old, a, ab, ba, sum
print(name)
print(age)

print("Mera naam", name, "hai")
print("Meri umar", age, "saal hai")

print(type(name))
print(type(age))
print(type(applePrice))
print(type(old))
# print(type(a))

print(sum)
# print(ba ** ab) # ba^ab

ba += 100
# ba -= 100
# ba += 10
# ba /= 10
# ba %= 10
# ba **= 10
print("num: ", ba)

# Logical Operators
print(not False)
print(not True)

val1 = True
val2 = False
print("Answer Operator(and): ", val1 and val2) # False
print("Answer Operator(or): ", val1 or val2) # True

val3 = True
val4 = True
print("Answer Operator(and): ", val3 and val4) # True
print("Answer Operator(or): ", val3 or val4) # True

# Type Conversion(Interpreter of Python does it automatically)
# Type Casting(It is done manually)
a = float("9.02")
b = int("3")
st = str(124)

print(type(a))
print(type(b))
print(type(st))

summ = a + b
print(summ)