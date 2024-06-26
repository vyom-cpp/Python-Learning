# For loops are generally used for the sequential traversal. For traversing list, string, tuples, etc.

list = [1, 2, 3]
for el in list:     # el is a variable jisme list ke saare numbers pass honge
    print(el)


lists = [1, 2, 3, 4, 5]
for el in lists:
    print(el)
else:       # Work when loop ends
    print("End")


str = "Vyom Sutariya"
for char in str:
    print(char)


# Range: Range function returns a sequence of numbers starting from zero by default, and increments by 1 by default, and stops before a specified number

# range(start?, stop, step?)
# single value then range(stop);    two values then range(start, stop)


# Pass Statement
# Pass is a null statement that does nothing. It is used as a placeholder for future code