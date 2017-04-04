from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId

class MongoDBManagement:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mongoDatabaseDemo']
        self.collection_employee = self.db['employees']

    def insert_one_employee(self):
        self.collection_employee.insert_one({
            "name": "Nguyen Van A",
            "age": 20,
            "email": "nguyenvana@gmail.com"
        })

    def insert_many_employees(self):
        new_employees = self.collection_employee.insert_many(
            [
                {
                    "name": "Ember Wakens",
                    "age": 20,
                    "email": "emberwakens@gmail.com"
                },
                {
                    "name": "Anna Nguyen",
                    "age": 22,
                    "email": "annanguyen@gmail.com"
                }
            ]
        )

    def update_a_student(self):
        self.collection_employee.find_one_and_update(
            {
                '_id': ObjectId('58e30a55c7a349052310d009')
            },
            {
                '$set': {
                    'name': "Ember Wakens 2"
                }
            },
            projection={'seq': True, '_id': False},
            upsert=True, #upsert = insert if not available
            return_document=ReturnDocument.AFTER
        )

    def find_all_employees(self):
        all_employees = self.collection_employee.find({})
        print("Number of records = " + str(all_employees.count()))
        for each_student in all_employees:
            pprint(each_student)
            
    def delete_an_employee(self):
        self.collection_employee.delete_one({"name": "Anna Nguyen"})

    def drop_employee(self):
        self.collection_employee.drop()

if __name__ == "__main__":
    mongoDB = MongoDBManagement()
    # mongoDB.insert_one_employee()
    # mongoDB.insert_many_employees()
    # mongoDB.update_a_student()
    # mongoDB.find_all_employees()
    # mongoDB.delete_an_employee()
    mongoDB.drop_employee()

