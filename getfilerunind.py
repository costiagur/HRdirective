import base64
import db

def getfilerunind(runind,filetype):
    mydb = db.MYSQLDB()
    res = mydb.select_file_runind(runind,filetype)
    
    file64enc = base64.b64encode(res[0][1])
    file64dec = file64enc.decode()

    resobj = {"filename":res[0][0] if isinstance(res[0][0],str) else res[0][0].decode('UTF-8'),
              "filedata":file64dec}

    return resobj
#