# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 12:48:53 2015

@author: greenbotics
"""

import requests
from bs4 import BeautifulSoup

def get_htmlsoup(link): #gets 
    soups =[]
    if type(link) is list:
        for t in link:
            #print "im in"
            r=requests.get(t)
            soup = BeautifulSoup(r.content)
            soups.append(soup)
    else:
        r=requests.get(link)
        soups = BeautifulSoup(r.content)
    return soups
    
#traders_links = ['http://stockwars.cidevelop.com/transactions/Dan%20Gustafson%203025?view=v', 'http://stockwars.cidevelop.com/transactions/iihbki2?view=v','http://stockwars.cidevelop.com/transactions/perikx1?view=v']
#print get_htmlsoup(traders_links)