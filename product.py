from base import BaseModel


class Product(BaseModel):

    def __init__(self,name, price, description):
        super().__init__(name)
        self._price = price
        self._description = description
        self._product_type = "goods"   

    def select_goods_product_type(self):
        self._product_type="goods"
        return self._product_type
    
    def select_services_product_type(self):
        self._product_type="services"
        return self._product_type

    @property
    def price(self):
        return self._price
    
    @property
    def description(self):
        return self._description
    
    @price.setter
    def price(self, pValue):
        if pValue <= 0 :
            raise ValueError("Price Can't be less than 0 ")
        self._price = pValue

    @description.setter
    def description(self, dValue):
        self._description = dValue

    def __str__(self):
            return (
                f"{self.__class__.__name__}("
                f"id={self._id}, "
                f"name={self._name}, "
                f"price={self._price}, "
                f"description={self._description}, "
                f"product_type={self._product_type} "
                f")"
            )