# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 21:16:57 2015

@author: greenbotics
"""

import requests
from bs4 import BeautifulSoup
from yahoo_finance import Share
import MySQLdb
#myfiles below
from SoupFunctions import get_htmlsoup
#from dbFunctions import *
from dbFunctions_forkfork import *
from Trades_w_yahoo import *

conn = MySQLdb.connect(host="bamdm.c81zpi4sue10.us-west-1.rds.amazonaws.com", user="BAM",passwd='cooler94550',db = 'BAMDB')

def recent_trade(soup): #only off very specific trade page takes in list of soups 
    recent_trades = []
    buy = []
    if type(soup) is list:
        print "recent trades"
        for page in soup: #s is a full page i think
            table = page.findAll("tr")
            #href = soup.findAll("transactions")
            n =0
            for t in table:
                n += 1
                if n == 7: #this should be returning a row
                    td= t.findAll("td")
                    #print len(td)
                    for tag in td:# these are elements in the row, tag is a soup element type
                        if tag.findAll('a'): #looking for the hyperlink wih the stock symbol
                            a = tag.findAll("a")
                            a = str(a)
                            end = a.find("?")
                            start = a.find(":")
                            symbol = a[start+1:end]
                            recent_trades.append(symbol)
                        tagS = str(tag)
                        #print tagS
                        if "Buy" in tagS:   # looking for buy or sell and then breaking out to go to next page
                            buy.append("Buy")
                            break
                        elif "Sell" in tagS:
                            buy.append("Sell")
                            break
                        elif "Dividend" in tagS:
                            buy.append("Dividend")
        return recent_trades, buy
                
def take_the_table(soup): #only off very specific trade page takes in list of soups 
    recent_trades = []
    buy = []
    Column = ["Date", "Balance","Symbol","Type","Qty","Price","Amount"]
    if type(soup) is list:
        print "recent trades"
        for page in soup: #s is a full page i think
            table = page.findAll("tr")
            #href = soup.findAll("transactions")
            n =0
            for t in table:
                n += 1
                if n == 7: #this should be returning a row
                    td= t.findAll("td")
                    #print len(td)
                    for tag in td:# these are elements in the row, tag is a soup element type
                        print tag
    else:
        print "singlink"
        thesoup = get_htmlsoup(soup)
        table = thesoup.findAll("tr")
        #href = soup.findAll("transactions")
        n =0
        #print table
        for t in table: #this should be returning a row
            n += 1
            if (n > 7): 
                temp = []
            #td= t.findAll("td")
                #print t.text
                for link in t.findAll("td"):
                    if (link.get('colspan')) == None: # Filtering out the "Next"
                        #print "-----------------------"
                        #print link.text, type(link.text)
                        temp.append(str(link.text))
                if len(temp) != 0:
                    send_to_dataBase("Dan_G",Column,temp)

def make_all_trades(database):
    Column = ["Date","Symbol","Type","Price"]
    fetch = select_db(database,Column,"*")
    for f in fetch:
        print f
                    

def real_update(links):#this runs function form db and passes in the id needed and the buy or sell
    n = 0
    # i think what needs to happen here is that there are three cases buy seel deividen and depending on which it is 
    # you call the function sfrom Trades_w_yahoo.  The Buy sell or Dividend doesnt need to go into the database i don't think 
#    #from this list call get_last_trade
    htmlsoup_list = get_htmlsoup(traders_links)
    traded_company, BorS = recent_trade(htmlsoup_list)
    print traded_company, BorS
    cols = ["",""]
    for comp in traded_company:
        #iD = cur.execute("SELECT iD FROM Symbol WHERE UserName='"+comp+"'")
        print "real_update",BorS[n]
        if BorS[n] == "Buy":
            buy_a_stock(traded_company[n],2)
        elif BorS[n] == "Sell":
            sell_a_stock(traded_company[n])
        else:
            print "it was a div"
        cur = conn.cursor()
        iD = cur.execute("SELECT idSymbol FROM Symbol WHERE Symbol=%s",comp)
        #update_Symbol_Uni(BorS[n],iD)
        data = ["",""]
        #update_Symbol_Uni("Bens_Stocks",cols,"SYMBOL",data)
        n+=1


def user_name_from_links(link_list): # returns list of usernames in a list of linked trade pages
    user_names = []
    for link in link_list:
        name_start = link.find('transactions/')+ len('transactions/')
        name_end = link.find('?view=v')
        name = link[name_start:name_end]
        name_edit = name.replace('%','')
        user_names.append(name_edit)
    print user_names
    return user_names
    


#r = requests.get("http://stockwars.cidevelop.com/portfolios/Dan%20Gustafson%203025?view=v&full=NO")
traders_links = ['http://stockwars.cidevelop.com/transactions/Dan%20Gustafson%203025?view=v','http://stockwars.cidevelop.com/transactions/omar_baker1?view=v','http://stockwars.cidevelop.com/transactions/perikx1?view=v','http://stockwars.cidevelop.com/transactions/Jbetterton?view=v','http://stockwars.cidevelop.com/transactions/Matlas?view=v','http://stockwars.cidevelop.com/transactions/dmeier2?view=v','http://stockwars.cidevelop.com/transactions/studliestone?view=v']

#http://stockwars.cidevelop.com/transactions/Jbetterton?view=v
#htmlsoup = get_htmlsoup(traders_links)
#print type(htmlsoup)
###recent_trade(htmlsoup)
#user_name_from_links(traders_links)
#print htmlsoup

#update_db(traders_links)
#real_update(traders_links)

#<a href="/transactions/Dan%20Gustafson%203025/NYSE:CLF?view=v&amp;full=NO">NYSE:CLF</a>                 
take_the_table('http://stockwars.cidevelop.com/transactions/Dan%20Gustafson%203025?view=v')
make_all_trades("Dan_G")


#Column = ["Account","Last_trade"]
##rows = ["Dan",trunk]
#rows = ['\"Dan\"','\"appl\"']
#print rows
#send_to_dataBase("Traders",Column,rows)