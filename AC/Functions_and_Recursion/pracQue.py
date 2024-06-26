def factorial(n):
    if n < 0:
        print("Wrong input")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        facto = 1
        i = 1
        while i <= n:
            facto *= i
            i += 1
        return facto

# Example usage:
num = int(input("Enter the number: "))
fact = factorial(num)
if fact is not None:
    print("Factorial is:", fact)