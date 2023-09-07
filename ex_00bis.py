from pymongo import MongoClient
import json


def create_connection():

    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    # Created or Switched to collection
    # names: GeeksForGeeks
    Countries = db["nobelCountries"]
    Laureates = db["nobelLaureates"]
    Prizes = db["nobelPrizes"]


    with open('D-POO-300_03_nobelCountries.json') as file:
        country_file = json.load(file)

    with open('D-POO-300_03_nobelLaureates.json') as file:
        laureate_file = json.load(file)

    with open('D-POO-300_03_nobelPrizes.json') as file:
        prizes_file = json.load(file)

    # Add countries
    if isinstance(country_file, list):
        Countries.insert_many(country_file)
    else:
        Countries.insert_one(country_file)

    # Add laureates
    if isinstance(laureate_file, list):
        Laureates.insert_many(laureate_file)
    else:
        Laureates.insert_one(laureate_file)

    # Add prizes
    if isinstance(prizes_file, list):
        Prizes.insert_many(prizes_file)
    else:
        Prizes.insert_one(prizes_file)


if __name__ == '__main__':
    create_connection()
