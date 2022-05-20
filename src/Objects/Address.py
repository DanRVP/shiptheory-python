from src.Objects.ClientObject import ClientObject

class Address(ClientObject):
    
    @property 
    def company(self) -> str:
        return self._company

    @company.setter
    def company(self, company: str):
        self._company = company

    @property 
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self._firstname = firstname

    @property 
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self._lastname = lastname

    @property 
    def address_line_1(self) -> str:
        return self._address_line_1

    @address_line_1.setter
    def address_line_1(self, address_line_1: str):
        self._address_line_1 = address_line_1

    @property 
    def address_line_2(self) -> str:
        return self._address_line_2

    @address_line_2.setter
    def address_line_2(self, address_line_2: str):
        self._address_line_2 = address_line_2

    @property 
    def address_line_3(self) -> str:
        return self._address_line_3

    @address_line_3.setter
    def address_line_3(self, address_line_3: str):
        self._address_line_3 = address_line_3

    @property 
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property 
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city
