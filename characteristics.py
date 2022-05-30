# import materialStrategy as ms
from abc import ABCMeta as am,abstractmethod

class Characteristics(metaclass= am):
    """Abstract class for the creation of T-shirt characteristics (color, size, fabric)"""
    @abstractmethod
    def get_characteristics(self):
        pass

class AbstractTShirtCreation(metaclass=am):
    """Abstract class for the product creation"""
    @abstractmethod
    def get_product(self):
        pass

class TShirt:
    def __init__(self,color,size,fabric,price):
        self.color=color
        self.size=size
        self.fabric=fabric
        self.price=price

    def __str__(self):
        return f"{self.color} T-shirt of size {self.size} and fabric: {self.fabric}. The price is:{self.price}"

class CreateTShirt(AbstractTShirtCreation):
    def get_product(self):
        color = Color().get_characteristics()
        size = Size().get_characteristics()
        fabric = Fabric().get_characteristics()
        priced_tshirt = FabricPrice(fabric).calc()

        tshirt = TShirt(color,size,fabric,priced_tshirt)
        return tshirt 

class Color(Characteristics):
    def get_characteristics(self):
        colors = ["Red","Orange","Yellow","Green","Indigo","Violet"] 
        # validation for existing T-shirt colors
        while True:
            color=input("\tOur available colors are:\n Red\n Yellow\n Green\n Indigo\n Violet\nPlease choose color: ").capitalize()
            if color in colors:
                return color
            else:
                print("color does not exist")

class Size(Characteristics):
    def get_characteristics(self):
        sizes={"S","M","L","XL","XXL","XXXL"}
        # validation for available T-shirt sizes
        while True:
            size=input("\tT-shirts are available at sizes:\n S,M,L,XL,XXL,XXXL\nPlease choose size: ").upper()
            if size in sizes:
                return size
            else:
                print("size does not exist")       

class Fabric(Characteristics):
    def get_characteristics(self):
        fabrics={'wool','cotton','polyester','rayon','linen','cashmere','silk'}
        # validation for available T-shirt fabrics
        while True:
            fabric = input("\tYou can choose your favorite fabric:\n Wool\n Cotton\n Polyester\n Rayon\n Linen\n Cashmere\n Silk\nPlease choose fabric: ").lower()
            if fabric in fabrics:
                return fabric
            else:
                print("fabric does not exist")
    
class FabricPrice:
    """This class calculates T-shirt cost depending on the fabric option"""
    price=20
    def __init__(self, fabric):
        self.fabric=fabric

    def calc(self):
        if self.fabric=='wool':
            return FabricPrice.price*1.3
        elif self.fabric == 'cotton':
            return FabricPrice.price*1.2
        elif self.fabric == 'polyester':
            return FabricPrice.price*1.1
        elif self.fabric == 'rayon':
            return FabricPrice.price*1.2
        elif self.fabric == 'linen':
            return FabricPrice.price*1.1
        elif self.fabric == 'cashmere':
            return FabricPrice.price*1.8                
        elif self.fabric == 'silk':
            return FabricPrice.price*1.9
        else: return "fabric does not exist"



