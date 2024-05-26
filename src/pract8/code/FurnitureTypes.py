from console.db.Collection import Collection
from schema import Schema


class FurnitureTypes(Collection):
    name = "FurnitureTypes"
    schema = Schema({
        "Name": str,
        "Description": str
    })

    def __init__(self):
        super().__init__(self.name, self.schema)

    def insertTestData(self):
        super().insert([
            {"Name": "Chair", "Description": "A piece of furniture designed for one person to sit on."},
            {"Name": "Table",
             "Description": "A piece of furniture with a flat top and one or more legs, used as a surface for working, eating, etc."},
            {"Name": "Sofa",
             "Description": "A comfortable seating furniture for multiple people, typically found in living rooms."},
            {"Name": "Bed",
             "Description": "A piece of furniture for sleep or rest, typically a framework with a mattress."},
            {"Name": "Cabinet", "Description": "A piece of furniture with doors and shelves used for storage."},
            {"Name": "Desk",
             "Description": "A piece of furniture with a flat top for writing, reading, or using a computer."},
            {"Name": "Shelf", "Description": "A flat horizontal plane used for storing or displaying items."},
            {"Name": "Stool", "Description": "A simple seat without back or arms, typically for one person."},
            {"Name": "Wardrobe", "Description": "A large, tall cupboard or closet used for storing clothes."},
            {"Name": "Bookcase", "Description": "A piece of furniture with shelves for storing books."},
        ])
        print("FurnitureTypes test data inserted")
