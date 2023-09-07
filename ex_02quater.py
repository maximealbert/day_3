from pymongo import MongoClient
import json


def display_multiple_laureates():
    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelLaureates"]

    myquery = mydocument.find({})

    total = []

    for x in myquery:
        total = total + [x]

    new_list = []

    for element in total[0]['laureates']:
        try:
            if (len(element['prizes'])) > 1:
                try:
                    new_list = new_list + [element['firstname'] + ' ' + element['surname']]
                except:
                    new_list = new_list + [element['firstname']]
        except:
            new_list = new_list

    print(new_list)

if __name__ == '__main__':
    display_multiple_laureates()