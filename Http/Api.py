from ResponseObject import Response
import requests

class Api:

    def __init__(self, token = None):
        self.api_token = token

    def get(self, endpoint):
        """ Sends a get request to the specified endpoint of the Shiptheory API
        :param `self`:
        :param `token`: Bearer token
        :return `Response`: object
        """
        url = self.BASE_URL + endpoint
        headers = {
            'User-Agent': 'Shiptheory Python',
            'Authorization': 'Bearer ' + self.api_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = Response()
        res = requests.get(url, headers=headers)
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
