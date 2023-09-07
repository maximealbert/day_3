from pymongo import MongoClient
import json


def display_countries():
    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelCountries"]

    myquery = mydocument.find({})

    total = []

    for x in myquery:
        total = total + [x]

    full_list = []

    for i in range(0, len(total[0]['countries']) - 1):
        try:
            # print((total[0]['countries'][i]['name'], total[0]['countries'][i]['code']))
            full_list = full_list + [(total[0]['countries'][i]['name'], total[0]['countries'][i]['code'])]
        except:
            # print((total[0]['countries'][i]['name'], "No code provided"))
            full_list = full_list + [(total[0]['countries'][i]['name'], "No code provided")]

    print(full_list)


def display_shared_peace_NP():
    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelPrizes"]

    myquery = mydocument.find({})

    total = []

    for x in myquery:
        total = total + [x]

    peace_list = []
    # print(total[0]['prizes'])
    for element in total[0]['prizes']:
        if element['category'] == 'peace':
            try:
                if (element['laureates'][0]['share']) == "2":
                    peace_list = peace_list + [element['category'] + ' '+element['year']]
                    #print(element['laureates'][0]['share'])


            except:
                peace_list = peace_list

    print(peace_list)


if __name__ == '__main__':
    display_shared_peace_NP()
