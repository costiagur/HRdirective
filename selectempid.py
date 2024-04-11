import db
import datetime
from searchidname import searchidname
import re

def selectempid(empid,orderertype):
    mydb = db.MYSQLDB()
    
    orderertype = orderertype if isinstance(orderertype,str) else orderertype.decode()

    res = mydb.select_empid(empid,orderertype)

    reslist = []

    pattern = re.compile('^0+$')


    for eachrow in res:
        resdict = dict()

        resdict["runind"] = eachrow[0]
        resdict["empid"] = eachrow[1]
               
        if pattern.match(empid):
            empname = "רשימה"
        else:
            empres = searchidname("empid_in",eachrow[1])
            if empres == "":
                empname = "עובד לא נמצא"
            else:    
                empname = empres[0]["empname"]
            #
        #
        
        resdict["empname"] = empname
        resdict["addressee"] = eachrow[2] if isinstance(eachrow[2],str) else eachrow[2].decode('UTF-8')
        resdict["ordercapt"] = eachrow[3] if isinstance(eachrow[3],str) else eachrow[3].decode('UTF-8')
        resdict["startdate"] = datetime.datetime.strftime(eachrow[4],"%d/%m/%Y")
        resdict["enddate"] = datetime.datetime.strftime(eachrow[5],"%d/%m/%Y")
        resdict["ordertext"] = eachrow[6] if isinstance(eachrow[6],str) else eachrow[6].decode('UTF-8')
        resdict["username"] = eachrow[7] if isinstance(eachrow[7],str) else eachrow[7].decode('UTF-8')
        if eachrow[8] != None:
            resdict["filename"] = eachrow[8] if isinstance(eachrow[8],str) else eachrow[8].decode('UTF-8')
        else:
            resdict["filename"] = ""
        #
        if eachrow[9] != None:
            resdict["listfilename"] = eachrow[9] if isinstance(eachrow[9],str) else eachrow[9].decode('UTF-8')
        else:
            resdict["listfilename"] = ""
        #
        resdict["state"] = eachrow[10]
        resdict["listnum"] = eachrow[11]
        resdict["ordertime"] = datetime.datetime.strftime(eachrow[12],"%d/%m/%Y %H:%M")

        reslist.append(resdict)

    #
    return reslist
#