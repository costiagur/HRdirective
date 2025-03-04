import getpass
import db

def username():
    thisuser = getpass.getuser().lower()
    print(thisuser)
    mydb = db.MYSQLDB()
    
    res = mydb.username_select(thisuser)
    print(res)
    
    if len(res) == 0:
        res = [(0,0)]
    #

    return res 
#