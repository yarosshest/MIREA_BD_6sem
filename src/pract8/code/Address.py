from console.db.Collection import Collection
from schema import Schema


class Address(Collection):
    name = "Address"
    schema = Schema({
        "Street": str,
        "City": str,
        "Postal_Code": str,
        "Country": str,
        "Order_id": str
    })

    def __init__(self):
        super().__init__(self.name, self.schema)

    def insertTestData(self):
        print("This table not content test data")
