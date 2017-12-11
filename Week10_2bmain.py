class CashRegister :
    def __init__(self) :
        self.itemCount = 0
        self.totalPrice = 0.0
        self.change = 0.0

    def addItem(self):
        print("Buyer: How much does this item cost?")
        price = float(input("Enter a price: "))
        print("This item costs %s pounds!" % (price))
        self.itemCount = self.itemCount + 1
        self.totalPrice = self.totalPrice + price
                
    def getTotal(self):
        return self.totalPrice

    def getCount(self) :
        return self.itemCount

    def clear(self) :
        self.itemCount = 0
        self.totalPrice = 0.0
        self.change = 0.0
        
    def giveChange(self):
        pay = float(input("How much are you willing to pay?"))
        self.change = pay - self.totalPrice
        

    def printinfo(self):
      print("You have %s item!" % (self.itemCount))
      if self.change >= 0:
          print("Change: %s pounds" % (self.change))
      else:
          print("You owe me money bastard!")
    
    
            
