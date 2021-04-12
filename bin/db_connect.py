#this file contans functions for database connections
def mongodb_connect(db_name, password, db_url):
    #create a pymongo connection
    
    client = pymongo.MongoClient("mongodb+srv://dataconnect:<password>@cluster0.jligz.azure.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test