number_one = int(input("Enter the number: "))
number_two = int(input("Enter the number: "))
number_three = int(input("Enter the number: "))
number_four = int(input("Enter the number: "))

if number_one > number_two:
    if number_one > number_three:
        if number_one > number_four:
            print(f"{number_one} is the greatest")
        else:
            print(f"{number_four} is the greatest")
    else:
        if number_three > number_four:
            print(f"{number_three} is the greatest")
        else:
            print(f"{number_four} is the greatest")
else:
    if number_two > number_three:
        if number_two > number_four:
            print(f"{number_two} is the greatest")
        else:
            print(f"{number_four} is the greatest")
    else:
        if number_three > number_four:
            print(f"{number_three} is the greatest")
        else:
            print(f"{number_four} is the greatest")
