import db
import datetime

def loadbyrunind(runind):
    mydb = db.MYSQLDB()

    res = mydb.load_runind(runind)[0]
    resdict = dict()

    resdict["runind"] = res[0]
    resdict["empid"] = res[1]
    resdict["addressee"] = res[2] if isinstance(res[2],str) else res[2].decode('UTF-8')
    resdict["ordercapt"] = res[3] if isinstance(res[3],str) else res[3].decode('UTF-8')
    resdict["startdate"] = datetime.datetime.strftime(res[4],"%Y-%m-%d")
    resdict["enddate"] = datetime.datetime.strftime(res[5],"%Y-%m-%d")
    resdict["ordertext"] = res[6] if isinstance(res[6],str) else res[6].decode('UTF-8')
    resdict["reference"] = res[7] if isinstance(res[7],str) else res[7].decode('UTF-8') if res[7] != None else ""
    resdict["username"] = res[8] if isinstance(res[8],str) else res[8].decode('UTF-8') if res[8] != None else ""
    
    if res[9] != None:
        resdict["filename"] = res[9] if isinstance(res[9],str) else res[9].decode('UTF-8')    
    else:
        resdict["filename"] = ""
    #

    if  res[10] != None:
        resdict["listfilename"] = res[10] if isinstance(res[10],str) else res[10].decode('UTF-8')
    else:
        resdict["listfilename"] = ""
    #
        
    resdict["state"] = res[11]
    resdict["listnum"] = res[12]
    resdict["ordertime"] = datetime.datetime.strftime(res[13],"%Y-%m-%d %H:%M")
    #
    return resdict
#