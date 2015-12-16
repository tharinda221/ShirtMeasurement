__author__ = 'tharinda'
import MySQLdb
class databaseConnecton:
    def __init__(self,host="",user="",passwd="",db=""):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.db=db
    def createConnection(self):
        db = MySQLdb.connect(host=self.host, user=self.user,passwd=self.passwd,db=self.db)
        print "Connected to the database"
        return db
