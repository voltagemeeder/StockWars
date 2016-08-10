# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 17:21:52 2015

@author: greenbotics
"""
#import sys
#(x,y) = (5,0)
#try:
#    z = x/y
#    except ZeroDivisionError:
#        print "divide by zero"

while True:
    try:
        kx = int(raw_input("Please enter a number: "))
        break
    except ValueError:
      print "Oops!  That was no valid number.  Try again..."