from pymongo import MongoClient
import json


def display_french_NP():
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
            if element['bornCountryCode'] == "FR":
                if (len(element['prizes'])) > 0:
                    for prizee in element['prizes']:
                        new_list = new_list + [prizee['year'] + ' ' + prizee['category']]
                    #new_list = new_list + [element['prizes']]
        except:
            new_list = new_list

    print(new_list)


if __name__ == '__main__':
    display_french_NP()
