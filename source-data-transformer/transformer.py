from numpy import add
import pandas as pd
import json
import collections

df = pd.read_csv ('smalldata.csv')
#print(df)

tmpinvoice = ""

d = collections.defaultdict(dict) 

for index, row in df.iterrows():
#   if index == 0:
#        tmpinvoice = row.InvoiceNo
    
    d['InvoiceNo'] = row.InvoiceNo
    d[row.InvoiceNo][row.StockCode] = row.Description
    
    #if row.InvoiceNo == tmpinvoice:
    #    d[row.InvoiceNo][row.StockCode] = row.Description
    #else:
    #    nix
    #
    
print(d)


#grouped = df.groupby("InvoiceNo")

#for index, row in df.iterrows():
#    print(row)

#result = df.to_json(orient="index")
#parsed = json.loads(result)
#print(parsed)




