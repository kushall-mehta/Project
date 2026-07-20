class dog:
    def __init__(self,name,id):
        print("dog created")
        self.name = name
        self.id = id 
        print(self.name)
        print(self.id)
        pass
    def display(self):
        print("dog name is: ",self.name)
        print("dog id is: ",self.id)
        pass
Myclass = dog("kushal",5)
Myclass.display()


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