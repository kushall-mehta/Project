# Program to check string case
text = input("Enter a string: ")
if text.isupper():
    print("UPPERCASE.")
elif text.islower():
    print(" lowercase.")
else:
    print("Mixed case.")