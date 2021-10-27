# Highly useful link
# https://pymongo.readthedocs.io/en/stable/tutorial.html
# Figure out indexing later

import requests
import json
from pymongo import MongoClient

# reading the website once - made me realize that there's a format for getting JSON data"
# https://randomuser.me/api/?results=5000 - for 5000 users - watchout and be careful
url = "https://randomuser.me/api/?format=json"
number_of_users = 50

# Returns database object
def setup_db():
    client = MongoClient('localhost', 27017)    # connect to the mondodb daemon
    db = client['random_user_database']         # make a database called 'random_user_database'
    # Tries to make a collection, if already made - just prints out that it already exists
    try:
        db.create_collection('user_collections')    # make a collections in there called user_collections
        print("Created a collection called user_collections")
    except Exception as e:
        print(e.args)
    return db

# Returns JSON dict
def get_user_from_website(website):
    # Here we go - all JSON byte stream in response.content"
    return json.loads(requests.get(website).content)

# returns Object_ID
def insert_user_into_db(db, user):
    db_collection = db.get_collection('user_collections')
    return db_collection.insert_one(user)

if __name__ == "__main__":
    database = setup_db()
    for i in range(number_of_users):
        object_id = insert_user_into_db(database, get_user_from_website(url))
        print("Got a user: ", object_id.inserted_id)


#result = db_collection.find_one({"_id": object_id.inserted_id})  # object_id.inserted_id is not a string
# object_id.inserted_id is a bson object_id object - whatever that is
# and then in the end - there's indexing

# Commands on the mongo client
# > db.user_collections.count() - find total number of users in the collection
# > db.user_collections.find()  - list all the users in the collection
# > db.user_collections.findOne({"_id" : ObjectId("607d6fa7ccedc213f774b07c")}) - find a specific Object ID
# Be careful of spellings and capitalizations of ObjectId - and what's supposed to be string and what's not
# db is not the database name - you choose the database with > use <database_name>