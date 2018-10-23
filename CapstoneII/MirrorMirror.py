from guizero import App, Text, Picture, Box
import datetime
import calendar
import asyncio
import socket
#from msg_parser import MessageParser
from filelock import Timeout, FileLock
#import tkinter


class SmartMirror:
	settings_file = "./conf/settings.json"
	def check_settings(self):
		lock = FileLock(self.settings_file + ".lock", timeout=2)
		s_data = None
		try:
			with lock:
				settings_data_fhandle = open(self.settings_file)
				self.settings_data = settings_data_fhandle.read()
				print(self.settings_data)
		except Timeout:
			print("Failed to acquire file lock")
		finally:
			lock.release()
		
	def update_gui(self):
		now = datetime.datetime.now()
		self.display_clock.set(now.strftime("%X %p")) #now.strftime("%I:%M %p"))
		self.display_date.set(now.strftime("%a, %b-%d, %Y"))
	
	def get_local_ip(self):
		s = socket.gethostname()
		return "Please connect to: %s.local " % s
	
	def __init__(self):
		self.app = App(title="Mirror Mirror", width=1500, height=800, layout="grid", bg="black")

		now = datetime.datetime.now()
		self.cal = calendar.TextCalendar(calendar.SUNDAY)

		if(now.strftime("%h") < "12"):
		    self.display_greeting = Text(self.app, text = "Good Morning,",grid=[0,0], color="white", size="30")
		elif(now.strftime("%h") >= "12" and now.strftime("%h") < "19"):
		    self.display_greeting = Text(self.app, text = "Good Afternoon",grid=[0,0], color="white", size="30")
		elif(now.strftime("%h") >= "19"):
		    self.display_greeting = Text(self.app, text = "Good Evening",grid=[0,0], color="white", size="30")

		self.display_clock = Text(self.app, text = now.strftime("%I:%M %p"),grid=[0,1], color="white", size="30")
		self.display_date = Text(self.app, text = now.strftime("%a, %b-%d, %Y"), grid=[0,2], color="white", size="20")
		self.display_ip = Text(self.app, text = self.get_local_ip(), grid=[1,6], color="white", size="12")

		year = int(now.strftime("%Y"))
		month = int(now.strftime("%-m"))
		box = Box(self.app, grid=[0,3], align="left")
		self.display_calendar = Text(box, text = self.cal.formatmonth(year,month), color="white")


		self.app.repeat(1000, self.update_gui)
		self.app.repeat(2000, self.check_settings)

		#sets full screen-Makes debug hard. To Get out: CTR+ALT+D
		#app.tk.attributes("-fullscreen", True)
		#app.tk.attributes("-nocursor", True)
		self.app.display()

mirror = SmartMirror()
