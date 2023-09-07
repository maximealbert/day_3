import pymongo
from pymongo import MongoClient

def create_connection():
    client = MongoClient("localhost", 27017)
    db = client.nobel_database
    collection = db.myelements
    print(collection)


if __name__ == '__main__':
    create_connection()
