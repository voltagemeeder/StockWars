# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:37:16 2015

@author: greenbotics
"""

from yahoo_finance import *
import MySQLdb
import time
import datetime
#myfiles below
from dbFunctions_forkfork import *


def buy_a_stock(symbol,shareNum):#takes you stock and 
    yahoo = Share(symbol)
    print "symbol", symbol
    price = yahoo.get_price()
    if type(price) is str: #this is effectivley checking if the symbol is found in yahoo finance
        p = float(price)
        newshare = int(700/p)
        shareNum = newshare
        print "newshare",shareNum
        print "im in"
        value = float(shareNum)*float(price)
        buying_power = update_portfolio_balance(0,2)
        #value = "10"
       # print type(value)
        cols = ['Cash_Value','Shares']
        colSend = ['Cash_Value','Shares','Symbol']
        rows = [value,shareNum,symbol]
    #    cols = ['Shares','Symbol']
    #    rows = [str(shareNum),'YHOO']
        print buying_power
        print buying_power - value
        if buying_power > value: # this is checking if you have enough funds to buy the stocks
            if send_to_dataBase("Bens_Stocks",colSend,rows)== False: # this is checking if you already have the stock and are adding to it
                print "bought"
            else:# maybe you need to select the previous value of this stock and just increment it by 2.  For now lets just never have any shares go above 2
                sym = "Symbol = \'" + symbol + "\'"
                sharesStr = select_db_single("Bens_Stocks","Shares",sym)
                shares = int(sharesStr)
                #print "YEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAH",sharesStr, shares
                if shares > 0: #right now if it has any shares at all
                    print "buy_a_stock, already had it"
                else:
                    update_Symbol_Uni("Bens_Stocks",cols,"SYMBOL",rows)
                    print "bought updated"
            update_portfolio_balance(value,1)
        else:
            print "it wasn't enough"
            
    
def sell_a_stock(symbol): #This method should update a preexisting stock row
    stock = Share(symbol)
    price = stock.get_price()
    sym = "Symbol = \'" + symbol + "\'" #reformatting the Symbol to look like Symbol = 'APPL'
    #print sym 
#    value =  float(select_db("Bens_Stocks","Shares",sym)) * float(price)
    shareNum =  select_db_single("Bens_Stocks","Shares",sym)
    #Cash_Value = select_db_single("Bens_Stocks","Cash_Value",sym)
    if type(shareNum) is not str:
        print "im about to break"
        print type(shareNum)
        print shareNum
    else:
        value = float(shareNum)*float(price)
        print "this is value",value
        #    cols = ['Cash_Value','Shares','Symbol']
        cols = ['Shares','Cash_Value']
        data = [0,0,symbol]
        update_Symbol_Uni("Bens_Stocks",cols,"SYMBOL",data)
        update_portfolio_balance(value,0)



def update_portfolio_balance(Cash_Value,BorS): #needs to select all stock values, add them uo then add it to the tital not invesred.  then run sell, it sells. total money is not changed but uninvested gers selected and added to
    #original_value = select_db_single("Bens_Portfolio_Value","id",1)
    print "Starting to Update portfolio Balence"
    total_value =  select_db_topDate("Total_Value")
    original_value = select_db_topDate("UnusedFunds")
    DTime = datetime.datetime.utcnow()
    #original_value = select_db_single("Bens_Portfolio_Value","Total_Value","id =0")
    original_value = float(original_value)
    print "Unused Funds",original_value 
    values_list = select_db("Bens_Stocks","Cash_Value",'*')
    Stock_Value = 0
    for r in values_list:
        print " vlaueslist"
        print r
        for a in r:
            print "list inside"
            a = float(a)
            Stock_Value += a
    print Stock_Value
    if BorS == 1: # 0 is sell 1 is buy
        Total_Value = total_value
        UnusedFunds = Total_Value - Stock_Value
        cols = ['Total_Value','Stock_Value','UnusedFunds','DTime']
        data = [Total_Value,Stock_Value,UnusedFunds,DTime]
        send_to_dataBase("Bens_Portfolio_Value",cols,data)
    elif BorS ==0:
        Total_Value = original_value + Stock_Value + Cash_Value
        UnusedFunds = Total_Value - Stock_Value
        cols = ['Total_Value','Stock_Value','UnusedFunds','DTime']
        data = [Total_Value,Stock_Value,UnusedFunds,DTime]
        send_to_dataBase("Bens_Portfolio_Value",cols,data)
    elif BorS == 2:
        Total_Value = total_value
        print "just grabbing"
        UnusedFunds = Total_Value - Stock_Value
    return UnusedFunds


#update_portfolio_balance(0,1)
#question for Eric 

#select_db_single("Bens_Portfolio_Value","UnusedFunds","id =0")http://www.ebay.com/itm/Headphoneque-Replacement-Ear-Pad-Cushion-BOSE-Quiet-Comfort-QC-2-QC-15-/140792627793?hash=item20c7e50251
#test all Trades functions 
#buy_a_stock
#print get_price('YHOO')
#yahoo = Share('YHOO')
#print yahoo.get_price() 
#buy_a_stock('CHK',2)
#buy_a_stock('C',2)
#sell_a_stock('C')
#sell_a_stock('NFLX')
#print update_portfolio_balance(0,1)

#symbol = "WFC-J"
#yahoo = Share(symbol)
#print "symbol", yahoo
#price = yahoo.get_price()
#if type(price) is str:
#    print "crap"