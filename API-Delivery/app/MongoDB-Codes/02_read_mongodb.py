import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/",username='root',password='example')
mydb = myclient["test"]
mycol = mydb["testcol"]

# find these documents where the customer_id equals A85123
myquery = {"Cusomter_id": "A85123"}
mydoc = mycol.find( myquery )

# return only specific parts of the document
#myreturnonly = { "_id": 0, "Cusomter_id": 1}
#mydoc = mycol.find( myquery, myreturnonly )

#print out doucument
for x in mydoc:
  print(x)

# how to sort the data that you will retrieve
# find order ASC .sort("Cusomter_id") or .sort("Cusomter_id", 1)
# find order DSC .sort("Cusomter_id",-1)  