import csv
import pymongo
import time

client = pymongo.MongoClient("localhost:27017")
db = client.dates_and_values
coll = db.First

with open('./csvfile.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile)
    coll.delete_many({})

    t=time.time()
    for row in csvReader:
        coll.insert_one({'Date':row[0],'Value':row[1]})
    dt=time.time()-t

    coll.create_index('Date')
    coll.delete_one({'Date':'date'})

print(dt)