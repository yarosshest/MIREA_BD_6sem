from console.db.Collection import Collection
from schema import Schema


class Order(Collection):
    name = "Order"
    schema = Schema({
        "DeadLine": str,
        "User_id": str
    })

    def __init__(self):
        super().__init__(self.name, self.schema)

    def insertTestData(self):
        print("This table not content test data")
