from ShiptheoryPython.Http.AccessToken import AccessToken
from ShiptheoryPython.Http.Api import Api
import datetime
from ShiptheoryPython.Http.ResponseObject import Response
import json

class ShiptheoryClient:
    
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

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
        self.token = None

    def getAccessToken(self) -> bool:
        """ Gets an access token from shiptheory via post request. """
        data = json.dumps({
            'email': self.username,
            'password': self.password,
        })

        api = Api()
        response = api.post('token', data)

        if (response.code == 200):
            token = response.body['data']['token']
            self.token = AccessToken(token, datetime.datetime.now())
            return True
        
        return False

    def validateToken(self) -> bool:
        """ Checks if an access token exists and is still within a valid timeframe. """
        if (self.token in ['', None] or self.__checkTokenLifeExpired(self.token)):
            return self.getAccessToken()

        return True

    def __checkTokenLifeExpired(self, token: AccessToken) -> bool:
        """ 
        Checks if the token is younger than 58 minutes in age. 
        @param AccessToken `token` - The token object to check.
        """
        now = datetime.datetime.now()
        diff = (now - token.age)
        mins_diff = (diff.total_seconds() / 60)

        return mins_diff > 58

    def bookShipment(self, data: str) -> Response:
        """ 
        Book in a shipment with Shiptheory.
        @param dict `data` Data to book with.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.post('shipments', data)

    def viewShipment(self, reference: str) -> Response:
        """ 
        View a shipment 
        @param str `reference` The unique reference used when creating the shipment.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('shipments/' + reference)

    def listShipment(self, query_params: str) -> Response:
        """ 
        Calls the shipment/list API endpoint and returns a result. 
        @param str `query_params` URL query params to filter by.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('shipments/list' + query_params)
    
    def searchShipment(self, query_params: str) -> Response:
        """ 
        Calls the shipment/search API endpoint and returns a result. 
        @param str `query_params` URL query params to filter by.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('shipments/search' + query_params)

    def createReturnLabel(self, data: str) -> Response:
        """ 
        Create a new return label.
        @param dict `data` Data to book with.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.post('returns', data)

    def getOutgoingDeliveryServices(self) -> Response:
        """ 
        Get a list of outgoing delivery services.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('services')

    def getIncomingDeliveryServices(self) -> Response:
        """ 
        Get a list of incoming delivery services.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('services/incoming')

    def getPackageSizes(self, query_params: str) -> Response:
        """ 
        Get a list of package sizes.
        @param str `query_params` URL query params to filter by.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('packages/sizes' + query_params)

    def addProduct(self, data: str) -> Response:
        """ 
        Add a new product.
        @param dict `data` Data to add product with.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.post('products', data)

    def updateProduct(self, sku: str, data: str) -> Response:
        """ 
        Uppdate a product.
        @param str `sku` Unique product sku.
        @param dict `data` Data to update product with.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.put('products/update/' + sku, data)

    def viewProduct(self, sku: str) -> Response:
        """ 
        View a product from your product catalouge.
        @param str `sku` Unique product sku.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('products/view/' + sku)

    def listProducts(self, query_params: str) -> Response:
        """ 
        View a list of products from your product catalouge.
        @param str `query_params` URL query params to filter by.
        """
        if (self.validateToken() == False):
            return False

        api = Api(self.token)
        return api.get('products' + query_params)
