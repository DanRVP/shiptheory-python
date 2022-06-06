from Objects.QueryObject import QueryObject

class PackageQuery(QueryObject):
    valid_fields = [
        'id',
        'name',
        'lenght',
        'width',
        'height',
        'active',
        'limit',
    ]

    def __init__(self, data: dict = None) -> None:
        super().__init__(data)
