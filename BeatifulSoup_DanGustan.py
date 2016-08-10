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
from dbFunctions import send_to_dataBase


conn = MySQLdb.connect(host="bamdm.c81zpi4sue10.us-west-1.rds.amazonaws.com", user="BAM",passwd='cooler94550',db = 'BAMDB')

def recent_trade(soup): #only off very specific trade page takes in list of soups 
    recent_trades = []
    buy = []
    if type(soup) is list:
        print "recent tr"
        for page in soup: #s is a full page i think
            table = page.findAll("tr")
            #href = soup.findAll("transactions")
            n =0
            for t in table:
                n += 1
                if n == 7: #this should be returning a row
                    td= t.findAll("td")
                    print len(td)
                    for tag in td:# these are elements in the row, tag is a soup element type
                        #print tag
                        #print tag
                        if tag.findAll('a'): #looking for the hyperlink wih the stock symbol
                            a = tag.findAll("a")
                            a = str(a)
                            end = a.find("?")
                            start = a.find(":")
                            symbol = a[start+1:end]
                            recent_trades.append(symbol)
                        tagS = str(tag)
                        print tagS
                        #
                        #print len(a)
                        #for aa in a:
                        #    print aa
                        #    break
                        if "Buy" in tagS:   # looking for buy or sell and then breaking out to go to next page
                            buy.append("Buy")
                            break
                            print "hey"
                        elif "Sell" in tagS:
                            print "you"
                            buy.append("Sell")
                            break
                        elif "Dividend" in tagS:
                            buy.append("Dividend")
        return recent_trades, buy
#                    print t 
#                    break
#                    t = str(t)
#                    print "hi",t
#                    end = t.find("?")
#                    start = t.find(":")
#                    #print place, splace
#                    symbol = t[start+1:end]
#                    print symbol
#                    recent_trades.append(symbol)
                    #break
#    recent_trades = []
#    if type(soup) is list:
#        print "recent tr"
#        for s in soup:
#            table = s.findAll("a")
#            #href = soup.findAll("transactions")
#            n =0
#            for t in table:
#                n += 1
#                if n == 3:
#                    t = str(t)
#                    print "hi",t
#                    end = t.find("?")
#                    start = t.find(":")
#                    #print place, splace
#                    symbol = t[start+1:end]
#                    print symbol
#                    recent_trades.append(symbol)
#                    #break
            
                
                

def update_db(links):# this is the main method that uses all others.  takes in list of links
#    #call get_name_from_links
    n = 0
    names = user_name_from_links(links)
#    #from this list call get_last_trade
    htmlsoup_list = get_htmlsoup(traders_links)
    traded_company, BorS = recent_trade(htmlsoup_list)
    print traded_company, BorS
    #past_trade = get_last_trade(names[n])
    columns = ["User","Last_trade","buy_sell"]
    for t in traded_company:
        dataList = ["\'"+str(names[n])+"\'","\'"+str(t)+"\'","\'"+str(BorS[n])+"\'"]
        send_to_dataBase("Traders",columns,dataList)
        n+=1        
#    while n < len(traded_company):
#        try: # this try is to determine if the trade aquired is a new trade or not by looking at the symbol and bur or sell(datse should be included eventuall)
#            past_trade = get_last_trade(names[n])
#            if past_trade == traded_company[n]:
#        except:
#            print "oh craaaaaappppp"
#            break
        
#    while True:
#    try:
#        kx = int(raw_input("Please enter a number: "))
#        break
#    except ValueError:
#      print "Oops!  That was no valid number.  Try again..."
      #---------------------------
#    #if it returns null or none then 
#        #run recent trade and add recent trade with buy or sell
#    #else
#        #compare getlast trade to recent trade and buy sell
#            # if the differ add recent trade
#            # if not don't add it!
    

def get_last_trade(UserName):#gets the last made trade from the DB
    cur = conn.cursor()
    #cur.execute("SELECT last_Trade FROM Users WHERE UserName='"+UserName+"'")
    cur.execute("SELECT last_Trade,buy_sell FROM Traders WHERE UserName='"+UserName+"'")

        
        

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
             

#def get_portfolio_names(htmlsoup):
#    portfolios = []
#    names = []
#    for port in soup.find_all("a"):
#        #print port
#        p = str(port)
#        if "java" in p:
#            #print port.text
#            names.append(port.text[0:])
#            link = "http://stockwars.cidevelop.com/portfolios/"+port.text[0:]+'?view=v'
#            portfolios.append(link)
#    return portfolios, names

#r = requests.get("http://stockwars.cidevelop.com/portfolios/Dan%20Gustafson%203025?view=v&full=NO")
traders_links = ['http://stockwars.cidevelop.com/transactions/Dan%20Gustafson%203025?view=v','http://stockwars.cidevelop.com/transactions/omar_baker1?view=v','http://stockwars.cidevelop.com/transactions/perikx1?view=v','http://stockwars.cidevelop.com/transactions/Jbetterton?view=v','http://stockwars.cidevelop.com/transactions/Matlas?view=v','http://stockwars.cidevelop.com/transactions/dmeier2?view=v','http://stockwars.cidevelop.com/transactions/studliestone?view=v']

#http://stockwars.cidevelop.com/transactions/Jbetterton?view=v
#htmlsoup = get_htmlsoup(traders_links)
#print type(htmlsoup)
###recent_trade(htmlsoup)
#user_name_from_links(traders_links)
#print htmlsoup
update_db(traders_links)


#<a href="/transactions/Dan%20Gustafson%203025/NYSE:CLF?view=v&amp;full=NO">NYSE:CLF</a>                 




#Column = ["Account","Last_trade"]
##rows = ["Dan",trunk]
#rows = ['\"Dan\"','\"appl\"']
#print rows
#send_to_dataBase("Traders",Column,rows)