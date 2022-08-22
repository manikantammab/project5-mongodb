import pymongo
client = pymongo.MongoClient("mongodb+srv://manimnab1:mongodb12345@cluster0.vn0en.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database=client['myinfo']
collection=database['test']

#data=collection.find({'companyName':'INeuron'})
data=collection.find({'courseOffered':{'$gt':'E'}})
for i in data:
    print(i)