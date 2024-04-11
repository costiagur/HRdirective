import pandas as pd
import numpy as np
import os

def searchidname(this_id, this_value):

    modified = {}
    thedir = '.\\emplist'
    
    for eachfile in os.listdir(thedir):
        modified[os.path.getmtime(thedir + "\\" + eachfile)] = eachfile #check when each employees file was modified
    #
    
    tabfile =  thedir + "\\" + modified[max(modified.keys())] #take the latest file (the most up to date)

    DF = pd.read_csv(tabfile,sep="\t",encoding="cp1255",na_filter=True,skip_blank_lines=True,parse_dates=['תוקף עד','תוקף מ'],dayfirst=True,usecols=list(range(0,7,1)))
    DF.rename(columns={"מספר זהות ":"empid","שם עובד":"empname","מ.נ":"mn","מעמד":"maamad"},inplace=True)
    DF["empidstr"] = DF["empid"].astype("string")

    if this_id == "empid_in":
        res = DF.loc[DF["empidstr"].str.contains('^{}'.format(this_value),regex=True),["empid","empname"]]
    
    elif  this_id == "empname_in":
        res = DF.loc[DF["empname"].str.contains('{}'.format(this_value),regex=True),["empid","empname"]]
    #
    elif this_id == "maamad":
        res = DF.loc[DF["empidstr"].str.contains('{}'.format(this_value),regex=True),["maamad"]]
    
    if res.empty:
        return ""
    else:
        return res.to_dict('records')
    #
#