# Input the comment from the user
user_comment = input("Enter the comment: ").lower()

# Check for spam keywords using if-else conditions
if "make a lot of money" in user_comment:
    print("This is a spam comment.")
elif "buy now" in user_comment:
    print("This is a spam comment.")
elif "subscribe this" in user_comment:
    print("This is a spam comment.")
elif "click this" in user_comment:
    print("This is a spam comment.")
else:
    print("This is not a spam comment.")
