from src.Objects.SharedProduct import SharedProduct

class Product(SharedProduct):

    @property 
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    @property 
    def barcode(self) -> str:
        return self._barcode

    @barcode.setter
    def barcode(self, barcode: str):
        self._barcode = barcode

    @property 
    def commodity_composition(self) -> str:
        return self._commodity_composition

    @commodity_composition.setter
    def commodity_composition(self, commodity_composition: str):
        self._commodity_composition = commodity_composition

    @property 
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: float):
        self._length = length

    @property 
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, width: float):
        self._width = width

    @property 
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, height: float):
        self._height = height
    