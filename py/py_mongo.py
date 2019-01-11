#Python to MongoDB
#install MongoDB, install pymongo, import test data -->Python_MongoDB.ppt
#
#Import MongoClient from pymongo.
from pymongo import MongoClient 

#Use MongoClient to create a connection
client=MongoClient('127.0.0.1:27017')

#To assign the local variable db to the database named test (or #client.test)
db=client['test']

#assign the collection object to a variable for use (or db.restaurants)
coll=db['restaurants']

#Query for All Documents in a Collection find()
cursor=coll.find() #collection object coll, coll.find() 

#for 迭代器
for document in cursor: #for 迭代器
    print(document)

#Query by a Top Level Field
cursor2 = db.restaurants.find({"borough": "Manhattan"})

for document in cursor2: #for 迭代器
    print(document)