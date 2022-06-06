from ShiptheoryPython.Objects.ClientObject import ClientObject

class SharedProduct(ClientObject):
    
    @property 
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property 
    def sku(self) -> str:
        return self._sku

    @sku.setter
    def sku(self, sku: str):
        self._sku = sku
    
    @property 
    def qty(self) -> int:
        return self._qty

    @qty.setter
    def qty(self, qty: int):
        self._qty = qty

    @property 
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property 
    def commodity_code(self) -> str:
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, commodity_code: str):
        self._commodity_code = commodity_code

    @property 
    def commodity_description(self) -> str:
        return self._commodity_description

    @commodity_description.setter
    def commodity_description(self, commodity_description: str):
        self._commodity_description = commodity_description

    @property 
    def commodity_manucountry(self) -> str:
        return self._commodity_manucountry

    @commodity_manucountry.setter
    def commodity_manucountry(self, commodity_manucountry: str):
        self._commodity_manucountry = commodity_manucountry
