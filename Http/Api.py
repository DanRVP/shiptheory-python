from Http.AccessToken import AccessToken
from Http.ResponseObject import Response
import requests

class Api:
    _BASE_URL = 'https://api.shiptheory.com/v1/'
    _headers = {
            'User-Agent': 'Shiptheory Python',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def __init__(self, token: AccessToken = None):
        if (token and isinstance(token.token, str)):
            self._headers['Authorization'] = 'Bearer ' + token.token

    def get(self, endpoint: str) -> Response:
        """ 
        Sends a get request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :return `Response`: object
        """
        url = self._BASE_URL + endpoint        
        response = Response()
        res = requests.get(url, headers = self._headers)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            return response
        
        response.body = res.json()
        return response

    def post(self, endpoint: str, data: str) -> Response:
        """ 
        Sends a post request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :param `data`: JSON string of data
        :return `Response`: object
        """
        url = self._BASE_URL + endpoint        
        response = Response()
        res = requests.post(url, headers=self._headers, data=data)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            return response
        
        response.body = res.json()
        return response

    def put(self, endpoint: str, data: str) -> Response:
        """ 
        Sends a put request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :param `data`: JSON string of data
        :return `Response`: object
        """
        url = self._BASE_URL + endpoint        
        response = Response()
        res = requests.put(url, headers=self._headers, data=data)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            return response
        
        response.body = res.json()
        return response
