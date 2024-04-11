import re
import pdfkit
import os

def pdforder(runind,empid,empname, addressee, ordercap, startdate, enddate, ordtxt, reftxt, username,filename,listfilename,ordertime):

    rowdict = locals()

    recomp = re.compile('##(\w+)##')
    
    config = pdfkit.configuration(wkhtmltopdf= 'wkhtmltox\\bin\\wkhtmltopdf.exe')

    templf = open('template.html',"r",encoding="utf-8")

    totaltxt = templf.read()

    rowdict["curdir"] = os.path.dirname(os.path.realpath(__file__))  

    for eachmatch in recomp.findall(totaltxt):               
        totaltxt = totaltxt.replace("##" + eachmatch + "##",str(rowdict.get(eachmatch,"")))                     
    #
        
    pdfres = pdfkit.from_string(totaltxt,"orderpdfs\\" + str(rowdict['runind']) + ".pdf",configuration=config,options={"enable-local-file-access": ""})

    if pdfres:
        res = rowdict["curdir"] + "\\orderpdfs\\" + str(rowdict['runind']) + ".pdf"
    else:
        res = 0
    #
        
    return res
#