# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 12:30:54 2015

@author: greenbotics
"""

this document is a note of where I  am and what I need to do

October 12th:
    To do:
        -First I need to filter all of the traders that I initial add
            This could be done with a user imput.  The program stops, gives me a link. I look at it and say y or n.  
            if y then it gets added to users, if no it get added to a deleted users table:
                
            -I need a create table function that 
            
            
            
            
    For the quick and easy test(Oct 12):
        -I need to create a table with traders that I like and their most recent trades.  Maybe get 10 traders together
        -I run an update script every half an hour and trade all the trades they make with 5% of my "total" funds lets say I start with $5000
            -one thing that would be nice to have is a way to save the last trade and the date it was entered into the database
            *Get trader name out of link with a method and pass it to the DB
        -Need to get python dateTime installed 
            -once done just add a column to the db for time, if the last trade is different just update the time and trade.  (make sure to look if buy or sell)
     Oct 16: right now my database is empty, so Im going to populate it, and then run the instert ignore on multiple rows and see if it doesnt add more traders bc I just ran it and it shouldnt have seen anything new
     Oct 17:ok here is how you do it- don't worry about the names of people.  just create tables where 
             unique id is the stock symbol.  then you just have to figure out how to "buy" the stock 
             -use the update function (Use Code Accedemy for this) you have now to just start the table, then have a real update table function.  
             And try actually using the "update" MySQL function!!
    Oct 18:  You can run the command that uses insert ignore first before the you run the MySQL update command.  The reason is that the MySQL insert
                wont update any values
    Oct 30: Where did I leave off?  I am on sell_stocks and need to fix the update command in my DB to include Table and Columns as well 
    Nov 2: Goal, by wednesday get a thing working with autoTrading probably on my stupid Fajitsu or Raspberry pi.  My idea is to have a loop that
            runs the checker to see if anyone made a trade change every 10 min.  This then updates my portfolio and then updates a graph the has the 
            value of my net worth and all of my positions with a legend.  The key here is that it is somehow updateing every 10 min with a history.
    Nov 9:  Use FetchOne instead of FetcAll in selectone!!!! db function 
    Nov 12: Its working now I just need to ask Eric how he thinks i can use the dates to create a performance log if how its doing with dates maybe
            And then in the mean time I can start trying to control an andriod app through python on a VM. 
            -also to fix the problem of having tons of rows if you are always adding new rows on buy and sell.  If the total value changes significantly
            add a new row if not, just do an update on the most recent one.  
            -tonight work on inserting the datetime and sorting the col to get most recent total values
    Nov 15: Add an area that holds symbol and buy or sell in every portfolio balance
    Nov 18: Fix the amount of stocks that are bought, in terms of value everything is completely skewed
    Nov 20: Add more initial funds to begin with.  Ok here is how you do the back testing and possibly combine it with what is going on now.  
            take you exiting stock table and build off of dan G fork with Yahoo.  The modified version of the table should include who the trade 
            was made by.  if it included this, then I could use the new file to gather all trades to a certain date lets say the past 24 months.
            Now I can filter by all trades made by so and so and date them and then run it through the trading app to see who is the best
            -Also work on the graphinng feature.
    Dec 3:  Here is something you could use codementor for.  Get this lady to help you grap all of the data in these tables and filter it quickly.
            Numpy might be able to do this.  Basically if you could grab all the data page after page quickly and store it all in Numpy, then 
            just search for dates somehow. Trunkate the numpy array, delete everything that has a 
            -Ok nmv new thought, lets just write a script that freeking takes every thing on every link to the trading table and put in 
              a db for that trader, then I can just filter it like crazy and say, I want all buys and sells between such and such a date
             -gettting the table on the page is fine, now clean up the output so you can start shoving it into the DB
        
    Controlling the app(Oct 12):
        Erik and I were talking today, and i think if I were to run everything on an EC2, then the processing would be way faster bc you can thread
        it.  Annndd Erik knows of a way to control the app through clicking so all I need to do is figure out how to run andriod as a VM on 
        an EC2.  But to start off I just need to get a VM of android to run on my PC and then make python interact with it.
        
        
    Problems:
        SQL- Oct 30 many problems, but one in particular is I can now send multiple columns data to be inserted but not multiple rows at once
                which means each time i want to add a new row, I need to reopen the connection and make a cursor or something like that...
                