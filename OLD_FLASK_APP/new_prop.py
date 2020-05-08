from pymongo import MongoClient

username = 'Terra925'
password = 'H%40mmond271'
client = MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-paegd.mongodb.net/test?retryWrites=true&w=majority")
db = client.rental_db
collection = db['properties']


def new_property(obj):
    post = {
    'nickname': obj['nickname'],
    'APN': obj['apn'],
    'address': {
        'full_address': f"{obj['inputAddress']} {obj['inputAddress2']} {obj['inputCity']}, {obj['inputState']} {obj['inputZip']}",
        'street_address': obj['inputAddress'],
        'addr_line2': obj['inputAddress2'],
        'city': obj['inputCity'],
        'state': obj['inputState'],
        'zip': obj['inputZip']
    }
    }
    print(post, flush=True);
    id = collection.insert_one(post).inserted_id
    return id
