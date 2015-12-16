__author__ = 'tharinda'

import MySQLdb
import returnDBConnection
class AddMeasure:
    def __init__(self,me_iid=""):
        self.me_iid=me_iid

    def SaveMeasure(self):
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        cur.execute('''INSERT into measurement (me_iid)
                  values (%s)''',
                  (self.me_iid))

        print "Successfully added"
        # Commit your changes in the database
        db.commit()
        # disconnect from server
        db.close()
    def getMeasureId(self):
        db=returnDBConnection.returnDB()
        cur = db.cursor()
        query = "SELECT COUNT(*) from measurement"
        cur.execute(query)             #execute query separately
        res = cur.fetchone()
        total_rows = res[0]      #total rows
        return str(total_rows)