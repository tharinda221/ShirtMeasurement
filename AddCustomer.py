__author__ = 'tharinda'

import returnDBConnection
class AddCustomer:
    def __init__(self, cid="", firstname="", lastname="", age="", contactnumber="", address=""):
        self.cid = cid
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.contactnumber = contactnumber
        self.address = address

    def saveToDB(self):

        db=returnDBConnection.returnDB()
        cur = db.cursor()

        cur.execute('''INSERT into customer (firstname,lastname,age,contactnumber,address)
                  values (%s, %s, %s, %s, %s)''',
                  (self.firstname, self.lastname,self.age,self.contactnumber,self.address))

        print "Successfully added"
        # Commit your changes in the database
        db.commit()
        # disconnect from server
        db.close()

    def searchCustomers(self):
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        cur.execute("SELECT * FROM customer")
        result=cur.fetchall()
        return result
    @staticmethod
    def getCID():
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        query = "SELECT COUNT(*) from customer"
        cur.execute(query)             #execute query separately
        res = cur.fetchone()
        total_rows = res[0]      #total rows
        return str(total_rows)
    @staticmethod
    def getDataInVoice():
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        cid=AddCustomer.getCID()
        cur.execute("SELECT cid,firstname,lastname FROM customer WHERE cid="+cid)
        result=cur.fetchall()
        return result

