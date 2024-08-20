class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


vyom = Employee()
vyom.name = "vyom" # This is an instance attribute
print(vyom.name, vyom.language, vyom.salary)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class