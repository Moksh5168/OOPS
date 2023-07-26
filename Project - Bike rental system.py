#-----------------------------------------  Bike Rental System  ---------------------------------------------#

#(1)Display availble bike
#(2)Request a bike for rent(100Rs-> 1 qty)
#(3)Exit

class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("Total Bikes",self.stock)
    def rentForBike(self,q):

        if q<=0:
            print("Enter the positive value or grater than zero")
        elif  q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("Total price",q*100)
            print("Total Bikes",self.stock)
while True:
    obj=bikeShop(100)
    uc=int(input('''
1 Display Stocks
2 Rent a Bike
3 exit''' ))
    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("Enter the Qty:----"))
        obj.rentForBike(n)
    else:
        break    

