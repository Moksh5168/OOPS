#____polymorphism means same function name (but different signatures) being uses for differentn types.

l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

#----------------------Function Overriding------------------------------------------#
class Ws:
    def displayinfo(self):
        print("Welcome to Google")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()                         # use for clled paraent class
        print("Welcome to Amazom")
obj=IIP()
obj.displayinfo()


#------------------------------Funtiion Overloading------------------------------------#

class Ws:
    def displayinfo(self,name=''):
        print("Welcome to Wscubetech"+name)

obj=Ws()
obj.displayinfo()
obj.displayinfo('python')