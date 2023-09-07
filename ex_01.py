from pymongo import MongoClient
import mongoengine as me


def create_connection():
    client = MongoClient("localhost", 27017)
    db = client.nobel_database
    collection = db.myelements
    print(collection)


me.connect("nobel_database", "mongodb://localhost:27017")


class Country(me.Document):
    name = me.StringField(required=True, unique=True)
    code = me.StringField(required=True, unique=True, max_length=10)


class Person(me.Document):
    name = me.StringField(required=True, unique=True)
    firstName = me.StringField(required=True, unique=False)
    age = me.IntField(required=False)
    nationality = me.ReferenceField(Country)


class Prize(me.Document):
    name = me.StringField(required=True, unique=False)
    year = me.IntField(required=True, unique=False)
    laureates = me.ListField(me.ReferenceField(Person))


class Category(me.Document):
    name = me.StringField(required=True, unique=False)


class Affiliation(me.EmbeddedDocument):
    name = me.StringField(required=True, unique=True)
    country = me.ReferenceField(Country)


if __name__ == '__main__':
    usa = Country(name='United States of America', code='USA')
    usa.save()
    sweden = Country(name='Suede', code='SWE')
    sweden.save()

    physics = Category(name='Physics')
    physics.save()
    mathematics = Category(name='Mathematics')
    mathematics.save()

    #mit = Affiliation(name='MIT Institute', country=usa)
    #harvard = Affiliation(name='Harvard School', country=sweden)

    #person1 = Person(name='Maxime', firstname='ALBERT', age=20, nationality=usa)
    #person2 = Person(name='Ambre', firstname='FLAMENT', age=30, nationality=sweden)

    #nobel_physics = Prize(name='Physics Nobel Prize', year=2022, laureates=[person1, person2])
   # nobel_physics.save()
