from src.Http.AccessToken import AccessToken
from src.Http.Api import Api
import datetime

class ShiptheoryClient:
    
    ##############
    # Properties #
    ##############
    @property 
    def token(self) -> AccessToken:
        return self._token

    @token.setter
    def token(self, token: AccessToken) -> AccessToken:
        self._token = token

    @property 
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> str:
        self._username = username

    @property 
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str) -> str:
        self._password = password

    ###########
    # Methods #
    ###########

    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def getAccessToken(self):
        data = {
            'email': self.username,
            'password': self.password,
        }

        api = Api()
        response = api.post('token', data)

        if (response.code == 200):
            token = response.body['data']['token']
            print(token)
            self.token = AccessToken(token, datetime.datetime.now())
            return True
        
        return False