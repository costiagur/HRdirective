import db
import os
import re
from pdforder import pdforder
from datetime import datetime
from searchidname import searchidname
from mail_final import mail_final
from authsubmitlist import authsubmitlist

def authsubmit(runind,ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile_bin=None,reffile_name=None,listfile_bin=None,listfile_name=None):
   
    mydb = db.MYSQLDB()
    
    inserted = mydb.auth_submit(runind,empid, addressee, ordercap, startdate, enddate, ordtxt, reftxt, username, reffile_bin,reffile_name,listfile_bin,listfile_name)
   
    if int(inserted) > 0:
        res = mydb.select_runind(inserted)[0]

        startdate = datetime.strftime(res[4],"%d/%m/%Y")
        enddate = datetime.strftime(res[5],"%d/%m/%Y")
        ordertime = datetime.strftime(res[15],"%d/%m/%Y %H:%M")
    
        pattern = re.compile(r'^0+$')
        empidreshima = pattern.match(empid)

        if empidreshima:
            empname = "רשימה"
        else:    
            empdict = searchidname("empid_in",empid)
            
            if empdict == "":
                empname = ""
            else:
                empname = empdict[0]["empname"]
            #
        #

        filename = ""
        listfilename = ""
        curdir = os.path.dirname(os.path.realpath(__file__))

        if res[10] != None and res[10] != "":
            with open(curdir + "\\orderpdfs\\" + res[10] if isinstance(res[10],str) else res[10].decode('UTF-8'),"wb") as w:
                w.write(res[9])
                filename = w.name
                print(filename)
            #
        else:
            filename = ""
        #

        if res[12] != None and res[12] != "":
            with open(curdir + "\\orderpdfs\\" + res[12].decode('UTF-8'),"wb") as w:
                w.write(res[11])
                listfilename = w.name
            #
            authsubmitlist(runind)
        else:
           listfilename = ""
        # 
          
        pdffilepath = pdforder(res[0],empid,empname, res[2] if isinstance(res[2],str) else res[2].decode('UTF-8'), \
                               res[3] if isinstance(res[3],str) else res[3].decode('UTF-8'), startdate, enddate, res[6] if isinstance(res[6],str) else res[6].decode('UTF-8'),  \
                               res[7] if isinstance(res[7],str) else res[7].decode('UTF-8') if res[7] != None else "", res[8] if isinstance(res[8],str) else res[8].decode('UTF-8'), \
                               res[10].decode('UTF-8') if filename != "" else "",res[12].decode('UTF-8') if listfilename != "" else "",ordertime)
    
        if pdffilepath != 0:
            maildone = mail_final(runind,empid,addressee,res[8] if isinstance(res[8],str) else res[8].decode('UTF-8'),pdffilepath,filename,listfilename)
        #
        if maildone:
            os.unlink(pdffilepath)
            if filename != "":
                os.unlink(filename)
            #
            if listfilename != "":
                os.unlink(listfilename)
            #
        #
        
    return inserted 
#