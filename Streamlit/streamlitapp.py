from numpy import double
import streamlit as st
import pandas as pd
import numpy as np

# create a function that will load the csv data, will be cached if nothing changes
@st.cache
def loaddata():
    data = pd.read_csv("data.csv")
    return data

# create empty dataframe
# mydata = pd.DataFrame()

# fill it fom the file
mydata = loaddata()

# Create a first table with a first overview of the data
# Only 20 rows
st.header("Your Data")
table = st.dataframe(data=mydata.head(20))

# Below the fist chart add a input field for the invoice number
inv_no = st.text_input("InvoiceNo:")
#st.text(inv_no)  # Use this to print out the content of the input field

# if enter has been used on the input field 
if inv_no:
    
    # Filter the dataset by the invoice number
    reduced = mydata[mydata["InvoiceNo"] == inv_no]
    
    # Print out the number of found rows
    st.text(len(reduced.index))

    # Add the table with a headline
    st.header("Output by Invoice ID")
    table2 = st.dataframe(data=reduced.head(20))    
    
# Do the same for the customer as with the invoices below.
# Just display the input field in the sidebar
cust_id = st.sidebar.text_input("CustomerID:")

if cust_id:
    reduced_cust = mydata[mydata["CustomerID"] == int(cust_id)]

    st.header("Output by Customer ID")
    table3 = st.dataframe(data=reduced_cust.head(20))


# Create a price slider in the sidebar that will modify a table
slide = st.sidebar.slider('Select min price of item', min_value=0.0, max_value=10000.0, step=0.1)

if slide:
    reduced_cust = mydata[mydata["UnitPrice"] >= slide]

    st.header("Price based on slider")
    table4 = st.dataframe(data=reduced_cust.head(20))













# st.title('Load the data')
# if st.sidebar.button('Load'):
#     mydata = loaddata()

#     table = st.dataframe(data=mydata)
    
#     inv_no = st.sidebar.text_input("InvoiceNo:")
#     #if inv_no:
#     reduced = mydata[mydata["InvoiceNo"] == inv_no]
#     #reduced = data["InvoiceNo"]
#     table2 = st.dataframe(reduced)    
 
# else:
#     st.write('No Data Loaded')

    





# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

