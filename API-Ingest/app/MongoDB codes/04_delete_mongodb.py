import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Function to delete a single document
def delete_single():
   # find the document
    mydict = { "Cusomter_id": "A85123" }

    # delete one document to the collection, if there are MULTIPLE ones it only deletes ONE
    x = mycol.delete_one(mydict)

    # this is the id field of the new document
    print(x.deleted_count, "deleted")

# delete single document
delete_single()