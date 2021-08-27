import numpy as np
from numpy import add
import pandas as pd


df = pd.read_csv ('data.csv') 
#print(df)

# add a json column to the dataframe
# splitlines will split the json into multiple rows not a single one
df['json'] = df.to_json(orient='records', lines=True).splitlines()
#print(df)

# just take the json column of the dataframe
dfjson = df['json']
print(dfjson)

# print out the dataframe to a file
# Note that the timestamp forward slash will be escaped to stay true to JSON schema
np.savetxt(r'./output.txt', dfjson.values, fmt='%s')
