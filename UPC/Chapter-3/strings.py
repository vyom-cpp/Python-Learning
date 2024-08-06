name = "Vyom"
print(len(name))

# The index in a string starts from 0 to (length - 1).
# sl = name[index_start:index_end]
# index_start is included
# index_end is not included

sl = name[2:4] # Start from index 2 all the way till 4th index (excluding 4)
print(sl)

# Negative indices start from last character from -1 to the first character
SL = name[-2:len(name)]
print(SL)

# Negative indices corresponds to -1 = (length - 1) index, -2 = (length - 2) index

a = "abcdefghijklmnopqrstuvwxyz"
print(a[0:19:3]) #adgjmps
#  Slices from index 0 to index 18, which is abcdefghijklmnopqr, then it starts from index 0 and jumps till 3rd on, which above shown