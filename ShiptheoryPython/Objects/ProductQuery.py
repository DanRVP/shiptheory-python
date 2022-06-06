from ShiptheoryPython.Objects.QueryObject import QueryObject

class ProductQuery(QueryObject):
    valid_fields = [
        'limit',
        'sort',
    ]

    def __init__(self, data: dict = None) -> None:
        super().__init__(data)

class ProductSortParameters:
     SKU = 'sku'
     NAME = 'name'
     PRICE = 'price'
     WEIGHT = 'weight'
     CREATED = 'modified'
     MODIFIED = 'modified'
