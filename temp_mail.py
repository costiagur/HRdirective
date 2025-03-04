import win32com.client
import db
from searchidname import searchidname

def temp_mail(runind,empid,username):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mydb = db.MYSQLDB()
    managers = mydb.managers_select()
    managerlist = [eachtuple[0] for eachtuple in managers]

    empdict = searchidname("empid_in",empid)
            
    if empdict == "":
        empname = ""
    else:
        empname = empdict[0]["empname"]
    #

    mail.To = ";".join(managerlist)
    mail.Subject = 'הוראה בעניין {} לאישורך'.format(empname)
    
    mailbody = \
        '<div dir="rtl">' \
        '<p>דנה, שלום</p>' \
        '<p>נוצרה הוראה עבור {}, {} לאישורך</p>' \
        '<p>בברכה<br>{}</p></div>'.format(empname,empid,username)
    

    mail.HTMLBody = mailbody
    #mail.Body = "This is the normal body"
    #mail.Attachments.Add('c:\\sample.xlsx')
    #mail.Attachments.Add('c:\\sample2.xlsx')
    #mail.CC = 'somebody@company.com'
    mail.Display()
    #mail.Send()
#