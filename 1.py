from abc import ABC,abstractmethod

class Shop(ABC):
    @abstractmethod
    def calcRevenue(self):
        pass

class ClothesShop(Shop):
    def calcRevenue(self):
        return self.sellscount*5
    
obj= ClothesShop()
obj.sellsCount=20
print(obj.calcRevenue())