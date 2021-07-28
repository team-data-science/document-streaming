# You need this to use FastAPI, work with statuses and be able to end HTTPExceptions
from fastapi import FastAPI, status, HTTPException

# Both used for BaseModel
from pydantic import BaseModel
from typing import Optional

# You need this to be able to turn classes into JSONs and return
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# import json
# from os import times


class Customer(BaseModel):
    customer_id: str
    country: str
    # city: Optional[str] = None


class URLLink(BaseModel):
    #url: str
    url: Optional[str] = None
    

class Invoice(BaseModel):
    invoice_no: int
    invoice_date: str
    customer: Optional[URLLink] = None

fakeInvoiceTable = dict()

# this is important for general execution and the docker later
app = FastAPI()

# Base URL
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Add a new Customer
@app.post("/customer")
async def create_customer(item: Customer): #body awaits a json with customer information
# This is how to work with and return a item
#   country = item.country
#   return {item.country}

    # You would add here the code for creating a Customer in the database

    # Encode the created customer item if successful into a JSON and return it to the client with 201
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


# Get a customer by customer id
@app.get("/customer/{customer_id}") # Customer ID will be a path parameter
async def read_customer(customer_id: str):
    
    # only succeed if the item is 12345
    if customer_id == "12345" :
        
        # Create a fake customer ( usually you would get this from a database)
        item = Customer(customer_id = "12345", country= "Germany")  
        
        # Encode the customer into JSON and send it back
        json_compatible_item_data = jsonable_encoder(item)
        return JSONResponse(content=json_compatible_item_data)
    else:
        # Raise a 404 exception
        raise HTTPException(status_code=404, detail="Item not found")


# Create a new invoice for a customer
@app.post("/customer/{customer_id}/invoice")
async def create_invoice(customer_id: str, invoice: Invoice):
    
    # Add the customer link to the invoice
    invoice.customer.url = "/customer/" + customer_id
    
    # Turn the invoice instance into a JSON string and store it
    jsonInvoice = jsonable_encoder(invoice)
    fakeInvoiceTable[invoice.invoice_no] = jsonInvoice

    # Read it from the store and return the stored item
    ex_invoice = fakeInvoiceTable[invoice.invoice_no]
    
    return JSONResponse(content=ex_invoice) 



# Return all invoices for a customer
@app.get("/customer/{customer_id}/invoice")
async def get_invoices(customer_id: str):
    
    # Create Links to the actual invoice (get from DB)
    ex_json = { "id_123456" : "/invoice/123456",
                "id_789101" : "/invoice/789101" 
    }
    return JSONResponse(content=ex_json) 



# Return a specific invoice
@app.get("/invoice/{invnoice_no}")
async def read_invoice(invnoice_no: int):
    # Option to manually create an invoice
        #ex_inv = Invoice(invoice_no = invnoice_no, invoice_date= "2021-01-05", customer= URLLink(url = "/customer/12345"))
        #json_compatible_item_data = jsonable_encoder(ex_inv)
    
    # Read invoice from the dictionary
    ex_invoice = fakeInvoiceTable[invnoice_no]

    # Return the JSON that we stored
    return JSONResponse(content=ex_invoice)


#get a specific stock code on the invoice
@app.get("/invoice/{invnoice_no}/{stockcode}/")
async def read_item(invnoice_no: int,stockcode: str):
    return {"message": "Hello World"}

# Add a stockcode to the inovice
@app.post("/invoice/{invnoice_no}/{stockcode}/")
async def add_item(invnoice_no: int ,stockcode:str):
    return {"message": "Hello World"}

