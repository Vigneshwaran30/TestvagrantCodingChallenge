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
object1 = Product("LeatherWallet",1100,18,1)
object2 = Product("Umbrella",900,12,4)
object3 = Product("Cigarette",200,28,3)
object4 = Product("Honey",100,0,2)

#create basket with differnet products
basket=[object1,object2,object3,object4]

#Initialize maxgst and the maxproduct name to first object
maxgst=(basket[0].gst()/100)*basket[0].unitprice()
maxproductname=basket[0].returnname()

#travesrsing through array and finding the answer
for i in range(len(basket)):
    if (basket[i].gst()/100)*basket[i].unitprice() > maxgst:
        maxgst=(basket[i].gst()/100)*basket[i].unitprice()
        maxproductname=basket[i].returname()

print("The Product with maximum Gst is : " + maxproductname) 

#Calculate the amount to be paid to the Shop Keeper
maxprice=0
for i in basket:
    if i.gst()==0:
        perunit=i.unitprice()
    else:
        perunit=i.unitprice()+(i.unitprice()*(i.gst()/100))
    
    if perunit>500:
        perunit=perunit*(95/100)

    maxprice=maxprice+(perunit*i.getquantuity())

print(maxprice)