from src.Objects.Address import Address

class Recipient(Address):
    
    @property 
    def tax_numbers(self) -> list:
        return self._tax_numbers

    @tax_numbers.setter
    def tax_numbers(self, tax_numbers: list):
        self._tax_numbers = tax_numbers

    @property 
    def what3words(self) -> str:
        return self._what3words

    @what3words.setter
    def what3words(self, what3words: str):
        self._what3words = what3words
