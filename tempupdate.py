import db

def tempupdate(runind,ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile,filename):
   
    mydb = db.MYSQLDB()
    
    res = mydb.temp_update(runind,empid, addressee, ordercap, startdate, enddate, ordtxt, reftxt, username, reffile,filename,0)
   
    print(res)

    return res 
#