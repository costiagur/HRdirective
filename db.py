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


    def selectaddressee(self, saldep=''):
        
        if saldep == '':
            querystr = 'SELECT `saldep` FROM `addressee` WHERE 1'
            self.curs.execute(querystr)
        else:
            querystr = 'SELECT `salemail` FROM `addressee` WHERE `saldep` = %s'
            self.curs.execute(querystr,(saldep,))
        #
        
        return self.curs.fetchall()
    #

    def inserttemp(self, saldep,ordetype,empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile = 'b'):

        self.curs.execute('SELECT `orderind` FROM ordetab ORDER BY `orderind` DESC')

        lasindex = self.curs.fetchone()
        orderind = int(lasindex)+1

        querystr = 'INSERT INTO ordetab (`orderind`, `saldep`, `ordetype`, `empid`, `empname`, `startdate`, `enddate`, `ordtxt`, `reftxt`, `orderer`, `reffile`, `ordauthed`, `executedate`, `executer`) VALUES'
        querystr = querystr + " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        queryvals = list()

        if type(empid) is tuple:
            pass
        else:
            empid = (empid,)
            ordtxt = (ordtxt,)
        #

        for i in range(0,len(empid),1):
            queryvals.append((str(orderind),saldep,ordetype,empid[i], empname, startdate, enddate, ordtxt[i], reftxt, orderer, reffile,'NULL','NULL','NULL'))
        #

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.rowcount
    #

    def updatetemp(self, orderind, saldep, ordetype, empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile = 'b'):
        querystr = 'UPDATE ordetab SET `saldep`, `ordetype`, `empid`, `empname`, `startdate`, `enddate`, `ordtxt`, `reftxt`, `orderer`, `reffile` WHERE `orderind`= '
        querystr = querystr + " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        queryvals = (saldep,ordetype,empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile,str(orderind))

        self.curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return self.curs.rowcount
    #

    def authorizeord(self,):
        pass
    #