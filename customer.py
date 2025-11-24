from base import BaseModel

class Customer (BaseModel):
    def __init__ (self,name,email,phone):
        super().__init__(name) 
        self._email=email
        self._phone=phone
        pass


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, mail={self.email}, phone={self.phone})"