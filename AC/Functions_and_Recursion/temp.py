# Write a function to print the length of a list (list is a parameter)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def listLength(list):
    print(len(list))

listLength(nums)

# Write a function to print the elements of a list in a single line. (list is a parameter)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printList(list):
    for element in list:
        print(element, end=" ")  # Using end=" " to print elements in the same line with a space between them
    print() 

printList(num)