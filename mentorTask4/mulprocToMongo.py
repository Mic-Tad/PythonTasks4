import csv
import pymongo
import time
import multiprocessing as mp

client = pymongo.MongoClient("localhost:27017")
db = client.dates_and_values
coll = db.Third
coll.delete_many({})

data=[]

with open('./csvfile.csv', newline='') as csvfile:
    csvReader = csv.reader(csvfile) 
    for row in csvReader:
        data.append(row)
chunk_size = 20000
def insert_doc(chunk):
    client = pymongo.MongoClient("localhost:27017")
    db = client.dates_and_values
    coll = db.Third
    for i in chunk:
        coll.insert_one({"Date":i[0],"Value":i[1]})

def chunks(sequence,j):
    yield sequence[j:j + chunk_size]

if __name__ =='__main__':
    procs=[]
    Arr_chunks=[]
    num_of_proc=(len(data)-1)//chunk_size+1
    for j in range(num_of_proc):
        Arr_chunks.append(chunks(data,j*chunk_size,))
    time2s = time.time()
    for j in range(num_of_proc):
        p=mp.Process(target=insert_doc,args=(Arr_chunks[j]))
        p.start()
        procs.append(p)
        
    for i in procs:
        i.join()

    time2f = time.time()
    print(time2f - time2s)
