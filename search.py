import db
import datetime
import os
import pandas as pd
import re

def search(empid,empname,startdate,enddate,ordercap,ordtxt,regexp,state,listnum):
    mydb = db.MYSQLDB()

    pattern = re.compile(r'^0+$')
    empidreshima = pattern.match(empid)

    modified = {}
    thedir = '.\\emplist'
        
    for eachfile in os.listdir(thedir):
        modified[os.path.getmtime(thedir + "\\" + eachfile)] = eachfile #check when each employees file was modified
    #
        
    tabfile =  thedir + "\\" + modified[max(modified.keys())] #take the latest file (the most up to date)

    DF = pd.read_csv(tabfile,sep="\t",encoding="cp1255",na_filter=True,skip_blank_lines=True,parse_dates=['תוקף עד','תוקף מ'],dayfirst=True,usecols=list(range(0,7,1)))
    DF.rename(columns={"מספר זהות ":"empid","שם עובד":"empname","מ.נ":"mn"},inplace=True)

    if empidreshima or empname == "רשימה":
        empid = "000000000"
        empid = tuple([empid,empid])
    
    elif empid == "" and empname != "":
        empid = DF.loc[DF["empname"].str.contains('.*{}.*'.format(empname),regex=True),"empid"].unique().tolist()
        empid = tuple(empid)
    #
    elif empid == "" and empname == "":
        empid = ""
    #
    else:
        empid = tuple([empid,empid])       
    #
    
    res = mydb.search(empid,ordercap,startdate,enddate,ordtxt,regexp,state,listnum)

    reslist = []

    for eachrow in res:
        resdict = dict()
        print(eachrow)
        if eachrow[1] == 0:
            resdict["empname"] = "רשימה"
        else:
            empname = DF.loc[DF["empid"] == eachrow[1],"empname"]
            if empname.empty:
                resdict["empname"] = "שם לא נמצא"
            else:
                resdict["empname"] = empname.unique().item()
            #
        #
            
        resdict["runind"] = eachrow[0]
        resdict["empid"] = eachrow[1]
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
