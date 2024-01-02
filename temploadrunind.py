import db
import datetime

def temploadrunind(runind):
    mydb = db.MYSQLDB()
    
    res = mydb.temp_load_runind(runind)[0]
    resdict = dict()

    print(res)

    resdict["runind"] = res[0]
    resdict["empid"] = res[1]
    resdict["addressee"] = res[2].decode('UTF-8')
    resdict["ordercapt"] = res[3].decode('UTF-8')
    resdict["startdate"] = datetime.datetime.strftime(res[4],"%Y-%m-%d")
    resdict["enddate"] = datetime.datetime.strftime(res[5],"%Y-%m-%d")
    resdict["ordertext"] = res[6].decode('UTF-8')
    resdict["username"] = res[7].decode('UTF-8')
    resdict["filename"] = res[8].decode('UTF-8') if res[8] != None else ""
    resdict["ordertime"] = datetime.datetime.strftime(res[9],"%Y-%m-%d %H:%M")
    resdict["state"] = res[10]
    resdict["reference"] = res[11].decode('UTF-8')

    #
    return resdict
#