import getpass
import db

def username():
    thisuser = getpass.getuser()
    
    mydb = db.MYSQLDB()
    
    res = mydb.username_select(thisuser)
    
    if len(res) == 0:
        res = [(0,0)]
    #

    return res 
#