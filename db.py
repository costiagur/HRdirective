import mysql.connector

class MYSQLDB:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="10.76.76.77",
        user="kostya_hrorder",
        password="yJSVm)W[si*yDXO8",
        database="kostya_hrorder")

        self.curs = self.mydb.cursor()
    #

    def username_select(self,username):
        querystr = 'SELECT `orderertype`, `name` FROM `users` WHERE `username` = %s'
        self.curs.execute(querystr,(username,))

        return self.curs.fetchall()
    #

    def usernameback_select(self,name):
        querystr = 'SELECT `username` FROM `users` WHERE `name` = %s'
        self.curs.execute(querystr,(name,))

        return self.curs.fetchall()
    #

    def ordercaps_select(self):
        querystr = 'SELECT `ordercapt` FROM `ordertype` WHERE 1'
        self.curs.execute(querystr)
        
        return self.curs.fetchall()
    #

    def temp_insert(self, ordercap, addressee, empid, startdate, enddate, ordtxt, reftxt, username, reffile_bin=None,reffile_name=None,listfile_bin=None,listfile_name=None):
        
        if listfile_name is None:
            listnum = 0
        else:
            querystr = 'SELECT MAX(`listnum`) FROM `ordertab` WHERE 1'
            self.curs.execute(querystr)
            listnum = self.curs.fetchone()[0]+1
        #

        querystr = 'INSERT INTO `ordertab`(`empid`, `addressee`, `ordercapt`, `startdate`, `enddate`, `ordertext`, `reference`, `username`, `orderfile`,`filename`, `listfile`, `listfilename`, `listnum`,`state`) VALUES ' \
        "(%(empid)s,%(addressee)s,%(ordercapt)s,%(startdate)s,%(enddate)s,%(ordertext)s,%(reference)s,%(username)s,%(orderfile)s,%(filename)s,%(listfile)s, %(listfilename)s, %(listnum)s, %(state)s)"

        queryvals = {
            "empid":empid,
            "addressee":addressee,
            "ordercapt":ordercap,
            "startdate":startdate,
            "enddate":enddate,
            "ordertext":ordtxt,
            "reference":reftxt,
            "username":username,
            "orderfile":reffile_bin,
            "filename":reffile_name,
            "listfile":listfile_bin,
            "listfilename":listfile_name,
            "listnum":listnum,
            "state":0
        }
        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.lastrowid
    #

    def auth_listitem_insert(self, empid, addressee, ordercap, startdate, enddate, ordtxt, reftxt, username,listnum):

        querystr = 'INSERT INTO `ordertab`(`empid`, `addressee`, `ordercapt`, `startdate`, `enddate`, `ordertext`, `reference`, `username`, `listnum`,`state`) VALUES ' \
        "(%(empid)s,%(addressee)s,%(ordercapt)s,%(startdate)s,%(enddate)s,%(ordertext)s,%(reference)s,%(username)s, %(listnum)s, %(state)s)"

        queryvals = {
            "empid":empid,
            "addressee":addressee,
            "ordercapt":ordercap,
            "startdate":startdate,
            "enddate":enddate,
            "ordertext":ordtxt,
            "reference":reftxt,
            "username":username,
            "listnum":listnum,
            "state":1
        }
        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.lastrowid
    #

    def temp_update(self,runind,empid,addressee,ordercap,startdate,enddate,ordtxt,reftxt,username,reffile_bin=None,reffile_name=None,listfile_bin=None,listfile_name=None):
        querystr = 'UPDATE `ordertab` SET `addressee`= %(addressee)s,`ordercapt`= %(ordercapt)s,' \
        '`startdate`= %(startdate)s,`enddate`= %(enddate)s,`ordertext`= %(ordertext)s,`reference`= %(reference)s,`username`= %(username)s, `state`= %(state)s'

        if reffile_name != "" and reffile_name is not None:
            querystr = querystr + ',`orderfile`= %(orderfile)s,`filename`= %(filename)s'
        #

        if listfile_name != "" and listfile_name is not None:
            querystr = querystr + ',`listfile`= %(listfile)s,`listfilename`= %(listfilename)s'
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
            "orderfile":reffile_bin,
            "filename":reffile_name,
            "listfile":listfile_bin,
            "listfilename":listfile_name,
            "state":0
        }

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.rowcount    
    #

    def auth_submit(self,runind,empid,addressee,ordercap,startdate,enddate,ordtxt,reftxt,username,reffile_bin=None,reffile_name=None,listfile_bin=None,listfile_name=None):
        if runind == "":
            querystr = 'INSERT INTO `ordertab`(`empid`, `addressee`, `ordercapt`, `startdate`, `enddate`, `ordertext`, `reference`, `username`,`state`) VALUES ' \
                "(%(empid)s,%(addressee)s,%(ordercapt)s,%(startdate)s,%(enddate)s,%(ordertext)s,%(reference)s,%(username)s, %(state)s)"
        else:      
            querystr = 'UPDATE `ordertab` SET `addressee`= %(addressee)s,`ordercapt`= %(ordercapt)s,' \
                '`startdate`= %(startdate)s,`enddate`= %(enddate)s,`ordertext`= %(ordertext)s,`reference`= %(reference)s,`state`= %(state)s'
            #username here should stay the one of the initial orderer
            
            if reffile_name != "" and reffile_name is not None:
                querystr = querystr + ',`orderfile`= %(orderfile)s,`filename`= %(filename)s'
            #

            if listfile_name != "" and listfile_name is not None:
                querystr = querystr + ',`listfile`= %(listfile)s,`listfilename`= %(listfilename)s'
            #
        
            querystr = querystr + ' WHERE `runind`= %(runind)s'
        #
            
        queryvals = {
            "runind":runind,
            "empid":empid,
            "addressee":addressee,
            "ordercapt":ordercap,
            "startdate":startdate,
            "enddate":enddate,
            "ordertext":ordtxt,
            "reference":reftxt,
            "username":username,
            "orderfile":reffile_bin,
            "filename":reffile_name,
            "listfile":listfile_bin,
            "listfilename":listfile_name,
            "state":1
        }

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        if runind == "":
            res = self.curs.lastrowid
        else:
            if self.curs.rowcount > 0:
                res = runind
            else:
                res = 0
            #
        #
        return res    
    #


    def select_runind(self,runind):
        querystr = 'SELECT * FROM `ordertab` WHERE `runind` = %(runind)s'
        queryvals = {"runind":runind}
        
        self.curs.execute(querystr,queryvals)  

        return self.curs.fetchall()
    #

    def select_file_runind(self,runind,filetype):
        if filetype == "reffile":
            querystr = 'SELECT `filename`, `orderfile` FROM `ordertab` WHERE `runind` = %(runind)s'
        elif filetype == "listfile":
            querystr = 'SELECT `listfilename`, `listfile` FROM `ordertab` WHERE `runind` = %(runind)s'
        #
            
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)  

        return self.curs.fetchall()
    #

    def select_empid(self,empid,ordererormanager):

        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`username`,`filename`, `listfilename`,`state`,`listnum`,`ordertime` FROM `ordertab` WHERE `empid`= %(empid)s'  
        
        if ordererormanager == "orderer":
            querystr = querystr + ' ORDER BY `state` ASC, `ordertime` DESC'
        elif ordererormanager == "manager":
            querystr = querystr + ' AND `state`>-1 ORDER BY `state` ASC, `ordertime` DESC' #select non declined orders
        elif ordererormanager == "searcher":
            querystr = querystr + ' AND `state`> 0 ORDER BY `state` ASC, `ordertime` DESC' #select non declined orders
        #
        
        queryvals = {"empid":empid}
        self.curs.execute(querystr,queryvals)
        
        return self.curs.fetchall()
    #

    def auth_select_awaiting (self): #select non declined orders

        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`username`,`filename`,`listfilename`,`state`,`listnum`,`ordertime`'  
        querystr = querystr + ' FROM `ordertab` WHERE `state`=0 ORDER BY `ordertime` DESC, `empid` ASC'
        
        self.curs.execute(querystr,)
        
        return self.curs.fetchall()
    #

    def load_runind(self,runind):

        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`reference`,`username`,`filename`,`listfilename`,`state`,`listnum`,`ordertime`'  
        querystr = querystr + ' FROM `ordertab` WHERE `runind`= %(runind)s'
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)
        
        return self.curs.fetchall()
    #
    
    def temp_delete(self,runind):

        querystr = 'SELECT `state` FROM `ordertab` WHERE `runind`= %(runind)s'
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)

        rownum = self.curs.fetchone()

        if rownum[0] <= 0:
            querystr = 'DELETE FROM `ordertab` WHERE `runind`= %(runind)s'
            self.curs.execute(querystr,queryvals)
            res = self.curs.rowcount
        else:
            res = 0
        #
            
        return res
    #

    def auth_decline(self,runind):

        querystr = 'SELECT `state` FROM `ordertab` WHERE `runind`= %(runind)s'
        queryvals = {"runind":runind}
        self.curs.execute(querystr,queryvals)

        existstate = self.curs.fetchone()

        runres = 0

        if existstate[0] == 0:
            querystr = 'UPDATE `ordertab` SET `state`= -1 WHERE `runind`= %(runind)s'
            queryvals = {"runind":runind}
            self.curs.execute(querystr,queryvals)
            self.mydb.commit()
            runres = self.curs.rowcount

        elif existstate[0] == -1:
            runres = 1 #means that manager wants to send again the decline mail
        #

        if runres > 0:
            querystr = 'SELECT `runind`, `empid`, `username` FROM `ordertab` WHERE `runind`= %(runind)s'
            queryvals = {"runind":runind}          
            self.curs.execute(querystr,queryvals)
            resarr = self.curs.fetchone()
            res = resarr
        else:
            res = (0)
        #
        return res
    #

    def addressee_mail(self,addressee):
        querystr = 'SELECT `email` FROM `addressees` WHERE `addressee`= %s'
        self.curs.execute(querystr,(addressee,))

        return self.curs.fetchone()
    #

    def search(self, empid="", ordercapt="", startdate='', enddate='', ordertext="", regexp=False, state="", listnum=""):
        
        querystr = 'SELECT `runind`,`empid`,`addressee`,`ordercapt`,`startdate`,`enddate`,`ordertext`,`username`,`filename`,`listfilename`,`state`,`listnum`,`ordertime` FROM `ordertab` WHERE 1' 

        queryvals= dict()
       

        if len(empid) == 0:
            pass
        else:
            querystr = querystr + " AND `empid` IN {}".format(empid)
        #

        print(querystr)

        if ordercapt == "":
            pass
        else:
            querystr = querystr + " AND `ordercapt` LIKE %(ordercapt)s"
            queryvals["ordercapt"] = '%{}%'.format(ordercapt)
        #

        if startdate == "":
            pass
        else:
            querystr = querystr + " AND `startdate` >= %(startdate)s"
            queryvals["startdate"] = startdate
        #            

        if enddate == "":
            pass
        else:
            querystr = querystr + " AND `enddate` <= %(enddate)s"
            queryvals["enddate"] = enddate
        #

        if ordertext == "":
            pass
        else:
            if regexp == 'true':
                querystr = querystr + " AND REGEXP_INSTR(`ordertext`, %(ordertext)s) > 0"
                queryvals["ordertext"] = ordertext
            else:
                querystr = querystr + " AND `ordertext` LIKE %(ordertext)s"
                queryvals["ordertext"] = '%{}%'.format(ordertext)
            #
            
        #    

        if state == "":
            pass
        else:
            querystr = querystr + " AND `state` IN (%(state)s)"
            queryvals["state"] = state
        #

        if listnum == "":
            pass
        else:
            querystr = querystr + " AND `listnum` IN (%(listnum)s)"
            queryvals["listnum"] = listnum
        #

        self.curs.execute(querystr,queryvals)
        
        return self.curs.fetchall()
    #
