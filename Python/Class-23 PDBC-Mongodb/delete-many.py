from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    user_col=db['users']
    user_col.delete_many({"gender":"Female"})
    print("All Male Users deleted successfully")
except:
    print('Unable to Perform')
finally:
    pass