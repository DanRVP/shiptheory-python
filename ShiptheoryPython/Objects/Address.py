from ShiptheoryPython.Objects.ClientObject import ClientObject

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
    def county(self) -> str:
        return self._county

    @county.setter
    def county(self, county: str):
        self._county = county

    @property 
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

    @property 
    def postcode(self) -> str:
        return self._postcode

    @postcode.setter
    def postcode(self, postcode: str):
        self._postcode = postcode

    @property 
    def telephone(self) -> str:
        return self._telephone

    @telephone.setter
    def telephone(self, telephone: str):
        self._telephone = telephone

    @property 
    def mobile(self) -> str:
        return self._mobile

    @mobile.setter
    def mobile(self, mobile: str):
        self._mobile = mobile

    @property 
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property 
    def tax_number(self) -> str:
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number: str):
        self._tax_number = tax_number
