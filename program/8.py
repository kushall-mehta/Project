# Program to check if string contains only numbers
text = input("Enter a string: ")
if text.isnumeric():
    print("The string contains only numeric characters.")
else:
    print("The string does NOT contain only numeric characters.")