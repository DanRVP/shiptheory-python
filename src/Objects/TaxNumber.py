from src.Objects.ClientObject import ClientObject

class TaxNumber(ClientObject):

    def __init__(self, tax_number, tax_number_type):
        self.tax_number = tax_number
        self.tax_number_type = tax_number_type
        
    @property 
    def tax_number(self) -> str:
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number: str):
        self._tax_number = tax_number

    @property 
    def tax_number_type(self) -> str:
        return self._tax_number_type

    @tax_number_type.setter
    def tax_number_type(self, tax_number_type: str):
        self._tax_number_type = tax_number_type

class TaxNumberTypes:
    IOSS = 'IOSS'
    ABN = 'ABN'
    IRD = 'IRD'
    OSS = 'OSS'
    VOEC = 'VOEC'

class AddressTaxNumberTypes:
    EORI = 'EORI'
    PID = 'PID'
    VAT = 'VAT'
