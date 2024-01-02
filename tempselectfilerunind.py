import base64
import db

def tempselectfilerunind(runind):
    mydb = db.MYSQLDB()
    res = mydb.temp_select_file_runind(runind)
    
    file64enc = base64.b64encode(res[0][1])
    file64dec = file64enc.decode()

    resobj = {"filename":res[0][0].decode(),
              "orderfile":file64dec}

    return resobj
#