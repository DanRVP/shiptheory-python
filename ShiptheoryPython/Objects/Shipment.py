from ShiptheoryPython.Objects.ClientObject import ClientObject
from ShiptheoryPython.Objects.ShipmentDetail import ShipmentDetail
from ShiptheoryPython.Objects.Recipient import Recipient
from ShiptheoryPython.Objects.Sender import Sender

class Shipment(ClientObject):

    @property 
    def reference(self) -> str:
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        self._reference = reference
    
    @property 
    def reference2(self) -> str:
        return self._reference2

    @reference2.setter
    def reference2(self, reference2: str):
        self._reference2 = reference2
    
    @property 
    def delivery_service(self) -> str:
        return self._delivery_service

    @delivery_service.setter
    def delivery_service(self, delivery_service: str):
        self._delivery_service = delivery_service

    @property 
    def increment(self) -> int:
        return self._increment

    @increment.setter
    def increment(self, increment: int):
        self._increment = increment

    @property 
    def shipment_detail(self) -> ShipmentDetail:
        return self._shipment_detail

    @shipment_detail.setter
    def shipment_detail(self, shipment_detail: ShipmentDetail):
        self._shipment_detail = shipment_detail

    @property 
    def recipient(self) -> Recipient:
        return self._recipient

    @recipient.setter
    def recipient(self, recipient: Recipient):
        self._recipient = recipient

    @property 
    def sender(self) -> Sender:
        return self._sender

    @sender.setter
    def sender(self, sender: Sender):
        self._sender = sender

    @property 
    def products(self) -> list:
        return self._products

    @products.setter
    def products(self, products: list):
        self._products = products

    @property 
    def packages(self) -> list:
        return self._packages

    @packages.setter
    def packages(self, packages: list):
        self._packages = packages
