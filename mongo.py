import pymongo
import os

MONGODB_URI = os.getenv("MONGODB_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_docs = {"first": "Kim", "last": "Shin", "dob": "18/05/1994",
#            "hair_colour": "pink", "occupation": "Train Manufacturer",
#            "nationality": "welsh"}, {"first": "viv", "last": "nue",
#            "dob": "18/05/1994", "hair_colour": "green",
#            "occupation": "city builder", "nationality": "korean"

# coll.insert_many(new_docs)

coll.update_many({"nationality": "welsh"}, {"$set": {"hair_colour": "pink"}})

documents = coll.find({"nationality": "welsh"})

for doc in documents:
    print(doc)
