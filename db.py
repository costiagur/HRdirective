import mysql.connector

class MYSQLDB:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="HRORDERuser",
        password="yJSVm)W[si*yDXO8",
        database="hrorder")

        self.curs = self.mydb.cursor()
    #

    def username_select(self,username):
        querystr = 'SELECT `orderertype`, `name` FROM `users` WHERE `username` = %s'
        self.curs.execute(querystr,(username,))

        return self.curs.fetchall()
    #

    def ordercaps_select(self):
        querystr = 'SELECT `ordercapt` FROM `ordertype` WHERE 1'
        self.curs.execute(querystr)
        
        return self.curs.fetchall()
    #

    def temp_insert(self, ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile = b'',filename="",state=0):
        
        querystr = 'INSERT INTO `temporder`(`empid`, `addressee`, `ordercapt`, `startdate`, `enddate`, `ordertext`, `reference`, `username`, `orderfile`,`filename`, `oneofmany`) VALUES ' \
        "(%(empid)s,%(addressee)s,%(ordercapt)s,%(startdate)s,%(enddate)s,%(ordertext)s,%(reference)s,%(username)s,%(orderfile)s,%(filename)s,%(state)s)"

        queryvals = {
            "empid":empid,
            "addressee":addressee,
            "ordercapt":ordercap,
            "startdate":startdate,
            "enddate":enddate,
            "ordertext":ordtxt,
            "reference":reftxt,
            "username":username,
            "orderfile":reffile,
            "filename":filename,
            "state":state
        }

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.lastrowid
    #

    def temp_update(self,runind,empid,addressee,ordercap,startdate,enddate,ordtxt,reftxt,username,reffile = b'',filename = '',state=0):
        querystr = 'UPDATE `temporder` SET `addressee`= %(addressee)s,`ordercapt`= %(ordercapt)s,' \
        '`startdate`= %(startdate)s,`enddate`= %(enddate)s,`ordertext`= %(ordertext)s,`reference`= %(reference)s,`username`= %(username)s, `state`= %(state)s'

        if filename != "":
            querystr = querystr + '`orderfile`= %(orderfile)s,`filename`= %(filename)s'
        #
        
        querystr = querystr + ' WHERE `runind`= %(runind)s'

        queryvals = {
            "runind":runind,
            "addressee":addressee,
            "ordercapt":ordercap,
            "startdate":startdate,
            "enddate":enddate,
            "ordertext":ordtxt,
            "reference":reftxt,
            "username":username,
            "orderfile":reffile,
            "filename":filename,
            "state":state
        }

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.rowcount    
    #

    def temp_select_runind(self,runind):
        querystr = 'SELECT * FROM `temporder` WHERE `runind` = %(runind)s'
        queryvals = {"runind":runind}
        
        self.curs.execute(querystr,queryvals)  

        return self.curs.fetchall()
    #

    def temp_select_file_runind(self,runind):
        querystr = 'SELECT `filename`, `orderfile` FROM `temporder` WHERE `runind` = %(runind)s'
        queryvals = {"runind":runind}
        
        self.curs.execute(querystr,queryvals)  

        return self.curs.fetchall()
    #

    def temp_select_all(self,empid):

        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`username`,`filename`,`ordertime`,`state`'  
        querystr = querystr + ' FROM `temporder` WHERE `empid`= %(empid)s AND `state` > -1 ORDER BY `state` ASC, `ordertime` DESC'
        queryvals = {"empid":empid}
        self.curs.execute(querystr,queryvals)
        
        return self.curs.fetchall()
    #
    def temp_load_runind(self,runind):

        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`username`,`filename`,`ordertime`,`state`, `reference`'  
        querystr = querystr + ' FROM `temporder` WHERE `runind`= %(runind)s'
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)
        
        return self.curs.fetchall()
    #
    def temp_delete(self,runind):

        querystr = 'SELECT `state` FROM `temporder` WHERE `runind`= %(runind)s'
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)

        rownum = self.curs.fetchone()

        if rownum[0] == 0:
            querystr = 'DELETE FROM `temporder` WHERE `runind`= %(runind)s'
            self.curs.execute(querystr,queryvals)
            res = self.curs.rowcount
        else:
            res = 0
        #
            
        return res
    #