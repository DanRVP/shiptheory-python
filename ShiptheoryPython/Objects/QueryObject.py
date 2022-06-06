class QueryObject:
    valid_fields = []

    @property
    def fields(self) -> dict:
        return self._fields

    @fields.setter
    def fields(self, fields: dict):
        self._fields = fields

    def __init__(self, data: dict = None) -> None:
        self.fields = data

    def toQueryParams(self, strict = True):
        if self.fields in [None, '', []]:
            return ''

        fields = {}
        if (strict):
            for key in self.fields:
                if key in self.valid_fields and (self.fields[key] in ['', None]) == False:
                    fields[key] = self.fields[key]
        else:
            fields = self.fields

        return self._buildQueryParams(fields)

    def _buildQueryParams(self, fields):
        query_string = '?'
        params = ''
        for field in fields:
            params += '&' + str(field) + '=' + str(fields[field])

        return query_string + params.lstrip('&')

    def addExtraValidFields(self, fields):
        self.valid_fields = self.valid_fields + fields  
