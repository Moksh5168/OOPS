#Encapsulation means private

class Student:
    __name="Ravi"   #For making a variable in encapssulatioon use '__'
    def __init__(self):
        print(self.__name)
        self.__displayinfo() # private che etle andar j access karay

    #private
    def __displayinfo(self):
        print("Welcome to Google MOKSH!!")
obj=Student()

