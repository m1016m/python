# -*- coding: utf-8 -*-
"""
py_mongo2.py
Created on Sun Apr 23 14:47:57 2017

@author: HP
"""

#Python to MongoDB
#install MongoDB, install pymongo, import test data -->Python_MongoDB.ppt
#
#Import MongoClient from pymongo.
from pymongo import MongoClient 

#Use MongoClient to create a connection (host:192.168.0.104, port:27017)
client=MongoClient('192.168.0.104:27017')

#To assign the local variable db to the database named test (or #client.test)
db=client['test'] #or db=clinet.test

#db:test, collection:pymongotest
#insert_one(), insert 單筆資料
db.pymongotest.insert_one({"user_id":"A001","age":25})

#insert_many(), insert 多筆資料
db.pymongotest.insert_many([{"user_id":"A002","age":26},{"user_id":"A003","age":28}])

#assign the collection object to a variable for use (or db.restaurants)
coll=db['pymongotest'] #or coll=db.pymongotest

#Query for All Documents in a Collection find()
cursor=coll.find() #collection object coll, coll.find() 

#for 迭代器
for document in cursor: #for 迭代器
    print(document)

#Query 
cursor2=db.pymongotest.find({"age":{"$gt":25}},{"_id":0})

for document in cursor2: #for 迭代器
    print(document)