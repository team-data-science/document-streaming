import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Look into: https://docs.mongodb.com/manual/reference/operator/update-field/

# Function to insert multiple documents with sub documents at once
def insert_multiple():
   # create a dummy document
    mylist = []

    mylist.append({ "Cusomter_id": "15311", "Country": "US", "simple_order_items": {"StockCode":"21791","UnitPrice":0.65, "Description":"STARS GIFT TAPE" ,"Quantity" : 3} })
    mylist.append({ "Cusomter_id": "14527", "Country": "US", "simple_order_items": {"StockCode":"21792","UnitPrice":2.95, "Description":"WHITE METAL LANTERN" ,"Quantity" : 1} })



    # write the document to the collection
    x = mycol.insert_many(mylist)

    # this is the id field of the new document
    print(x.inserted_ids) 

#insert_multiple()

def query_sub_document():
    # find these documents where the StockCode is 21791
    myquery = {"simple_order_items.StockCode": "21791"}
    mydoc = mycol.find( myquery)

    # return only specific parts of the document
    #myreturnonly = { "_id": 0, "name": 1}
    #mydoc = mycol.find( myquery, myreturnonly )

    #print out doucument
    for x in mydoc:
        print(x)

#query_sub_document()


# update a stock code of a sub document
def update_sub_document():
    myquery = { "Cusomter_id": "15311"}
    newvalues = { "$set": { "simple_order_items.StockCode": "22778" } }

    x = mycol.update_one(myquery, newvalues)   

    for x in mycol.find():
        print(x) 

update_sub_document()