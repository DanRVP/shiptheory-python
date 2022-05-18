from datetime import datetime

class AccessToken:

    @property 
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, token: str) -> str:
        self._token = token

    @property 
    def age(self) -> datetime:
        return self._age

    @age.setter
    def age(self, age: datetime) -> datetime:
        self._age = age

    def __init__(self, access_token, token_age):
        self.token = access_token
        self.age = token_age
