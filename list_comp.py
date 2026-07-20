import random
li = ["kushal","kumar", "kushal kumar"]
li3 = [x for x in li if "kumar" not in x]
print(li3)

# Generate a list of squares root of numbers from 0 to 9
li2=[a**3 for a in range(10) if a%2==0]
print(li2)

# Generate a list of 10 random integers between 0 and 9, and filter those that are less than 5
r = [random.randint(0,9) for _ in range(10)]
li4 = [b for b in r if b < 5]
print(li4)
# can use inbuild function here 
li5=[c.replace('kumar','mehta') for c in li]
print(li5)

new_li=[20,20,20,20,100,200,50]
new_li2=[m*2 for m in new_li]   
print(new_li2)

new = [x if x == 20 or x ==100 or x == 200 else x*2 for x in new_li]
print(new)

