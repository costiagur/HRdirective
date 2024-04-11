import db

def deleterunind(runind):
    mydb = db.MYSQLDB()

    res = mydb.temp_delete(runind)

    if res == 0:
        res = "הוראה לא נמחקה"
    else:
        res = "נמחקו {} הוראות".format(res)
    #

    return res
#