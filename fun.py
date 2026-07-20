# def hello(*srti):
#     for i in srti:
#         print("Hello, " + i)
#     # print("Hello, " + srti[3])
# hello("World","raja","rani","shyam")

# def add(lis):
#     sum =0
#     for i in lis:
#         sum = sum+i
#     print("Sum of the list is:", sum)

# add([1, 2, 3, 4, 5])

# def multi(x):
#     product = 1
#     for i in x:
#         product =product* i
#     print("Product of the list is:", product)
# multi([1, 2, 3, 4, 5])

def strin(fname : str, lname : str):
    fname.capitalize()
    lname.capitalize()
    print("Hello, " + fname + " " + lname)
    return fname + " " + lname
strin("rajan","kushal")

def myfcun(no1 , no2):
    return no1+no2
print(myfcun(20,30))

