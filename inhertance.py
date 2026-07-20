class one:
    def onee(self,a,b):
        self.a=a
        self.b=b
class two(one):
    def cal_sum(self):
        print(self.a+self.b)
obj1=one()
obj1.onee(5,10)
obj2=two()
two.cal_sum(obj1)   

# class name:
#     def __init__(self,first,last):
#         self.first=first
#         self.last=last
# class child(name):
#     def display(self,age):
#         self.age=age
#         print("first name is: ",self.first)
#         print("last name is: ",self.last)
#         print("age is: ",self.age)
# obj3=name("kushal","kumar")
# obj4=child()
# obj4.display(obj1,52)

    