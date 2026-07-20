li = ["kushal","kumar", "kushal kumar"]
li2 = ["raj", "kumar", "raj kumar",1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(li)
#print(li[5])
print(len(li))

if "kumar" in li:
    print("yes")
else:
    print("no")

li.insert(2,"new item")
print(li)
# add the item at the end of the list like 1st list in 2nd list
# li.extend(li2)
# print(li)

li.remove("kumar")
print(li)

li.pop(2)
print(li)

#del li[8]
print(li)

# for i in li:
#     print(i)
for i in range(len(li)):
    print(li[i])
    
li3 = [x for x in li if "kumar" not in x]
print(li3)

def ntg(n):
    return(n - 20)
    
li4=[50,10,70,80,50,100,200]
li4.sort(key = ntg)
print(li4)
print(li4.count(10))

li5 = []
for i in range(3):
    li5.append(input("Enter movie names: "))
l1 = li5.copy()
l1.reverse()


if li5 == l1:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
co = ['A','A','C','B','C','A','B','C','A']
co.sort()
print(co.count('A'))
print(co.count('B'))
print(co.count('C'))
print(co)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
eve = list(filter(lambda x: x % 2 == 0, numbers))
print(eve)  
