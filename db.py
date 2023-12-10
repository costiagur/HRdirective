import mysql.connector

class MYSQLDB:
    
    def __init__(self):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="order_user",
        password="dSjB6e5FpENhMVad",
        database="orders")
    #

    def selectaddressee(self, saldep=''):
        curs = self.mydb.cursor()
        
        if saldep == '':
            querystr = 'SELECT `saldep` FROM `addressee` WHERE 1'
            curs.execute(querystr)
        else:
            querystr = 'SELECT `salemail` FROM `addressee` WHERE `saldep` = %s'
            curs.execute(querystr,(saldep,))
        #
        
        return curs.fetchall()
    #

    def inserttemp(self, saldep,ordetype,empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile = 'b'):

        curs = self.mydb.cursor()
        curs.execute('SELECT `orderind` FROM ordetab ORDER BY `orderind` DESC')

        lasindex = curs.fetchone()
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

        curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return curs.rowcount
    #

    def updatetemp(self, orderind, saldep, ordetype, empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile = 'b'):
        querystr = 'UPDATE ordetab SET `saldep`, `ordetype`, `empid`, `empname`, `startdate`, `enddate`, `ordtxt`, `reftxt`, `orderer`, `reffile` WHERE `orderind`= '
        querystr = querystr + " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        
        queryvals = (saldep,ordetype,empid, empname, startdate, enddate, ordtxt, reftxt, orderer, reffile,str(orderind))

        curs = self.mydb.cursor()

        curs.execute(querystr,queryvals)
        self.mydb.commit()
        
        return curs.rowcount
    #

    def authorizeord(self,):
        pass
    #