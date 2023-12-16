from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, password, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = host
        PORT = port
        DB = database
        COL = collection
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # data should be dictionary
            insertDoc = self.database.animals.insert_one(data)  
            # checks to see if the an document was inserted. 
            if insertDoc != 0:
                return True
            else:
                return False
        
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. Note collections value is none by default.
    def read(self, collection=None):
        if collection is not None:
            # retrieved data from the paramater collecition by using the find funciton.
            retrived_Result = self.database.animals.find(collection)
        else:
            # if nothing is passed the whole collection is retrieved. 
            retrived_Result = self.database.animals.find({})
            
        return retrived_Result
    
            