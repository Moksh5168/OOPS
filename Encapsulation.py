class Student:
    def __init__(self):
        self.__name=""
    def getname(self):    #-------->getter
        return self.__name
    def setname(self,name): #------>setter
        self.__name=name

obj=Student()
obj.setname("Testing")
name=obj.getname()
print(name)