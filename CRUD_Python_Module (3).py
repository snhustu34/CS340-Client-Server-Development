# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'SNHU1234' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://aacuser:SNHU1234@localhost:27017/aac') 
        #access the database and collection
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        #insert a new document into the collection
        if data is not None:
            try:
                self.collection.insert_one(data) # data should be dictionary    
                return True
            except Exception as e:
                print("Insert failed:", e)
                return False
        else: 
            return False

    # Create method to implement the R in CRUD.
    def read(self, query):
        #return documents that match the query 
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print("Read failed:", e)
            return []
        
    
    def update(self, query, new_values):
        #update documents that match the query
        try:
            result = self.collection.update_many(query, {'$set': new_values})
            return result.modified_count
        except Exception as e:
            print("Update failed:", e)
            return 0
        
    def delete(self, query):
        #delete documents that match the query
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print("Delete failed:", e)
            return 0
            