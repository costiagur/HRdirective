import base64
from pdforder import pdforder
from loadbyrunind import loadbyrunind
from searchidname import searchidname
from datetime import datetime

def printpdf(runind):
    empdict= loadbyrunind(runind)

    searchdict = searchidname("empid_in",empdict["empid"])

    if searchdict == "":
        empdict["empname"] = ""    
    else:
        empdict["empname"] = searchdict[0]["empname"]
    #

    startdate = datetime.strftime(datetime.strptime(empdict["startdate"],"%Y-%m-%d"),"%d/%m/%Y")
    enddate = datetime.strftime(datetime.strptime(empdict["enddate"],"%Y-%m-%d"),"%d/%m/%Y")
    ordertime = datetime.strftime(datetime.strptime(empdict["ordertime"],"%Y-%m-%d %H:%M"),"%d/%m/%Y %H:%M")

    filepath = pdforder(empdict["runind"], empdict["empid"],empdict["empname"],empdict["addressee"],empdict["ordercapt"],startdate,enddate,empdict["ordertext"],empdict["reference"] \
                        ,empdict["username"],empdict["filename"],empdict["listfilename"],ordertime)
    
    with open(filepath,"rb") as r:
        blob = r.read()
    #
        
    file64enc = base64.b64encode(blob)
    file64dec = file64enc.decode()

    resobj = {"filename":"{}.pdf".format(runind), "orderfile":file64dec}

    return resobj    
#