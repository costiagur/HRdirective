import db
from temp_mail import temp_mail

def tempupdate(runind,ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile_bin,reffile_name,listfile_bin,listfile_name):
   
    mydb = db.MYSQLDB()
    
    res = mydb.temp_update(runind,empid, addressee, ordercap, startdate, enddate, ordtxt, reftxt, username, reffile_bin,reffile_name,listfile_bin,listfile_name)
   
    if res > 0:
        temp_mail(runind,empid,username if isinstance(username,str) else username.decode('UTF-8'))
    #
        
    return res 
#