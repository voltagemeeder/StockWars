# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:22:10 2015

@author: greenbotics
"""
import datetime
import dateutil.parser
import pytz

x = '2012-01-15 10:19:00'
      
def parse_date(self, date_text):
    payment_date = None
    try:
        naive_date = dateutil.parser.parse(date_text.strip())
        local_date = self.timezone.localize(naive_date)
        payment_date = local_date.astimezone(pytz.UTC)
    except ValueError:
        self.logger.warning("Cannot parse date: '%s'" % date_text.strip())
    return payment_date
    

parse_date(x)