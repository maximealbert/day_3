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

    full_list=[]

    for i in range(0, len(total[0]['countries'])-1):
        try:
            #print((total[0]['countries'][i]['name'], total[0]['countries'][i]['code']))
            full_list = full_list + [(total[0]['countries'][i]['name'], total[0]['countries'][i]['code'])]
        except:
            #print((total[0]['countries'][i]['name'], "No code provided"))
            full_list = full_list + [(total[0]['countries'][i]['name'], "No code provided")]

    print(full_list)

def display_categories():

    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelPrizes"]

    myquery = mydocument.find({})

    total = []

    for prize_obj in myquery:
        for prize in prize_obj['prizes']:
            total.append(prize['category'])

    #print(sorted(total))
    test_list = list(set(total))
    print(sorted(test_list))

def display_laureates():
    myclient = MongoClient("mongodb://localhost:27017")

    db = myclient["nobel_database"]

    mydocument = db["nobelLaureates"]

    myquery = mydocument.find({})

    total = []

    for x in myquery:
        total = total + [x]

    #print(total)

    full_list = []

    for i in range(0, len(total[0]['laureates']) - 1):
        try:
            # print((total[0]['countries'][i]['name'], total[0]['countries'][i]['code']))
            full_list = full_list + [total[0]['laureates'][i]['firstname'] + ' ' + total[0]['laureates'][i]['surname']]
        except:
            # print((total[0]['countries'][i]['name'], "No code provided"))
            full_list = full_list + [total[0]['laureates'][i]['firstname']]

    #print(full_list)


    print(sorted(full_list))


if __name__ == '__main__':
    #display_countries()
    display_categories()
    #display_laureates()

