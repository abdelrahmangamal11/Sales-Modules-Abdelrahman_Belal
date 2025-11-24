from base import BaseModel
from invoice import Invoice
from customer import Customer

class SaleOrder(BaseModel):
    
    def __init__(self, customer: Customer):
        super().__init__("Sale_Order") 
        self._lines = []
        self._state = "draft"
        self._customer = customer       
        self._customer_id = customer.id 

    def add_line(self,product, quantity,unite_price):
        new_line = SaleOrderline(product, quantity,unite_price)
        self._lines.append(new_line)
        return new_line
        

    def confirm(self):
        self._state="confirmed"

         # Create invoice for this order
        invoice = Invoice(self._customer)

        # Copy invoice lines from sale order
        for line in self._lines:
            invoice.add_line(
                product=line.product,
                quantity=line.quantity,
                unit_price=line.unit_price
            )
        return invoice
        
    def cancel(self):
        self._state="canceled"
        pass

    @property
    def state(self):
        return self._state
    
    @property
    def customer_id(self):
        return self._customer_id
    
    def __str__(self):
        lines_str = [str(line) for line in self._lines]
        return f"{self.__class__.__name__}( customer={self._customer_id}, state={self._state}, lines={lines_str})"


class SaleOrderline():

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
        return f"{self.__class__.__name__}(product={self.product}, quantity={self.quantity}, unit_price={self.unit_price}, total_price={self._sub_total})"
