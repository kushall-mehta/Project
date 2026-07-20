# class num():
#     def __init__(self,val1,val2):
#         self.val1=val1
#         self.val2 = val2
#         #print(sum)
#         pass
#     def sum(self):
#         print(self.val1+self.val2)   
#     #def sum():
# cl = num(28,30)
# cl.sum()


# class notes():
#     def __init__(self,l1):
#         print(l1)
# l1 =["hello im kushal there are no one here",8998,"chal chal chal","hello there"]
# notes(l1)



class person:
    name = "rahul"
    age = 12
    def info(self):
        print(self.name)
a = person()
b = person()
a.name = "ramu"
b.name = "rahul"
a.info()
b.info()

# class person:
#     name = None
#     age = None
#     def info(self):
#         print(self.name)
# a = person()
# b = person()
# a.name = "ramu"
# b.name = "rahul"
# a.info()
# b.info()



# class person:
#     name = None
#     age = None
#     def info(self,name,age):
#         print(name)
#         print(age)
# a = person()
# b = person()
# a.info("kushal",20)
# b.info("sakshi",19)








class person:
    def __init__(self,n,a):
        self.name = n 
        self.age = a
    def info(self):
        print(self.name)
a = person("kushal",20)
b = person("ramu",20)
a.info()
b.info()
