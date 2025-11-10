import requests,json,csv
fp1=open("emp.json",'w')
fp2=open("emp.json",'w',newline="")
#extract data from rest api
user_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=user_resp.json()
print(users)