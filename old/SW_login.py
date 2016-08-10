# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:21:18 2015

@author: greenbotics
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("http://stockwars.cidevelop.com/")
#print r.content

soup = BeautifulSoup(r.content)
#print soup.prettify()
print soup.find_all("input")

#all links in a page
for link in soup.find_all("a"):
    print link.get("href")