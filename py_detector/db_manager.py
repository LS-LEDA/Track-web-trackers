import datetime
import pymongo
from dotenv import dotenv_values

config = dotenv_values('.env')
myclient = pymongo.MongoClient(config['MONGO_HOST'])

mydb = myclient[config['DB_NAME']]


def get_stored_url(url):
    mycol = mydb[config['SITES_COLLECTION']]
    myquery = {"url": url}

    cur = mycol.find(myquery)

    results = list(cur)

    if len(results) == 0:
        return None
    return results[0]


def store_url(url, trackers):
    mycol = mydb[config['SITES_COLLECTION']]
    mycol.insert_one({"url": url, "trackers": trackers,
                     "date": datetime.datetime.now()})


def update_url(trackers, _id):
    mycol = mydb[config['SITES_COLLECTION']]
    myquery = {"_id": _id}
    newvalues = {"$set": {"trackers": trackers,
                          "date": datetime.datetime.now()}}
    mycol.update_one(myquery, newvalues)
