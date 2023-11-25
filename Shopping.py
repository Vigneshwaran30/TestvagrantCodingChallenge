#Vigneshwaran P S
#1BY20CS215

#Creating product class(inside basket)

class Product:
    def __init__(self,name,price,gstamt,quantity):
        self.name=name
        self.price=price
        self.gstamt=gstamt
        self.quantity=quantity

    def returnname(self):
        return self.name
    
    def gst(self):
        return int(self.gstamt)
    
    def getquantuity(self):
        return int(self.quantity)
    
    def unitprice(self):
        return int(self.price)
    
#Creating Objects
object1 = Product("LeatherWallet",110,18,1)
object2 = Product("Umbrella",900,12,4)
object3 = Product("Cigarette",200,28,3)
object4 = Product("Honey",100,0,2)

#create basket with differnet products
basket=[object1,object2,object3,object4]

#initialize maxgst to object1
maxgst=basket[0].gst()

#Initialize Maximum product name to object1
maxproductname=basket[0].returnname()

#Finding Max Gst among the products
for i in basket:
    if i.gst()>maxgst:
        maxgst=i.gst()
        maxproductname=i.returnname()
print("The Product with maximum Gst is : " + maxproductname) 
print("The Maximum GST is : " + str(maxgst))

#Calculate the amount to be paid to the Shop Keeper
TotalPrice=0
for i in basket:
    # if i.unitprice()>500:
    TotalPrice=TotalPrice+((i.unitprice()*(i.gst()+100)*i.getquantuity())/10)
print(TotalPrice)