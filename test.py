from ShiptheoryPython.Http.Api import *
from ShiptheoryPython.Http.ShiptheoryClient import *
from ShiptheoryPython.Objects.ListShipmentQuery import ListShipmentQuery
from ShiptheoryPython.Objects.PackageQuery import PackageQuery
from ShiptheoryPython.Objects.Product import Product
from ShiptheoryPython.Objects.ProductQuery import ProductQuery, ProductSortParameters
from ShiptheoryPython.Objects.Recipient import Recipient
from ShiptheoryPython.Objects.ReturnLabel import ReturnLabel
from ShiptheoryPython.Objects.SearchShipmentQuery import SearchShipmentQuery
from ShiptheoryPython.Objects.Sender import Sender
from ShiptheoryPython.Objects.Shipment import Shipment
from ShiptheoryPython.Objects.ShipmentDetail import ShipmentDetail
from ShiptheoryPython.Objects.TaxNumber import *

client = ShiptheoryClient('test@test.com', 'Password')

shipment_detail = ShipmentDetail()
shipment_detail.weight = 1
shipment_detail.parcels = 1
shipment_detail.value = 2
shipment_detail.shipping_price = 2.99
shipment_detail.reference3 = 'ORDERREF3'
shipment_detail.sales_source = 'eBay'
shipment_detail.ship_date = '2022-05-22'
shipment_detail.rules_metadata = 'custom string'

recipient = Recipient()
recipient.company = 'Shiptheory'
recipient.firstname = 'Test'
recipient.lastname = 'Customer'
recipient.address_line_1 = 'Unit 4.1 Paintworks'
recipient.address_line_2 = 'Bath Road'
recipient.city = 'Bristol'
recipient.county = 'Avon'
recipient.country = 'GB'
recipient.postcode = 'BS4 3EH'
recipient.email = 'recipient@test.com'
recipient.telephone = '01234567890'
recipient.mobile = '07734567890'
recipient.what3words = '///what.three.words'
eori = TaxNumber('GB205672212000', AddressTaxNumberTypes.EORI)
vat = TaxNumber('GB123456789', AddressTaxNumberTypes.VAT)
recipient.tax_numbers = [eori, vat]

sender = Sender()
sender.company = 'Shipper Inc'
sender.firstname = 'Test'
sender.lastname = 'Shipper'
sender.address_line_1 = 'Bristol Old Vic'
sender.address_line_2 = 'King Street'
sender.city = 'Bristol'
sender.county = 'Avon'
sender.country = 'GB'
sender.postcode = 'BS1 4ED'
sender.email = 'sender@test.com'
sender.telephone = '01234567890'
sender.mobile = '07734567890'

product = Product()
product.name = 'My Test Product'
product.sku = 'TestProd1'
product.qty = 1
product.value = 1
product.weight = 1
product.commodity_code = '8443991000'
product.commodity_manucountry = 'PL'

shipment = Shipment()
shipment.reference = 'S1546'
shipment.reference2 = 'O1445'
shipment.shipment_detail = shipment_detail
shipment.recipient = recipient
shipment.sender = sender
shipment.products = [product]

data = shipment.toJson()
result = client.bookShipment(data)
print('Done')


# View a shipment
result = client.viewShipment('Test1234')
print(vars(result))

# Search shipments
list_fields = {
    'created_from': '2022-04-01',
    'created_to': '2022-04-30',
    'include_products': 1,
}
query = SearchShipmentQuery(list_fields)
params = query.toQueryParams()
result = client.searchShipment(params)
print(vars(result))

# List shipments
list_fields = {
    'channel_name': 'Api',
    'status': 'Ignored',
    'limit': 1
}
query = ListShipmentQuery(list_fields)
params = query.toQueryParams()
result = client.listShipment(params)
print(vars(result))

# Search for packages
list_fields = {
    'length': 25,
    'width': 25,
    'height': 25,
}
query = PackageQuery(list_fields)
params = query.toQueryParams()
result = client.getPackageSizes(params)
print(vars(result))

# List services
result = client.getOutgoingDeliveryServices()
print(vars(result))

# Create a return label
label = ReturnLabel()
label.outgoing_reference = 'Test12345'
label.delivery_postcode = 'BS4 3EH'
label.return_service = 1
label.expiry = '2023-05-30'
result = client.createReturnLabel(label.toJson())
print(vars(result))

# Create a new product
product = Product()
product.sku = 'APIProd1'
product.name = 'API Test Product'
product.price = 1.99
product.weight = 1.25
product.barcode = '123456789'
product.commodity_code = '8443991000'
product.commodity_manucountry = 'GB'
product.commodity_description = 'This is a test product'
product.commodity_composition = 'Electronic components'
product.length = 25
product.width = 11.55
product.height = 4.66
result = client.addProduct(product.toJson())
print(vars(result))

# View a product
result = client.viewProduct('APIProd1')
print(vars(result))

# Update a product
product = Product()
product.price = 5.99
result = client.updateProduct('API-Product-1', product.toJson())
print(vars(result))

# List for products
list_fields = {
    'sort': ProductSortParameters.SKU,
    'limit': 5,
}
query = ProductQuery(list_fields)
params = query.toQueryParams()
result = client.listProducts(params)
print(vars(result))
