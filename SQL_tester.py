# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 13:07:56 2015

@author: greenbotics
"""

import MySQLdb
from dbFunctions_forkfork import *

conn = MySQLdb.connect(host="bamdm.c81zpi4sue10.us-west-1.rds.amazonaws.com", user="BAM",passwd='cooler94550',db = 'BAMDB')

#def send_to_dataBase(Table,Column,Data):
#    print "start"
#    query = "INSERT IGNORE INTO "+Table+" ("+Column+") values ("+Data+")"
#    print query
#    x = conn.cursor()
#    if x.execute(query):
#        print "heyyyyyyyyyyyyyyy"
#    #conn.commit()
#    print "stop"
    
#def send_to_dataBaseB(Data):
#    print "start"
#    #x.execute("INSERT IGNORE INTO %s %s values %s" % (Table,Column,Data))
#    #x.execute("""INSERT INTO Bens_Stocks VALUES (%s,%s)""",(Column,Data))
#    add_employee = ("INSERT INTO Bens_Stocks ""(Symbol,hey) ""VALUES (%s,%s)")
#    x = conn.cursor()
#    x.execute(add_employee,Data)
#    x.commit()
    
#data = ("TE","Buyit")
#cols = ["Symbol","BorS"]
data = "TEss"
cols = "Symbol"
#send_to_dataBaseB()
send_to_dataBase("Symbol",cols,data)
#update_Symbol("buy",1)



#def update_dataBase():
#sym = "AAPL"
#b = "yehn"
#iD = 1
#x = conn.cursor()
#if x.execute ("""
#    UPDATE Symbol
#    SET BorS = %s
#    WHERE idSymbol = %s;
#""", (b,iD)):
#    print "hi hi hi"
#conn.commit()
    
#def executeSQLpush(_connection,_sql,_values = (),_commit=True):
#try:
#_connection[1].execute(_sql,_values)
#if _commit:
#_connection[0].commit()
#return True
#except:
#print _sql
#raise
#return False



#sql = "SELECT ID FROM Users WHERE UserName='UserName[i]'"
#sql = "SELECT ID FROM Users WHERE UserName='Bullrider'"
#print sql
#cur = conn.cursor()
#cur.execute("SELECT ID FROM Users WHERE UserName='Bullrider'")
#rows = cur.fetchone()
#print rows
#print type(rows)
#print rows[0]
#fk = x.execute(sql)
#print fk


#Oct 20 trying the update how to do it in MySQLdb
#UPDATE celebs
#SET age = 22
#WHERE id = 1;
#ALTER TABLE celebs ADD COLUMN twitter_handle TEXT; 
#
#SELECT * FROM celebs;


#x.execute ("""UPDATE Symbol SET BorS=%s WHERE idSymbol = %s" """, (b,iD))

#x.execute
#UPDATE Symbol
#SET BorS = 'Buy'
#WHERE idSymbol = 1;

#SET BorS = b
#WHERE idSymbol = iD;
#SELECT * FROM celebs;

#cursor.execute ("""
#   UPDATE tblTableName
#   SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s
#   WHERE Server=%s
#""", (Year, Month, Day, Hour, Minute, ServerID))


#3cursor.execute ("UPDATE tblTableName SET Year=%s, Month=%s, Day=%s, Hour=%s, Minute=%s WHERE Server='%s' " % (Year, Month, Day, Hour, Minute, ServerID))