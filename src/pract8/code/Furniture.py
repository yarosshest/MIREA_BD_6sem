from console.db.Collection import Collection
from schema import Schema


class Furniture(Collection):
    name = "Furniture"
    schema = Schema({
        "Name": str,
        "Type": str,
        "Material": str,
        "Price": str,
        "Order_id": str,
        "Furniture_Type_id": str
    })

    def __init__(self):
        super().__init__(self.name, self.schema)

    def insertTestData(self):
        print("This table not content test data")
