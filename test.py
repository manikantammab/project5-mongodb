from typing import Union, Any, Mapping

import pymongo
from pymongo.database import Database

client = pymongo.MongoClient("mongodb+srv://manimnab1:mongodb12345@cluster0.vn0en.mongodb.net/?retryWrites=true&w=majority")
db = client.test#client is connection
print(db)
data={
    'name':'mani',
    'email':'mani123@gmail.com',
    'subject' : ['data science','big data','data analytics']
}
list_of_records=[
    {'companyName':'Ineuron',
    'product':'Afforable AI',
    'courseOffered':'Machine Learning with Deployment'},

    {'companyName': 'Ineuron',
     'product': 'Afforable AI',
     'courseOffered': 'Deep Learning for NLP with Deployment'},

    {'companyName': 'Ineuron',
     'product': 'Master Program',
     'courseOffered': 'Data Science Masters Program'},
]
database=client['myinfo']#databases
collection=database['test']#collection is nothing but table
collection.insert_one(data)#we acn insert the data
collection.insert_many(list_of_record)

