#import tkinter
from guizero import *
import datetime
import calendar
#import asyncio
#import socket
#import os
#import sys
#from msg_parser import MessageParser
from filelock import Timeout, FileLock
#import tkinter

settings_file = "./config/settings.json"
def check_settings():
		lock = FileLock(settings_file + ".lock", timeout=2)
		s_data = None
		try:
			with lock:
				settings_data_fhandle = open(settings_file)
				settings_data = settings_data_fhandle.read()
				print(settings_data)
		except Timeout:
			print("Failed to acquire file lock")
		finally:
			lock.release()


#Global Variables
global my_name
my_name = "Dr. Peng"


#Grid Location Variables - We will change these grid numbers to change Locations. [x,y]
global Time_Date_Greeting_Grid, Calendar_Grid
Time_Date_Greeting_Grid = [0,0]
Calendar_Grid = [0,3]


#Visibility for Boxes
global Time_Date_Greeting_Visible, Calendar_Visible
Time_Date_Greeting_Visible = 1
Calendar_Visible = 1

global now, display_clock, display_date
now = datetime.datetime.now()
display_clock = now.strftime("%I:%M %p")
display_date = now.strftime("%a %b-%d, %Y")
cal = calendar.TextCalendar(calendar.SUNDAY)

#class CursorOff(object)
#    def _enter_(self):
#        os.system('setterm -cursor off')
#
#    def _exit_(self,*args):
#        os.system('setterm -cursor on')



def update():
	now = datetime.datetime.now()
	display_clock.set(now.strftime("%I:%M %p"))
	display_date.set(now.strftime("%a %b-%d, %Y"))
        
#os.system('setterm -cursor off')
try:
	app = App(title="Mirror Mirror", width=1500, height=800, layout="grid", bg="black")

	#Black-Background Boxs- Will set all to Black525x425.png for final set. Use colors for debug
	B1 = Picture(app, image="Black525x425.png", grid=[0,0])
	B2 = Picture(app, image="Red525x425.png", grid=[0,1])
	B3 = Picture(app, image="Green525x425.png", grid=[0,2])
	B4 = Picture(app, image="Orange525x425.png", grid=[0,3])
	B5 = Picture(app, image="Yellow525x425.png", grid=[1,0])
	B6 = Picture(app, image="Blue525x425.png", grid=[1,1])


	#Time_Date_Greeting_Grid Section- WORKING!
	Box1 = Box(app,layout="grid", grid=Time_Date_Greeting_Grid, visible=Time_Date_Greeting_Visible)
	if(now.strftime("%h") < "12"):
	display_clock = Text(Box1, text = display_clock, grid=[0,0], color="white", size="45")
	display_date = Text(Box1, text = display_date, grid=[0,1], color="white", size="45")
	display_greeting = Text(Box1, text = "\nGood Morning, \n"+my_name, grid=[0,3], color="white", size="45")   

	elif(now.strftime("%h") >= "12" and now.strftime("%h") < "19"):
	display_clock = Text(Box1, text = display_clock, grid=[0,0], color="white", size="45")
	display_date = Text(Box1, text = display_date, grid=[0,1], color="white", size="45")
	display_greeting = Text(Box1, text = "\nGood Afternoon, \n"+my_name, grid=[0,3], color="white", size="45")

	elif(now.strftime("%h") >= "19"):
	display_clock = Text(Box1, text = display_clock, grid=[0,0], color="white", size="45")
	display_date = Text(Box1, text = display_date, grid=[0,1], color="white", size="45")
	display_greeting = Text(Box1, text = "\nGood Evening, \n"+my_name, grid=[0,3], color="white", size="45")


	#Calandar Section. Not working, Everything is center aligned not aligned, not in columns
	year = int(now.strftime("%Y"))
	month = int(now.strftime("%-m"))
	calFormat = cal.formatmonth(year,month,0,0)
	print(calFormat)
	Box2 = Box(app, grid=Calendar_Grid, visible = Calendar_Visible)
	display_calendar = Text(Box2, text = calFormat, color="white", size="35", align="left")


	app.repeat(500,update)

	#sets full screen-Makes debug hard. To Get out: CTR+ALT+D
	app.tk.attributes("-fullscreen", True)

	#nocursor is not working to turn cursor to be invisible.
	#will need to find something else to make it invisible or move position to side/corner

	app.display()

except KeyboardInterrupt:
	event_loop.close()

