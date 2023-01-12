import dask.dataframe as dd
import time
import dask_mongo
import pymongo

client = pymongo.MongoClient("localhost:27017")
database = client.dates_and_values
coll = database.Second
coll.delete_many({})

df = dd.read_csv('./csvfile.csv')  
bag=dd.to_bag(df,format='dict')

t=time.time()
dask_mongo.to_mongo(bag=bag,database="dates_and_values",collection="Second",connection_kwargs={"host": "localhost", "port": 27017},)
dt=time.time()-t

print(dt)

coll.update_many( {}, { '$rename': { "date": "Date",'value':'Value' } } )
coll.create_index('Date')
