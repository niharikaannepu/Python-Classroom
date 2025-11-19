from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db4']
    
    
    
    
except:
    pass


finally:
    pass