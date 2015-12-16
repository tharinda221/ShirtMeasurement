__author__ = 'tharinda'
from databaseConnection import databaseConnecton
def returnDB():
    database=databaseConnecton(host="localhost", user="root",passwd="tharinda",db="measurementApp")
    db=database.createConnection()
    return db