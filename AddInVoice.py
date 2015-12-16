__author__ = 'tharinda'
import returnDBConnection
class AddInVoice:
    def __init__(self, iv_cid="" ,submitdata="", requiredate="", quantity="", price=""):
        self.iv_cid=iv_cid
        self.submitdata = submitdata
        self.requiredate = requiredate
        self.quantity = quantity
        self.price= price
    def saveInVoice(self):
        db=returnDBConnection.returnDB()
        cur = db.cursor()

        cur.execute('''INSERT into invoice (iv_cid,submitdata,requiredate,quantity,price)
                  values (%s, %s, %s, %s, %s)''',
                  (self.iv_cid,self.submitdata, self.requiredate,self.quantity,self.price))

        print "Successfully added"
        # Commit your changes in the database
        db.commit()
        # disconnect from server
        db.close()
    @staticmethod
    def getIID():
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        query = "SELECT COUNT(*) from invoice"
        cur.execute(query)             #execute query separately
        res = cur.fetchone()
        total_rows = res[0]      #total rows
        return str(total_rows)
    @staticmethod
    def InVoiceList():
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        cur.execute("SELECT iid,firstname,lastname,submitdata,requiredate,quantity,price FROM customer,invoice WHERE iv_cid=cid")
        result=cur.fetchall()
        return result
    @staticmethod
    def getFLNames():
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        cur.execute("SELECT firstname,lastname,iid FROM customer,invoice WHERE iv_cid=cid AND iid="+AddInVoice.getIID())
        result=cur.fetchall()
        return result