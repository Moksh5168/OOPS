#inheritance ------(1)single (2)multiple (3)multilevel
#JAVA,PHP Never support mulitple inheritance

# sinngle level
class A:
    def displayA(self):
        print("Welcome to Google A")

class B(A):
    def displayB(self):
        print("Welcome to Amazon B")

obj=B()
obj.displayA()
obj.displayB()

#multilevel

class A:
    def displayA(self):
        print("Welcome to Google A")

class B(A):
    def displayB(self):
        print("Welcome to Amazon B")

class C(B):
    def displayC(self):
        print("Welcome to Microsoft C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()


#Multiple
class A:
    def displayA(self):
        print("Welcome to Google A")

class B:
    def displayB(self):
        print("Welcome to Amazon B")

class C(A,B):
    def displayC(self):
        print("Welcome to Microsoft C")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
