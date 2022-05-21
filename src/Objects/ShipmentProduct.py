from src.Objects.SharedProduct import SharedProduct

class ShipmentProduct(SharedProduct):

    @property 
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value
