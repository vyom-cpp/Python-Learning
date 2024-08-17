# Input the marks from the user
marks = float(input("Enter the marks (in percentage): "))

# Determine the grade using if-else statements
if 91 <= marks <= 100:
    print("Grade: A1")
elif 81 <= marks < 91:
    print("Grade: A2")
elif 71 <= marks < 81:
    print("Grade: B1")
elif 61 <= marks < 71:
    print("Grade: B2")
elif 51 <= marks < 61:
    print("Grade: C1")
elif 41 <= marks < 51:
    print("Grade: C2")
elif 31 <= marks < 41:
    print("Grade: D1")
elif 21 <= marks < 31:
    print("Grade: E1")
elif 0 <= marks < 21:
    print("Grade: E2")
else:
    print("Invalid marks entered. Please enter a value between 0 and 100.")
