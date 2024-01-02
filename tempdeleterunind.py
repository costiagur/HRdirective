import db

def tempdeleterunind(runind):
    mydb = db.MYSQLDB()

    res = mydb.temp_delete(runind)

    print(res)

    if res == 0:
        res = "הוראה לא נמחקה"
    else:
        res = "נמחקו {} הוראות".format(res)
    #

    return res
#