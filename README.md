Creates custom .csv file to write it into mongoDB in 3 different ways:
- by reading from .csv file and writing each row into mongodb with one process
- by reading from .csv file and writing each row into mongodb with several processes 
- by putting data from file into dask bag and putting data from this bag into mongoDB with dask_mongo
