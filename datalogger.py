#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# datalogger.py
# 
# Append makerspace usage statistics to a Google Spreadsheet
# Takes 4 arguments: date, timestamp (HH:MM), accessed (0 or 1), uniqueToday (0 or 1),
# line to append to

import gspread
import sys
import os
import subprocess
from oauth2client.client import GoogleCredentials

# Grab credentials from local auth.json file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/root/auth.json"

credentials = GoogleCredentials.get_application_default()
credentials = credentials.create_scoped(['https://spreadsheets.google.com/feeds'])

Data_Spreadsheet = 'makerspace_headcount'

class MyDatalogger:
		
	def __init__(self, hour, visitors):
		self.visitors = visitors

		self.date = subprocess.check_output('date +"%D"', shell=True)
		self.date = self.date.strip()

		self.hour = subprocess.check_output('date +"%H"', shell=True)
		self.hour = self.hour.strip()

		self.values = [self.date, self.hour, self.visitors]
		
		try:
			self.openSpreadsheet()
			self.performAppend()
		except:
			print "Logger Error:"
			print sys.exc_info()
		
	
	#---------- Open Spreadsheet ----------
	# Login to the Google account and open the spreadsheet and
	# worksheet (account and sheet info are in constants.py)
	def openSpreadsheet(self):
		self.gc = gspread.authorize(credentials)
		print "\nConnected"
		self.wks = self.gc.open(Data_Spreadsheet).sheet1
		print "Opened Spreadsheet"
		
	#---------- Perform Append ----------
	# Update the appropriate cells.
	def performAppend(self):
		self.wks.append_row(self.values)	
		
		print "Appended to datalog"

		
# Main Script
		
if len(sys.argv) != 3:
	print "\nRequires 2 arguments: hour (HH), number of visitors"
	quit()

datalogger = MyDatalogger(sys.argv[1], sys.argv[2])
