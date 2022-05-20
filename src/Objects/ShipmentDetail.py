from src.Objects.ClientObject import ClientObject
from datetime import datetime

class ShipmentDetail(ClientObject):

    @property 
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property 
    def parcels(self) -> int:
        return self._parcels

    @parcels.setter
    def parcels(self, parcels: int):
        self._parcels = parcels

    @property 
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property 
    def shipping_price(self) -> float:
        return self._shipping_price

    @shipping_price.setter
    def shipping_price(self, shipping_price: float):
        self._shipping_price = shipping_price

    @property 
    def reference3(self) -> str:
        return self._reference3

    @reference3.setter
    def reference3(self, reference3: str):
        self._reference3 = reference3

    @property 
    def format_id(self) -> int:
        return self._format_id

    @format_id.setter
    def format_id(self, format_id: int):
        self._format_id = format_id

    @property 
    def instructions(self) -> str:
        return self._instructions

    @instructions.setter
    def instructions(self, instructions: str):
        self._instructions = instructions

    @property 
    def gift_message(self) -> str:
        return self._gift_message

    @gift_message.setter
    def gift_message(self, gift_message: str):
        self._gift_message = gift_message

    @property 
    def channel_shipservice_name(self) -> str:
        return self._channel_shipservice_name

    @channel_shipservice_name.setter
    def channel_shipservice_name(self, channel_shipservice_name: str):
        self._channel_shipservice_name = channel_shipservice_name    

    @property 
    def currency_code(self) -> str:
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        self._currency_code = currency_code

    @property 
    def sales_source(self) -> str:
        return self._sales_source

    @sales_source.setter
    def sales_source(self, sales_source: str):
        self._sales_source = sales_source    

    @property 
    def ship_date(self) -> datetime:
        return self._ship_date

    @ship_date.setter
    def ship_date(self, ship_date: datetime):
        self._ship_date = ship_date 

    @property 
    def rules_metadata(self) -> str:
        return self._rules_metadata

    @rules_metadata.setter
    def rules_metadata(self, rules_metadata: str):
        self._rules_metadata = rules_metadata 
    
    @property 
    def duty_tax_number(self) -> str:
        return self._duty_tax_number

    @duty_tax_number.setter
    def duty_tax_number(self, duty_tax_number: str):
        self._duty_tax_number = duty_tax_number

    @property 
    def duty_tax_number_type(self) -> str:
        return self._duty_tax_number_type

    @duty_tax_number_type.setter
    def duty_tax_number_type(self, duty_tax_number_type: str):
        self._duty_tax_number_type = duty_tax_number_type
