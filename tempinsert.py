import db
from temp_mail import temp_mail

def tempinsert(ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile_bin, reffile_name,listfile_bin,listfile_name):

    mydb = db.MYSQLDB()
    
    res = mydb.temp_insert(ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile_bin,reffile_name,listfile_bin,listfile_name)
   
    if res > 0:
        temp_mail(res,empid,username if isinstance(username,str) else username.decode('UTF-8'))
    #

    return res 
#