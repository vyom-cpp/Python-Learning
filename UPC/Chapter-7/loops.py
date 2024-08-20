# For Loop
for i in range(1, 11):
    print(i)


# While Loop
j = 1
while(j < 6):
    print("Vyom")
    j +=1


# List using loops
l = [1, 2.4, "vyom", True]
k = 0
while(k < len(l)):
    print(l[k])
    k +=1

for item in l:
    print(item)


## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)


## For Loop with Strings
s = "Vyom"
for i in s:
    print(i)


z = [1,7,8] 

for item in z:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!


for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    


for i in range(645):
    pass



i = 0
while(i<45):
    print(i)
    i += 1