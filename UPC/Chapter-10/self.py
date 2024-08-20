class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


vyom = Employee()
# vyom.language = "JavaScript" # This is an instance attribute
vyom.greet()
vyom.getInfo() 
# Employee.getInfo(vyom)
 