import db

def tempinsert(ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile,filename):
   
    mydb = db.MYSQLDB()
    
    res = mydb.temp_insert(ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile,filename,0)
   
    print(res)

    return res 
#