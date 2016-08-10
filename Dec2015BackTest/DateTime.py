# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 17:47:09 2015

@author: greenbotics
"""

import time
import datetime
import sched
from BeatifulSoup_DanGustanFork_TwithYahoo import real_update

today = datetime.date.today()
print today
print datetime.datetime.utcnow()

traders_links = ['http://stockwars.cidevelop.com/transactions/Dan%20Gustafson%203025?view=v','http://stockwars.cidevelop.com/transactions/omar_baker1?view=v','http://stockwars.cidevelop.com/transactions/perikx1?view=v','http://stockwars.cidevelop.com/transactions/Jbetterton?view=v','http://stockwars.cidevelop.com/transactions/Matlas?view=v','http://stockwars.cidevelop.com/transactions/dmeier2?view=v','http://stockwars.cidevelop.com/transactions/studliestone?view=v']

#s = sched.scheduler(time.time, time.sleep)
#def do_something(sc): 
#    print "Doing stuff..."
#    DTime = datetime.datetime.now()
#    # do your stuff
#    #sc.enter(1, 1, do_something, (sc,))
#
##s.enter(5, 1, do_something, (s,)) #(delay, priority, action, argument)¶
##s.run()

DTime = datetime.datetime.now()
print "DTime", DTime
#datetime.now(tz=None)¶

#Nope I decided don't worry so much about the time... just runs a real update every 5 min 
    #but eventually, it should check the day is a weekday, that the market is open 9AM to 4:30 East Standard time
sec_trade_day = 60*60*3
sleeptime = 500
final = sec_trade_day/sleeptime
n = 0
while n <19:
    #s.enter(300, 1, real_update(traders_links), (s,))
    real_update(traders_links)
    print "done"
    time.sleep(900)
    n+=1