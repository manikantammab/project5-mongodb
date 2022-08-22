import pymongo
client = pymongo.MongoClient("mongodb+srv://manimnab1:mongodb12345@cluster0.vn0en.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['inventory']
collection=database['electricals']
data=[
{ "name": "xPhone", "price": 799, "releaseDate": "2011-05-14",
 "spec": {"ram": 4, "screen": 6.5, "cpu": 2.66}, "color": ["white", "black"], "storage": [64, 128, 256]},
{ "name": "xTablet", "price": 899, "releaseDate": "2011-09-01",
 "spec": {"ram": 16, "screen": 9.5, "cpu": 3.66}, "color": ["white", "black", "purple"], "storage": [128, 256, 512]},
{ "name": "SmartTablet", "price": 899, "releaseDate": "2015-01-14",
 "spec": {"ram": 12, "screen": 9.7, "cpu": 3.66}, "color": ["blue"], "storage": [16, 64, 128]},
{ "name": "SmartPad", "price": 699, "releaseDate": "2020-05-14",
 "spec": {"ram": 8, "screen": 9.7, "cpu": 1.66}, "color": ["white", "orange", "gold", "gray"],
 "storage": [128, 256, 1024]},
{ "name": "SmartPhone", "price": 599, "releaseDate": "2022-09-14",
 "spec": {"ram": 4, "screen": 9.7, "cpu": 1.66}, "color": ["white", "orange", "gold", "gray"], "storage": [128, 256]},
]
collection.insert_many(data)
#d=collection.find({'price':{'$lt':799}})
#d=collection.find({'storage':{'$lt':128}})
#d=collection.find({'price':{'$gt':799}})

for i in d:
    print(i)
