
from Objects.ShipmentQuery import ShipmentQuery

class SearchShipmentQuery(ShipmentQuery):
    extra_valid_fields = [
        'include_products',
        'created_from',
        'created_to',
    ]

    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
        self.addExtraValidFields(self.extra_valid_fields)
