from src.Http.ResponseObject import Response
import requests

class Api:

    def __init__(self, token = None):
        self.api_token = token

    def get(self, endpoint):
        """ Sends a get request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :return `Response`: object
        """
        url = self.BASE_URL + endpoint        
        response = Response()
        res = requests.get(url, headers = self.headers)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            print(vars(response))
            return response
        
        response.body = res.json()
        return response

    def post(self, endpoint, data):
        """ Sends a post request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :return `Response`: object
        """
        url = self.BASE_URL + endpoint        
        response = Response()
        res = requests.post(url, headers=self.headers, json=data)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            print(vars(response))
            return response
        
        response.body = res.json()
        return response

    def put(self, endpoint, data):
        """ Sends a put request to the specified endpoint of the Shiptheory API
        :param `endpoint`: Endpoint to hit
        :return `Response`: object
        """
        url = self.BASE_URL + endpoint        
        response = Response()
        res = requests.put(url, headers=self.headers, json=data)
        response.url = res.url
        response.code = res.status_code

        if (response.code != 200):
            response.error = res.json()
            print(vars(response))
            return response
        
        response.body = res.json()
        return response

    @property
    def api_token(self):
        return self._api_token

    @api_token.setter
    def api_token(self, token):
        self._api_token = token

    @property
    def BASE_URL(self):
        return 'https://api.shiptheory.com/v1/'

    @property
    def headers(self):
        headers = {
            'User-Agent': 'Shiptheory Python',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        if (type(self.api_token) is str):
            headers['Authorization'] = 'Bearer ' + self.api_token

        return headers
