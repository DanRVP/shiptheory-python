from ShiptheoryPython.Objects.ClientObject import ClientObject

class ReturnLabel(ClientObject):
    
    @property 
    def outgoing_reference(self) -> str:
        return self._outgoing_reference

    @outgoing_reference.setter
    def outgoing_reference(self, outgoing_reference: str):
        self._outgoing_reference = outgoing_reference

    @property 
    def delivery_postcode(self) -> str:
        return self._delivery_postcode

    @delivery_postcode.setter
    def delivery_postcode(self, delivery_postcode: str):
        self._delivery_postcode = delivery_postcode

    @property 
    def return_service(self) -> int:
        return self._return_service

    @return_service.setter
    def return_service(self, return_service: int):
        self._return_service = return_service

    @property 
    def expiry(self) -> str:
        return self._expiry

    @expiry.setter
    def expiry(self, expiry: str):
        self._expiry = expiry
