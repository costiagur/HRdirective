import db
import win32com.client

def authdecline(runind,managername):
    mydb = db.MYSQLDB()

    resdata = mydb.auth_decline(runind)

    if resdata[0] > 0:
        username = resdata[2] if isinstance(resdata[2],str) else resdata[2].decode('UTF-8')
        
        outlook = win32com.client.Dispatch('outlook.application')
        mail = outlook.CreateItem(0)

        mail.To = username
        mail.Subject = 'הוראה {} נדחתה'.format(runind)
        
        mailbody = \
            '<div dir="rtl">' \
            '<p>שלום, {}</p>' \
            '<p>הוראה {} עבור עובד מספר {} נדחתה מסיבות הבאות:</p>' \
            '<br><br>' \
            '<p>בברכה<br>{}</p></div>'.format(username,resdata[0],resdata[1],managername)
        

        mail.HTMLBody = mailbody
        mail.Display()
    #

    return "הוראה מספר {} נדחתה".format(resdata[0])
#