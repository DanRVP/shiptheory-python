from src.Http.Api import *
from src.Http.ShiptheoryClient import *

client = ShiptheoryClient('test@test.com', 'Password')
data = {
    "reference": "I1445",
    "reference2": "International",
    "shipment_detail": {
        "weight": 1,
        "parcels": 1,
        "value": 2,
        "shipping_price": 2.99,
        "reference3": "ORDERREF3",
        "sales_source": "eBay",
        "ship_date": "2023-02-22",
        "rules_metadata": "custom string"
    },
    "recipient": {
        "company": "Beard Supplies Co",
        "firstname": "Dan",
        "lastname": "Rogers",
        "address_line_1": "123 Southpaw Lane",
        "city": "Berlin",
        "county": "Berlin",
        "postcode": "10117",
        "telephone": "01161231245",
        "email": "test@test.com",
        "country": "DE",
        "what3words": "what.three.words",
        "tax_numbers": [
        {
            "tax_number_type": "EORI",
            "tax_number": "GB205672212000"
        },
        {
            "tax_number_type": "VAT",
            "tax_number": "GB123456789"
        },
        {
            "tax_number_type": "PID",
            "tax_number": "PID123456789"
        }
    ]
    },
    "sender": {
        "company": "Hair Wholersaler Co.",
        "firstname": "Julian",
        "lastname": "Bashir",
        "address_line_1": "65 Horfield Retail Park",
        "city": "Bath",
        "county": "BANES",
        "postcode": "BA1 2JW",
        "telephone": "01161231211",
        "email": "test@test.com",
        "country": "GB"
    },
    "products": [{
        "name": "API products",
        "sku": "APIPROD1",
        "qty": 1,
        "value": 1,
        "weight": 1,
        "commodity_code": "61044900",
        "commodity_manucountry": "GB",
        "commodity_description": "Stuff n junk"
    }]
}

result = client.bookShipment(data)
print('Done')
