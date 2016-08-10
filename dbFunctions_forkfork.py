# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:53:42 2015

@author: greenbotics
"""

import MySQLdb
import requests
from bs4 import BeautifulSoup
from yahoo_finance import Share
#myfiles below
from SoupFunctions import get_htmlsoup


conn = MySQLdb.connect(host="bamdm.c81zpi4sue10.us-west-1.rds.amazonaws.com", user="BAM",passwd='cooler94550',db = 'BAMDB')


def send_to_dataBase(Table,Column,Data): # this method inserts new rows into columns on tables whether it be one columns data or many in a row
    col = ",".join(Column) # makes the List Column into a string if need be
    if type(Column) is list:
        ## making %s list##
        n = len(Column)
        m = 0
        percentS = []
        while m < n:
            percentS.append("%s")
            m+=1
        row = ",".join(percentS)
        print "send to DB",row
        #add = ("INSERT IGNORE INTO "+Table+" ("+col+") VALUES (%s,%s)")
        add = ("INSERT IGNORE INTO "+Table+" ("+col+") VALUES " +"("+row+")")
        print "send to DB", add
        data = Data
    else:
        add = ("INSERT IGNORE INTO "+Table+ "("+Column+") VALUES (%s)")
        data = Data
        print "Insert, the single addition"
    try:
        x = conn.cursor()
        x.execute(add,data) # notice how the arguments are a list of the row data and the entire query
        conn.commit()
        print "Insert Into, It Worked!"
        if LAST_INSERT_ID() ==0: #if Ture the WHole thing was ignored If false it was inserted!!!!!!!!!!
            return True
        else:
            return False
    except:
        print "Insert Into, Didn't Work"
        print(x._last_executed) #this the query that couldn't run
    #conn.close()  # does this need to be here
    print "end of send to database"
    
def update_Symbol_Uni(Table,Column,row,data): #Column is the one(s) you want changed, row is the Primary key or Unique key, data [PK_actual_value,what youre changing column to]
    if type(Column) is list:
        colc = ""
        n = len(Column)
        m = 0
        for c in Column:
            colc = colc+c+"=%s "
            if m != (n-1):
                colc = colc+", "
            m+=1
        print colc
        update = ("UPDATE "+Table+ " set "+colc+" Where "+row+" =%s")
        print update
    else:
        update = ("UPDATE "+Table+ " set " +Column+ "= %s Where "+row+" =%s")
        print update
    try:
        x = conn.cursor()
        x.execute(update,data) # notice how the arguments are a list of the row data and the entire query
        conn.commit()
        print "Update Symbol, It Worked!"
    except:
        print "Update Symbol, Didn't Work"
        print(x._last_executed) #this the query that couldn't run


def select_db(table,col,row):#(table,col,row)
    if row == '*':
        try:
            x = conn.cursor()
            x.execute("SELECT %s FROM %s" % (col, table))
            print(x._last_executed)
        except:
            print "Didn't Work"
            print(x._last_executed) #this the query that couldn't run
    else:
        try:
            x = conn.cursor()
            x.execute("SELECT %s FROM %s WHERE %s" % (col, table, row))
        except:
            print "Didn't Work"
            print(x._last_executed) #this the query that couldn't run
#    x.execute("SELECT * FROM %s;",("Bens_Stocks"))
#    x.execute("SELECT Shares FROM Bens_Stocks WHERE id=1;")
#    x.fetchall()
    fetch = x.fetchall()
    for r in fetch:
        #return r
        for a in r:
            print type(r)
            print a
    return fetch
    
    
def select_db_single(table,col,row):#(table,col,row) #THIS SHOULD USE FetchONE!!!
    x = conn.cursor()
    x.execute("SELECT %s FROM %s WHERE %s" % (col, table, row))
    fetch = x.fetchall()
    if fetch is not tuple:
        print "not tubp"
    for r in fetch:
        for a in r:
            return a
            
def select_db_topDate(col):#(table,col,row) #THIS SHOULD USE FetchONE!!!
    x = conn.cursor()
    x.execute("SELECT %s FROM BAMDB.Bens_Portfolio_Value ORDER BY DTime DESC"%(col))
    #x.execute("SELECT %s FROM %s WHERE %s" % (col, table, row))
    fetch = x.fetchone()
#    print fetch
#    print type(fetch)
    if type(fetch) is not tuple:
        print "not tubp, there was nothing in the select"
    else:
        for f in fetch:
            return f

#select_db_topDate("UnusedFunds")
#select_db_single("Bens_Portfolio_Value","UnusedFunds","id =0") 
#select_db_single("Bens_Stocks","Shares","Symbol =\'YHOO\'")
#data = [20,100,'YHOO']
#update_Symbol_Uni("Bens_Stocks",["Shares","Cash_Value"],"SYMBOL",data)
#print select_db("Bens_Stocks","Cash_Value",'*')    

#print select_db('Bens_Stocks','Shares',1)
#select_db("Bens_Stocks","Shares",1)

#x = conn.cursor()
#comp = "APPL"
#iD = x.execute("SELECT Symbol FROM Symbol WHERE idSymbol=1")
#print x.execute("SELECT ID FROM Users WHERE UserName='"+'NickG'+"'")
#print type(iD)
#print iD
#SELECT Shares FROM Bens_Stocks WHERE id=1;

#update_Symbol("fu",1)
    
    
#####  I have zero idea why this one wouldn't work!  Oct 30 
    #def send_to_dataBaseB():
#    print "start"
#    #x.execute("INSERT IGNORE INTO %s %s values %s" % (Table,Column,Data))
#    #x.execute("""INSERT INTO Bens_Stocks VALUES (%s,%s)""",(Column,Data))
#    data = ("APKH","hey")
#    add_employee = ("INSERT IGNORE INTO Symbol "
#    "(Symbol,BorS) "
#    "VALUES (%s,%s)")
#    query = "INSERT IGNORE INTO Symbol (Symbol,BorS) VALUES ('APKH','hey')"
#    print add_employee
#    try:
#        x = conn.cursor()
#        x.execute(query)
#        #x.execute(add_employee,data)
#        x.commit()
#    except:
#        print(x._last_executed)
#        raise
#    #x.close()
    
    
    
#def update_Symbol_Uni(Table,Column,row,data): #Column is the one(s) you want changed, row is the Primary key or Unique key, data [PK_actual_value,what youre changing column to]
#    x = conn.cursor()
#    update = ("UPDATE "+Table+ " set " +Column+ "= %s Where "+row+" =%s")
#    print update
#    try:
#        x = conn.cursor()
#        x.execute(update,data) # notice how the arguments are a list of the row data and the entire query
#        conn.commit()
#        print "It Worked!"
#    except:
#        print "Didn't Work"
#        print(x._last_executed) #this the query that couldn't run
    