
from Objects.ShipmentQuery import ShipmentQuery

class ListShipmentQuery(ShipmentQuery):
    extra_valid_fields = [
        'created',
        'modified',
    ]

    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.addExtraValidFields(self.extra_valid_fields)
