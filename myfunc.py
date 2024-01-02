import base64
import json
import common
import pandas as pd
import numpy as np
import os
from username import username
from searchidname import searchidname
from ordercaps import ordercaps
from tempinsert import tempinsert
from tempselectall import tempselectall
from tempselectfilerunind import tempselectfilerunind
from temploadrunind import temploadrunind
from tempupdate import tempupdate
from tempdeleterunind import tempdeleterunind

CODESTR = "hrorder"
DF = ""

def myfunc(queryobj):
    #try:
        postdict = queryobj._POST()
        filesdict = queryobj._FILES()
        
        print("POST = " + str(postdict) + "\n")
        print("FILES = " + str(filesdict) + "\n")

        modified = {}
        thedir = '.\\emplist'
        for eachfile in os.listdir(thedir):
            modified[os.path.getmtime(thedir + "\\" + eachfile)] = eachfile
        #
        tabfile =  thedir + "\\" + modified[max(modified.keys())]

        DF = pd.read_csv(tabfile,sep="\t",encoding="cp1255",na_filter=True,skip_blank_lines=True,parse_dates=['תוקף עד','תוקף מ'],dayfirst=True,usecols=list(range(0,7,1)))
        DF.rename(columns={"מספר זהות ":"empid","שם עובד":"empname","מ.נ":"mn","מספר יחידה ":"deptnum","שם מספר יחידה ":"deptname"},inplace=True)
        DF["empidstr"] = DF["empid"].astype("string")
        print(DF)
        replymsg = json.dumps(["Error","Failed to run specific func"]).encode('UTF-8')

        orderertype, empname  = username()[0]
        print(orderertype)

        if postdict["request"] == "orderertype":
            if orderertype == 0:
                 common.errormsg(title="שגיאה",message="משתמש לא נמצא")
            else:
                replymsg = json.dumps(["Reply",{"orderertype":orderertype.decode('UTF-8'),"username":empname.decode('UTF-8')}]).encode('UTF-8')
            #
        #
        elif postdict["request"] == "loadtypes":
            if orderertype != 0:
                res = ordercaps()
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #             
        #
                
        elif postdict["request"] == "searchidname":
            if orderertype != 0:
                res = searchidname(DF,postdict["this_id"],postdict["this_value"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        #
        
        elif postdict["request"] == "submit":
            if orderertype == b'orderer':
                res = tempinsert(postdict["type_in"],postdict["addressee_in"],postdict["empid_in"],postdict["startdate_in"],postdict["enddate_in"], \
                                postdict["text_in"], postdict["reference_in"], empname,filesdict["reffiles_in"][1] if bool(filesdict) else b'',filesdict["reffiles_in"][0] if bool(filesdict) else "")
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        #

        elif postdict["request"] == "update":
            if orderertype == b'orderer':
                res = tempupdate(postdict["runind_in"],postdict["type_in"],postdict["addressee_in"],postdict["empid_in"],postdict["startdate_in"],postdict["enddate_in"], \
                                postdict["text_in"], postdict["reference_in"], empname,filesdict["reffiles_in"][1] if bool(filesdict) else b'',filesdict["reffiles_in"][0] if bool(filesdict) else "")
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        # 
                        
        elif postdict["request"] == "tempselectbyempid":
            if orderertype == b'orderer':
                res = tempselectall(postdict["empid"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        #
        elif postdict["request"] == "tempselectfilerunind":
            if orderertype != 0:
                res = tempselectfilerunind(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        elif postdict["request"] == "temploadrunind":
            if orderertype == b'orderer' or orderertype == b'manager':
                res = temploadrunind(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        
        elif postdict["request"] == "cancel":
            if orderertype == b'orderer': 
                res = tempdeleterunind(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
            elif orderertype == b'manager':
                pass
            #
        #
            
        # reply message should be encoded to be sent back to browser ----------------------------------------------
        # encoding to base64 is used to send ansi hebrew data. it is decoded to become string and put into json.
        # json is encoded to be sent to browser.

        #if bool(filesdict):
        #    file64enc = base64.b64encode(filesdict['doc1'][1])
        #    file64dec = file64enc.decode()
        
        #    replymsg = json.dumps([filesdict['doc1'][0],file64dec]).encode('UTF-8')
        #
        #else: #if filesdict is empty
        #    replymsg = json.dumps(["Error","No file provided"]).encode('UTF-8')
        #
        
        return replymsg
    #
    
    #except Exception as e:
    #    common.errormsg(title=__name__,message=e)
    #    replymsg = json.dumps(["Error","myfunc -" + str(e)]).encode('UTF-8')
    #    return replymsg
    #
#