from datetime import datetime

class AccessToken:

    def __init__(self, token, age):
        self.token = token
        self.age = age

    @property 
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, token: str) -> str:
        self._token = token

    @property 
    def age(self) -> datetime:
        return self._age

    @token.setter
    def age(self, age: datetime) -> datetime:
        self._age = age
