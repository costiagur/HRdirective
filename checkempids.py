import pandas as pd
import numpy as np
import os

def checkempids(listfile_bin):

    listDF = pd.read_excel(listfile_bin)

    print(listDF)
    abcentids = []
    modified = {}
    thedir = '.\\emplist'
    
    for eachfile in os.listdir(thedir):
        modified[os.path.getmtime(thedir + "\\" + eachfile)] = eachfile #check when each employees file was modified
    #
    
    tabfile =  thedir + "\\" + modified[max(modified.keys())] #take the latest file (the most up to date)

    DF = pd.read_csv(tabfile,sep="\t",encoding="cp1255",na_filter=True,skip_blank_lines=True,parse_dates=['תוקף עד','תוקף מ'],dayfirst=True,usecols=list(range(0,7,1)))
    DF.rename(columns={"מספר זהות ":"empid","שם עובד":"empname","מ.נ":"mn"},inplace=True)
    DF["empidstr"] = DF["empid"].astype("string")
    
    for eachid in listDF.iloc[:,0]:
        num = DF.loc[DF["empid"] == eachid,"empid"].count()
        if num > 0:
            pass
        else:
            abcentids.append(str(eachid))
        #
    #
   
    return abcentids
#