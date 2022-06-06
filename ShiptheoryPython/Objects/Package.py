from ShiptheoryPython.Objects.ClientObject import ClientObject

class Package(ClientObject):
    
    @property 
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property 
    def weight(self) -> float:
        return self._weight

    @id.setter
    def weight(self, weight: float):
        self._weight = weight
