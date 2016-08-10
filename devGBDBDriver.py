import MySQLdb
import time
import os
import json
import sys
import pdb
from datetime import datetime
sys.path.insert(0, '../Scripts')
sys.path.insert(0,"C:/EC2/GBmapper/Scripts")
from getConnection import getConnectionData

def connect():
    # print "connecting to database"
    con = getConnectionData()
    if con == False:
        print "failed to find connection data"
        return None
    db = MySQLdb.connect(con["server"],con["userName"],con["password"],con["database"] )
    cursor = db.cursor()
    # print "connected!"
    return [db,cursor]

def disconect(connection):
    connection[0].close()

def getLayoutJobs(connection):
	sql = "SELECT OpportunityID, Rev, Status, Location, Name, ID FROM siteDev.LayoutJobs where status = 'requested';"
	connection[1].execute(sql)
	return connection[1].fetchall()

def updateLayoutStatus(ID,status,connection):
	sql = "UPDATE siteDev.LayoutJobs SET\
		Status = '%s' where ID = '%s';" % (status,ID)
	connection[1].execute(sql)
	connection[0].commit()

def addLayoutJob(opID, rev, path, simName, connection):
    sql = "INSERT INTO siteDev.LayoutJobs (`OpportunityID`, `Rev`, `Status`, `Location`, `Name`) \
    VALUES ('%s', '%s', 'requested', '%s', '%s');" % (opID, rev, path, simName)
    connection[1].execute(sql)
    connection[0].commit()

# def setOutputPath(ID, outPath, connection):
#     sql = "UPDATE siteDev.LayoutJobs SET\
#         OutputPath = '%s' where ID =  '%s';" %(outPath, ID)

def getJobInfo(OpportunityID, Rev, Name, connection):
    sql = "SELECT OpportunityID, Rev, Status, Location, Name, ID, OutputPath \
    FROM siteDev.LayoutJobs where OpportunityID = '%s' and Rev = '%s' and Name = '%s';" %(OpportunityID, Rev, Name)
    connection[1].execute(sql)
    return connection[1].fetchall()   
