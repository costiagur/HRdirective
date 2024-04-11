import win32com.client

def temp_mail(runind,empid,username):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = ''
    mail.Subject = 'הוראה {} לאישורך'.format(runind)
    
    mailbody = \
        '<div dir="rtl">' \
        '<p>שלום</p>' \
        '<p>נוצרה הוראה {} עבור עובד מספר {} לאישורך</p>' \
        '<p>בברכה<br>{}</p></div>'.format(runind,empid,username)
    

    mail.HTMLBody = mailbody
    #mail.Body = "This is the normal body"
    #mail.Attachments.Add('c:\\sample.xlsx')
    #mail.Attachments.Add('c:\\sample2.xlsx')
    #mail.CC = 'somebody@company.com'
    mail.Display()
    #mail.Send()
#
