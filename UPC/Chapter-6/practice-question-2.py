# Input marks for the three subjects
pds = float(input("Enter marks obtained in PDS: "))
ada = float(input("Enter marks obtained in ADA: "))
se = float(input("Enter marks obtained in SE: "))

# Calculate the total and percentage
total_marks = pds + ada + se
percentage = (total_marks / 300) * 100

# Check the passing criteria
if percentage >= 40 and pds >= 33 and ada >= 33 and se >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")
