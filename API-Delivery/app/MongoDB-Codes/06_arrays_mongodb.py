import pymongo

# Connect to mongodb
myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')

mydb = myclient["test"] # select the database
mycol = mydb["testcol"] # select the collection

# Look into: https://docs.mongodb.com/manual/reference/operator/update-array/


# Function to insert multiple documents with sub documents at once
def insert_array():
   # create a dummy document

    myquery = {"Cusomter_id": "C84029", "complex_order_items": [{"StockCode" : "22622", "UnitPrice":0.65, "Description":"STARS GIFT TAPE" ,"Quantity" : 3},{"StockCode" : "22326", "UnitPrice":2.95, "Description":"WHITE METAL LANTERN" ,"Quantity" : 1} ]}


    # write the document to the collection
    x = mycol.insert_one(myquery)

    # this is the id field of the new document
    print(x.inserted_id) 

#insert_array()

def query_by_subdocument():
    # find these documents where the StockCode is 22622
    myquery = {"complex_order_items.StockCode": "22622"}
    mydoc = mycol.find( myquery)

    #print out doucument
    for x in mydoc:
        print(x)

#query_by_subdocument()

def add_subdocument_to_array():
    myquery =  {"Cusomter_id": "C84029"}
    newcar = { "$push": {"complex_order_items": {"StockCode" : "22637", "UnitPrice":2.55, "Description":"PIGGY BANK RETROSPOT" ,"Quantity" : 2  }} }

    x = mycol.update_one(myquery,newcar)

    print( x.matched_count , "updated")

    for x in mycol.find(myquery):
        print(x) 

add_subdocument_to_array()