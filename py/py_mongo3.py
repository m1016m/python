# -*- coding: utf-8 -*-
"""
py_mongo3.py
Created on Sun Apr 23 16:57:04 2017

@author: zzjack
"""
from pymongo import MongoClient

#Making a Connection with MongoClient
cn=MongoClient("127.0.0.1:27017") 
   #cn=MongoClient("127.0.0.1",27017)
   #cn=MongoClient("mongodb://localhost:27017/")
   
#Getting a Database
db=cn.test
   #db=cn['test']
   
#Getting a Collection
coll=db.pymongotest
   #coll=db['pymongotest']
   
#Inserting a Document
#In PyMongo we use dictionaries to represent documents.
import datetime
post = {"author": "Jack",
        "text":"My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

#insert_one()
coll.insert_one(post)

posts=[{"author":"Mary","tags":["java","c#"]},
       {"author":"John","tags":["sql","js"]}]

#insert_many()
coll.insert_many(posts)

#Getting a Single Document With find_one()
s1=db.pymongotest.find_one()
print(s1)

s2=db.pymongotest.find_one({"author":"Jack"},{"_id":0})

#Querying for More Than One Document, find()
#find() returns a Cursor instance
c1=db.pymongotest.find({},{"_id":0})

for doc in c1:
    print(doc)




