import pymongo
client = pymongo.MongoClient("mongodb+srv://manimnab1:mongodb12345@cluster0.vn0en.mongodb.net/?retryWrites=true&w=majority")
db = client.test#client is connection
print(db)

d={
    'name':'mani',
    'email':'mani123@gmail.com',
    'surname' : 'kumar'
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)