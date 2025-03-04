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
from selectempid import selectempid
from getfilerunind import getfilerunind
from loadbyrunind import loadbyrunind
from tempupdate import tempupdate
from deleterunind import deleterunind
from authsubmit import authsubmit
from authdecline import authdecline
from search import search
from printpdf import printpdf
from checkempids import checkempids

CODESTR = "hrorder"
DF = ""

def myfunc(queryobj):
    #try:
        postdict = queryobj._POST()
        filesdict = queryobj._FILES()
        
        print("POST = " + str(postdict) + "\n")
        print("FILES = " + str(filesdict) + "\n")

 
        replymsg = json.dumps(["Error","Failed to run specific func"]).encode('UTF-8')

        orderertype, empname  = username()[0]
        print(orderertype)

        if postdict["request"] == "orderertype":
            if orderertype == 0:
                 common.errormsg(title="שגיאה",message="משתמש לא נמצא")
            else:
                if isinstance(orderertype,str):
                    replymsg = json.dumps(["Reply",{"orderertype":orderertype,"username":empname}]).encode('UTF-8')
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
                res = searchidname(postdict["this_id"],postdict["this_value"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        #
        
        elif postdict["request"] == "submit":

            abscentids = None

            if "reffile_in" not in filesdict:
                reffile_bin = None
                reffile_name = None
            else:
                reffile_bin = filesdict["reffile_in"][1]
                reffile_name = filesdict["reffile_in"][0]
            #
                
            if "listfile_in" not in filesdict:
                listfile_bin = None
                listfile_name = None
            else:
                listfile_bin = filesdict["listfile_in"][1]
                listfile_name = filesdict["listfile_in"][0]
                abscentids = checkempids(listfile_bin)

                if len(abscentids) != 0:
                    replymsg =  json.dumps(["Error","מספרי עובד אלה אינם קיימים {}".format(",".join(abscentids))]).encode('UTF-8')
                #
            #
            if orderertype == b'orderer' or orderertype == 'orderer':
                if abscentids is None or len(abscentids) == 0:
                    res = tempinsert(postdict["type_in"],postdict["addressee_in"],postdict["empid_in"],postdict["startdate_in"],postdict["enddate_in"], \
                                postdict["text_in"], postdict["reference_in"], empname, reffile_bin, reffile_name,listfile_bin,listfile_name)
                    replymsg = json.dumps(["Reply",res]).encode('UTF-8')
                #                 
            #
            elif orderertype == b'manager' or orderertype == 'manager': 
                if abscentids is None or len(abscentids) == 0:
                    res = authsubmit(postdict["runind_in"],postdict["type_in"],postdict["addressee_in"],postdict["empid_in"],postdict["startdate_in"],postdict["enddate_in"], \
                                postdict["text_in"], postdict["reference_in"], empname, reffile_bin, reffile_name,listfile_bin,listfile_name)
                    replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
                #
            #
        #

        elif postdict["request"] == "update":
            if orderertype == b'orderer' or orderertype == 'orderer': #manager cannot update, only submit or decline 
                abscentids = None

                if "reffile_in" not in filesdict:
                    reffile_bin = None
                    reffile_name = None
                else:
                    reffile_bin = filesdict["reffile_in"][1]
                    reffile_name = filesdict["reffile_in"][0]
                #
                
                if "listfile_in" not in filesdict:
                    listfile_bin = None
                    listfile_name = None
                else:
                    listfile_bin = filesdict["listfile_in"][1]
                    listfile_name = filesdict["listfile_in"][0]
                    abscentids = checkempids(listfile_bin)

                    if len(abscentids) != 0:
                        replymsg =  json.dumps(["Error","מספרי עובד אלה אינם קיימים {}".format(",".join(abscentids))]).encode('UTF-8')
                    #
                #

                res = tempupdate(postdict["runind_in"],postdict["type_in"],postdict["addressee_in"],postdict["empid_in"],postdict["startdate_in"],postdict["enddate_in"], \
                                postdict["text_in"], postdict["reference_in"], empname, reffile_bin, reffile_name,listfile_bin,listfile_name)
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        # 
                        
        elif postdict["request"] == "selectempid":
            if orderertype != 0:
                res = selectempid(postdict["empid"],orderertype)
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')                 
            #
        #
        elif postdict["request"] == "getfilerunind":
            if orderertype != 0:
                res = getfilerunind(postdict["runind"],postdict["filetype"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        elif postdict["request"] == "loadbyrunind":
            if orderertype != 0:
                res = loadbyrunind(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        
        elif postdict["request"] == "cancel":
            if orderertype == b'orderer' or orderertype == 'orderer': 
                res = deleterunind(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #

        elif postdict["request"] == "decline":
            if orderertype == b'manager' or orderertype == 'manager': 
                #send message to orderer that was declined. update -1
                res = authdecline(postdict["runind"],postdict["managername"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        
        elif postdict["request"] == "search":
            if orderertype != 0:
                res = search(postdict["empid"],postdict["empname"],postdict["startdate"],postdict["enddate"],postdict["ordercap"],postdict["ordtxt"],postdict["regexp"],postdict["state"],postdict["listnum"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
            #
        #
        elif postdict["request"] == "printpdf":
            if orderertype != 0:
                res = printpdf(postdict["runind"])
                replymsg = json.dumps(["Reply",res]).encode('UTF-8')
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
    #    replymsg = json.dumps(["Error",__name__ +":"+ str(e)]).encode('UTF-8')
    #    return replymsg
    #
#