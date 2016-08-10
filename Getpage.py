# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:43:43 2015

@author: greenbotics
"""

import requests
import MySQLdb
from peewee import*

from bs4 import BeautifulSoup


def get_portfolio_names(soup):
    portfolios = []
    for port in soup.find_all("a"):
        p = str(port)
        if "java" in p:
            print port.text
            
        
r = requests.get("http://stockwars.cidevelop.com/portfolios?PortfolioName=&PortfolioPassword=&order=transactions&direction=DESC&filter=#")

#the only one I'm not taltally sure of is what the transaction sort does
# maybe just the # of transactions?
#Sorting by Transaction and DESC is the way to go!! it's better than Rank!!!
sort = ["rank","balence","prev_day_balance_change","last_login_date","last_transaction_date","create_date","name","country","transactions"]
soup = BeautifulSoup(r.content)


# displays link text and then the link itself
## however for my case the "link" seems to be '#' for all of them...
############
# here is a breakdown of the link
#<a href="#" onclick="javacript:getPortfolio('SAJJAN', 'SAJJAN');">SAJJAN</a>

#for link in soup.find_all("a"):
#    print link.text, link.get("href"), link.get("onclick")
    
print "--------------"
### sort portfolios 
#for option in soup.find_all("option"):
#    print link.text

print "heyyyyyyyyyyyy"

#get_portfolio_names(soup)







# how to get to an individual Portfolio!!!!!!!
    #http://stockwars.cidevelop.com/portfolios/Paulj114?view=v
    
## this is it!!! http://stockwars.cidevelop.com/portfolios?PortfolioName=&PortfolioPassword=&order=rank&direction=ASC&filter=#

#Build Class or several methods to dertime if a trader is proficient or just 
    #plain luck called luck or skilled 