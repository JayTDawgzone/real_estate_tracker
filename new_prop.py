from pymongo import MongoClient

username = 'Terra925'
password = 'H%40mmond271'
client = MongoClient("mongodb+srv://" + username + ":" + password + "@cluster0-paegd.mongodb.net/test?retryWrites=true&w=majority")
db = client.rental_db



def new_property(obj):
    post = {
    'nickname': obj['nickname'],
    'APN': obj['nickname'],
    'address': {
        'full_address': f"{obj['address']} {obj['address2']} {obj['city']}, {obj['state']} {obj['zip']}",
        'street_address': obj['address'],
        'addr_line2': obj['address2'],
        'city': obj['city'],
        'state': obj['state'],
        'zip': obj['zip']
    }
    }
    print(post, flush=True);
