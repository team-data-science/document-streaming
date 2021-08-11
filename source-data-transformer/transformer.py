import numpy as np
from numpy import add
import pandas as pd


df = pd.read_csv ('smalldata.csv') 
#print(df)

# add a json column to the dataframe
# splitlines will split the json into multiple rows not a single one
df['json'] = df.to_json(orient='records', lines=True).splitlines()

# just take the json column of the dataframe
dfjson = df['json']

# print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')



#

#d = collections.defaultdict(dict) 

#for index, row in df.iterrows():
#   if index == 0:
#        tmpinvoice = row.InvoiceNo
    
#    d['InvoiceNo'] = row.InvoiceNo
#    d[row.InvoiceNo][row.StockCode] = row.Description
    
    #if row.InvoiceNo == tmpinvoice:
    #    d[row.InvoiceNo][row.StockCode] = row.Description
    #else:
    #    nix
    #
    
#print(d)


#grouped = df.groupby("InvoiceNo")

#for index, row in df.iterrows():
#    print(row)

#result = df.to_json(orient="index")
#parsed = json.loads(result)
#print(parsed)




