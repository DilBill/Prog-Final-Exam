# Dilraj Bola, Student # 991736047
class Product:
    
    def __init__(self,code,name,category,quantity,cost):
        self._productCode = code
        self._productName = name
        self._productCategory = category
        self._productQuantity = quantity
        self._cost = cost
        
    def getCode(self):
        productCode = self._productCode
        
        return productCode
    
    def newMethod(self,category):
        
        try:
            if category == str:
                self._productCategory = category
            
        except ValueError:
            print("Please enter a valid alphabatical input ")
    
    def netPrice(self):
        net = (self._productQuantity * self._cost) * 1.135
        return round(net,2)
        
        
        