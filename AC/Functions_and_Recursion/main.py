# Functions: Block of statements that performs a specific task.

# Function Definition

# def func_name(param1, param2, ...):       
#   some work
#   return val

# Function Call

# func_name(arg1, arg2, ...)
def calc_sum(x,y):
    sum = x+y
    print(sum, "This line executed")
    return sum          # Ye line execute nahi hogi because of the upper print statement, and if the above print line is not there, then this function will not return anything


calc_sum(5,5)       # Abhi maine function ko call kiya hai toh isme (5,5) jake store ho jayegi x and y variable me

def printBsdk():
    print("Chala ja bsdk")

output = printBsdk()
print(output)           # Iske output None aayega kyuki function na kuch le raha hai na kuch de raha hai.

def average():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    return (a + b + c) / 3

result = average()
print("The average is:", result)

# Default Parameters: Assigning a default value to parameter, which is used when no argument is passed

