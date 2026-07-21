# Write a Python program to accept the total marks of a student and display the 
# corresponding grade. (Use if..elif..else) 
# Criteria: 
#  Marks 90–100: Grade A+ 
#  Marks 80–89: Grade A 
#  Marks 70–79: Grade B 
#  Marks 60–69: Grade C 
#  Marks 50–59: Grade D 
#  Marks below 50: Grade F

marks = int(input("Enter your total marks"))
if marks > 100 or marks < 0:
    print("plese enter marks between 0 to 100")
elif marks >= 90 and marks < 100:
    print("A+") 
elif marks >= 80 and marks < 90:
    print("A") 
elif marks >= 70 and marks < 80:
    print("B")
elif marks >= 60 and marks < 70:
    print("C")
elif marks >= 50 and marks < 60:
    print("D")
else :
    print("F")