import db

def ordercaps():
    
    mydb = db.MYSQLDB()
    
    reslist = mydb.ordercaps_select()

    res = []

    if len(reslist) == 0:
        res.append("")
    else:
        for eachelem in reslist:
            res.append(eachelem[0].decode('UTF-8'))
        #
    #
    
    return res 
#