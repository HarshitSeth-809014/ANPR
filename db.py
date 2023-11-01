from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.ANPR
entryColl = db.Entry
resident = db.Resident


def insert_id(data, time):
    info = {
        "plate": data,
        "time": time
    }
    _ = entryColl.insert_one(info)
    print(_)


def check_resident(data):
    if resident.find_one({"plate": data}):
        return True
    else:
        return False
