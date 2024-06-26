import win32com.client
import db
from searchidname import searchidname

def mail_final(runind, empid,addressee,username,orderfilepath,reffilepath,listfilepath):

    mydb = db.MYSQLDB()

    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    if addressee == "שכר":
        maamaddict = searchidname("maamad",empid)
        
        if maamaddict == "":
            maamad = ""
        else:
            maamad = maamaddict[0]["maamad"]
        #

        if maamad in ("","",""):
            whom = mydb.addressee_mail("שכר_אחר")[0]
        else:
            whom = mydb.addressee_mail("שכר_קבוע")[0]
        #
        whom = whom if isinstance(whom, str) else whom.decode('UTF-8')
        mail.CC = username

    elif addressee == "משאבי אנוש":
        whom = username
    #
    
    mail.To = whom
    mail.Subject = 'הוראה {} לביצוע'.format(runind)
    
    mailbody = \
        '<div dir="rtl">' \
        '<p>שלום רב</p>' \
        '<p>נוצרה הוראה {} עבור עובד מספר {}</p>' \
        '<p>בברכה<br>{}</p></div>'.format(runind,empid,username)
    

    mail.HTMLBody = mailbody

    mail.Attachments.Add(orderfilepath)
    
    if reffilepath != "":
        mail.Attachments.Add(reffilepath)
    
    if listfilepath != "":
        mail.Attachments.Add(listfilepath)

    mail.Display()
    #mail.Send()

    return True
#
