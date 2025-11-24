from base import BaseModel
from customer import Customer

class  Invoice(BaseModel):
    
    def __init__(self,customer:Customer):
        super().__init__("invoice")
        self._lines=[]
        self._state = "draft"
        self._customer_id=customer.id
        self._customer_name=customer.name
        self._customer_phone=customer.phone

    def add_line(self,product, quantity, unit_price):
        new_line = InvoiceLine(product, quantity,unit_price)
        self._lines.append(new_line)
        return new_line
        
    def confirm(self):
        self._state="posted"
        pass

    def cancel(self):
        self._state="canceled"
        pass

    @property
    def state(self):
        return self._state
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def customer_name(self):
        return self._customer_name
    
    @property
    def customer_phone(self):
        return self._customer_phone
    
    def __str__(self):
        lines_str = [str(line) for line in self._lines]
        return f"{self.__class__.__name__}( customer_id={self._customer_id}, customer_name={self._customer_name},customer_phone={self._customer_phone} ,state={self._state}, lines={lines_str})"


class InvoiceLine():

    def __init__(self,product,quantity,unit_price):
        self._quantity=quantity
        self._unit_price=unit_price
        self._sub_total=unit_price*quantity
        self._product=product
        pass

    @property
    def quantity(self):
        return self._quantity
    
    @property
    def unit_price(self):
        return self._unit_price
    
    @property
    def product(self):
        return self._product
    
    @property
    def sub_total(self):
        return self._sub_total
    
    def __str__(self):
        return f"{self.__class__.__name__}(product={self.product}, quantity={self.quantity}, unite_price={self.unit_price}, total_price={self._sub_total})"

