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

def send_to_dataBase(Table,Column,Data):
    print "start"
    print Column
    print Data
    if type(Column) is list:
        print "Inserting multiple columns"
        column = ""
        data = ""
        n = 0
        m = 0
        # must get rid of these Column and Data for loops 
        for c in Column: # making the list a string of the elements with a "," inbetween all of them
            if n == 0:
                column = column+c
            else:
                column = c+","+column
            n +=1
        for d in Data:
            if m == 0:
                data = data+d
            else:
                data = d+","+data
            m +=1
            x = conn.cursor()
        x = conn.cursor()
        x.execute(query)
        query = "INSERT IGNORE INTO "+Table+" ("+column+") values ("+data+")"
        print query
    else:
        x = conn.cursor()
        x.execute("INSERT IGNORE INTO %s %s values %s" % (table,col,row) 
        conn.commit()
#        query = "INSERT IGNORE INTO "+Table+" ("+Column+") values ("+Data+")"
        print "the single one"
#    print query
#    x = conn.cursor()
#    x.execute(query)
#    conn.commit()
    #conn.close()
    print "end of send to database"
    
def update_Symbol(BorS,iD):
    #b = "yehn"
    #iD = 1
    x = conn.cursor()
    if x.execute ("""
        UPDATE Symbol
        SET BorS = %s
        WHERE idSymbol = %s;
        """, (BorS,iD)):
            print "hi hi hi"
            if BorS == "Buy":
                print "get some"
            else:
                print "nah brah"
    conn.commit()

def select_db(table,col,row):#(table,col,row)
    x = conn.cursor()
    #query = ("SELECT Shares FROM Bens]\_Stocks WHERE Symbol=%s")
    #print x.execute(query, (row))
    x.execute("SELECT %s FROM %s WHERE %s" % (col, table, row))
    #x.execute("SELECT * FROM %s;",("Bens_Stocks"))
#    x.execute("SELECT Shares FROM Bens_Stocks WHERE id=1;")
#    x.fetchall()
    fetch = x.fetchall()
    for r in fetch:
        print len(r)
        for a in r:
            print type(r)
            print a
    return x.fetchall()
    
def select_db_single(table,col,row):#(table,col,row)
    x = conn.cursor()
    #query = ("SELECT Shares FROM Bens]\_Stocks WHERE Symbol=%s")
    #print x.execute(query, (row))
    x.execute("SELECT %s FROM %s WHERE %s" % (col, table, row))
    #x.execute("SELECT * FROM %s;",("Bens_Stocks"))
#    x.execute("SELECT Shares FROM Bens_Stocks WHERE id=1;")
#    x.fetchall()
    fetch = x.fetchall()
    for r in fetch:
        print len(r)
        for a in r:
            return a

    
#print select_db('Bens_Stocks','Shares',1)
select_db("Bens_Stocks","Shares",1)

#x = conn.cursor()
#comp = "APPL"
#iD = x.execute("SELECT Symbol FROM Symbol WHERE idSymbol=1")
#print x.execute("SELECT ID FROM Users WHERE UserName='"+'NickG'+"'")
#print type(iD)
#print iD
#SELECT Shares FROM Bens_Stocks WHERE id=1;

#update_Symbol("fu",1)
    
    