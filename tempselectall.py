import db
import datetime

def tempselectall(empid=0):
    mydb = db.MYSQLDB()
    
    res = mydb.temp_select_all(empid)
    reslist = []

    for eachrow in res:
        resdict = dict()

        resdict["runind"] = eachrow[0]
        resdict["empid"] = eachrow[1]
        resdict["addressee"] = eachrow[2].decode('UTF-8')
        resdict["ordercapt"] = eachrow[3].decode('UTF-8')
        resdict["startdate"] = datetime.datetime.strftime(eachrow[4],"%d/%m/%Y")
        resdict["enddate"] = datetime.datetime.strftime(eachrow[5],"%d/%m/%Y")
        resdict["ordertext"] = eachrow[6].decode('UTF-8')
        resdict["username"] = eachrow[7].decode('UTF-8')
        resdict["filename"] = eachrow[8].decode('UTF-8') if eachrow[8] != None else ""
        resdict["ordertime"] = datetime.datetime.strftime(eachrow[9],"%d/%m/%Y %H:%M")
        resdict["state"] = eachrow[10]

        reslist.append(resdict)

    #
    return reslist
#