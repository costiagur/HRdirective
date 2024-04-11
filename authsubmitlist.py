import db
import pandas as pd
import numpy as np

def authsubmitlist(runind):

    mydb = db.MYSQLDB()
    objlist = mydb.select_runind(runind)[0]

    listDF = pd.read_excel(objlist[11])

    addressee = objlist[2]
    ordercapt = objlist[3]
    startdate = objlist[4]
    enddate = objlist[5]
    reference = objlist[7]
    username = objlist[8]
    listnum = objlist[13]

    rowcounter = 0

    for eachrow in range(0,listDF.shape[0]):
        rowdata = listDF.iloc[[eachrow]]
        empid = rowdata.iloc[0,0].item()
        ordertxt = objlist[6].decode()
        
        for i in range(1,listDF.shape[1],1):
            ordertxt = ordertxt.replace("##" + rowdata.columns[i] + "##",str(rowdata.iloc[0,i]))
        #

        rowcounter = rowcounter + mydb.auth_listitem_insert(empid,addressee,ordercapt,startdate,enddate,ordertxt,reference,username,listnum)
    #
    
    return rowcounter
#