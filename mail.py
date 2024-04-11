import smtplib
from email.message import EmailMessage

def mymail (toaddress, fromaddress, subjecttext, bodytext):
    msg = EmailMessage()
    msg['Subject'] = subjecttext
    msg['From'] = fromaddress
    msg['To'] = toaddress
    msg.set_content (bodytext)
    with smtplib.SMTP('XXX.XXX.XXX.il') as s:
        s.send_message(msg)
    #
#
