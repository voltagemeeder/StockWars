# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 02:27:11 2015

@author: bam8
"""

# tasks for tomorrow
# just start with one traders profile, doesn't matter who
# and extract data from main page such as last seen and rank
# then go into transactions page and get all of them


from splinter.browser import Browser
browser = Browser()

browser.visit('http://google.com')
browser.fill('q', 'splinter - python acceptance testing for web applications')
button = browser.find_by_css('.lsb').first
button.first.click()

if browser.is_text_present('http://splinter.cobrateam.info'):
    print "Yes, found it! :)"
else:
    print "No, didn't find it :("
    
browser.quit()