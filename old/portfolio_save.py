# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 00:43:43 2015

@author: greenbotics
"""

import requests
from bs4 import BeautifulSoup
import MySQLdb


conn = MySQLdb.connect(host="bamdm.c81zpi4sue10.us-west-1.rds.amazonaws.com", user="BAM",passwd='cooler94550',db = 'BAMDB')
#query = "INSERT INTO tablename (feild we insert into) values ('what we want to send in the feild')
##-----------------------
#query = "INSERT INTO Users (UserName) values ('DannyA')"
         #INSERT INTO Users (UserName) values ('Dan Gustafson 3025')
#x = conn.cursor()
#x.execute(query)
###row = x.fetchall()
##conn.execute(query)
#conn.commit()
#conn.close()
##-------------------------

def send_to_dataBase(Table,Column,Data):
    print "start"
    print Column
    print Data
    if type(Column) is list:
        print "im in"
        column = ""
        data = ""
        n = 0
        m = 0
        for c in Column:
            if n == 0:
                column = column+c
            else:
                column = c+","+column
            n +=1
                
        for d in Data:
            if m == 0:
                data = data+d
            else:
                data = d+","+data
            m +=1
            print d 
            print data
        print data
        print column
        query = "INSERT IGNORE INTO "+Table+" ("+column+") values ("+data+")"
    else:
        query = "INSERT IGNORE INTO "+Table+" ("+Column+") values ("+Data+")"
    print query
    x = conn.cursor()
    x.execute(query)
    conn.commit()
    print "stop"
    #conn.close()

#def send_to_dataBase_foreignkey(Table,Column)
    
#def delete_data_from_database():
    #Delete * FROM BAMDB.Users;
    
    

def get_portfolio_names(soup):
    portfolios = []
    names = []
    for port in soup.find_all("a"):
        #print port
        p = str(port)
        if "java" in p:
            #print port.text
            names.append(port.text[0:])
            link = "http://stockwars.cidevelop.com/portfolios/"+port.text[0:]+'?view=v'
            portfolios.append(link)
    return portfolios, names



def get_rank_and_dateLastTrade(UserName,portfolio): #method will get rank form users page
    i = 0    
    print len(portfolio)
    for p in portfolio:
        r = requests.get(str(p))
        soup = BeautifulSoup(r.content)
        for port in soup.find_all("div"):
            s = str(port)
            print "----------------------"
            #print port
            print "---------------------"
#            if "smallertext" in s:
#                if "Traded" in s:
#                    #print port.text
#                    #print s
#                    x = s.find("Traded")
#                    y = s.find(" ",(x+1))
#                    print s[y+1:y+2]
#                    #print "heyyyyyyyyyyy"
            if "smalltext" in s:
                if "Ranked" in s:
                    #print port.text
                    x = s.find("#")
                    y = s.find(" ", (x+1))
                    r = s[x+1:y]
                    print r
                    print "hiiiii"
                    #x = s.find()
                    if "," in r:
                        a = r[:r.find(",")]+r[(r.find(",")+1):]
                        print a
                        Rank = int(a)
                    else:
                        Rank = int(r)
                    if (Rank < 4000):
                        print UserName[i]
                        print Rank
                        #u =  "Users","UserName","\'"+UserName[i]+"\'"
                        u =  "Users","UserName",Rank
                        print u
                        print "hi hi hi"
                        #UserName[i] = UserName[i].replace('-','')
                        #send_to_dataBase("Users","UserName","\'"+UserName[i]+"\'")
                        #need a method to get Foreign Key!
                        # need to figure out how to only insert certain data!!
                        #for instance- only inserting Rank but not all the other shit for an initial INSERT
                        #fk = SELECT * FROM Users WHERE UserName = 'UserName[i]'
                        cur = conn.cursor()
                        cur.execute("SELECT ID FROM Users WHERE UserName='"+UserName[i]+"'")
                        rows = cur.fetchone()
                        Column = ["UserId","Rank"]
                        print "YAAAAYY"
                        print rows[0]
                        
                        Data = [str(rows[0]),str(Rank)]
                        print Data
                        print Rank
                        ##Column = ["UserId","Rank"]
                        #3Data = [fk,Rank]
                        send_to_dataBase("User_Info",Column,Data)
                        
                else:
                    print "nope"
                    print i
        i +=1



def next_page(soup):
    print "hi"
    for port in soup.find_all("a"):
        l = str(port)
        next_l = ' '
        if "portfolios?" in l:
            print "heyyyyyyyyyyyy"
            nxt_page = port.get("href")
            next_l = "http://stockwars.cidevelop.com/"+nxt_page
            #print next_l
            break
            #print next_l
    return next_l

def cycle_through_pages(initial_page):
    number_pages_to_cycle = 5
    n = 0
    temp = initial_page
    num_transactions = []
    names = []
    strNames = []
    t = next_page(initial_page)
    while n < number_pages_to_cycle:
        if n > 0:
            #Mr broprint n
            #print "klajsdflkja"
            t = next_page(initial_page)
            #print t
            b = requests.get(t)
            soup = BeautifulSoup(b.content)    
            #print soup
            num_transactions = num_transactions + get_portfolio_names(soup)[0]
            names = names + get_portfolio_names(soup)[1]
        else:
            #print n
            num_transactions = num_transactions + get_portfolio_names(temp)[0]
            names = names + get_portfolio_names(temp)[1]
        #print num_transactions
        n +=1
    for y in names:
        strNames.append(str(y))
    return num_transactions, strNames

#after you have your list of links and profiles untfiltered, this calls 
#the database function
def cycle_through_profile_links_to_add(portfolios, names):
    n = len(names)
    i = 0
    while i <n:
        n = 0
        
    

rank = 2000 #must be in top 1000 traders
r = requests.get("http://stockwars.cidevelop.com/portfolios?PortfolioName=&PortfolioPassword=&order=transactions&direction=DESC&filter=#")
#r = requests.get("http://stockwars.cidevelop.com//portfolios?order=transactions&direction=DESC&cursor=CkAKEwoMdHJhbnNhY3Rpb25zEgMIhisSJWoPc35jaXN0b2Nrd2Fyc2hychILEglQb3J0Zm9saW8YrLLCCQwYACAB")
#r= requests.get("http://stockwars.cidevelop.com/portfolios/Brendan%20Thrapp?view=v&full=NO")
soup = BeautifulSoup(r.content)    
print "--------------"
#print get_portfolio_names(soup)
#next_page(soup)

portfolios,names =  cycle_through_pages(soup)
get_rank_and_dateLastTrade(names,portfolios)
#print type(names[1])



#z= get_rank_and_dateLastTrade(1,soup)
#print z
#send_to_dataBase("Users","UserName","'DannyC'")

#get all transactions and build love or List it for traders to determine if 
        #They are actially good at what the do

# how to get to an individual Portfolio!!!!!!!
    #http://stockwars.cidevelop.com/portfolios/Paulj114?view=v
    
## this is it!!! http://stockwars.cidevelop.com/portfolios?PortfolioName=&PortfolioPassword=&order=rank&direction=ASC&filter=#

#Build Class or several methods to dertime if a trader is proficient or just 
    #plain luck called luck or skilled 



#CREATE TABLE `BAMDB`.`Users` (
#  `UserName` VARCHAR(50) NOT NULL COMMENT '',
#  `ID` INT NOT NULL AUTO_INCREMENT COMMENT '',
#  UNIQUE INDEX `UserName_UNIQUE` (`UserName` ASC)  COMMENT '',
#  PRIMARY KEY (`ID`)  COMMENT '');


# Second Table!!!!!!!!!!!!
#CREATE TABLE `BAMDB`.`User Info` (
#  `Id` INT NOT NULL AUTO_INCREMENT COMMENT '',
#  `UserId` INT NULL COMMENT '',
#  `Rank` INT NOT NULL COMMENT '',
#  `Last Traded` INT NOT NULL COMMENT '',
#  `Date Added` DATE NULL COMMENT '',
#  PRIMARY KEY (`Id`)  COMMENT '',
#  INDEX `User Info_FK_idx` (`UserId` ASC)  COMMENT '',
#  CONSTRAINT `User Info_FK`
#    FOREIGN KEY (`UserId`)
#    REFERENCES `BAMDB`.`Users` (`ID`)
#    ON DELETE CASCADE
#    ON UPDATE NO ACTION);
