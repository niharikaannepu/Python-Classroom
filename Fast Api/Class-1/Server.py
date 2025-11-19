from fastapi import FastAPI

app=FastAPI()
'''
Usage:Application Root Req
Rest API URL:http://127.0.0.1:8000
Method Type:GET
Required Fields:None 
Access Type:Public
'''
@app.get("/")
def index_page():
    return {"message":"Application Root request"}

'''
Create
------
usage:create new user 
Rest API URL: http://127.0.0.1:8000/create 
Method Type:POST
Required Fiels: uid,uname,email
Access Type:Public
'''
@app.post("/create")
def create_User():
    return {"message":"User Created Successfully"}

