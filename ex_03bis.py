from pymongo import MongoClient
import json

def display_chemistry_NP(country):
    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelLaureates"]

    myquery = mydocument.find({})

    total = []

    for x in myquery:
        total = total + [x]

    full_list = []

    for element in total[0]['laureates']:
        try:
            if element['bornCountryCode'] == country:
                if (len(element['prizes'])) > 0:

                    for prizee in element['prizes']:
                        if prizee['category'] == "chemistry":
                            try:
                                full_list = full_list + [element['firstname'] + ' ' + element['surname']]
                            except:
                                full_list = full_list + [element['firstname']]


        except:
            total = total

    print(full_list)


if __name__ == '__main__':
    display_chemistry_NP('FR')
