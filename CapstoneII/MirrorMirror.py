from guizero import App, Text, Picture, Box
import datetime
import calendar
import asyncio
import socket
#from msg_parser import MessageParser
from filelock import Timeout, FileLock
#import tkinter
settings_file = "./conf/settings.json"
#def setup_msg():
#	msg_recv = MessageParser()
#	msg_recv.start_listening()

def run_gui():
	
	def check_settings():
		lock = FileLock(settings_file + ".lock", timeout=2)
		s_data = None
		try:
			with lock:
				settings_data_fhandle = open(settings_file)
				s_data = settings_data_fhandle.read()
				print(s_data)
		except Timeout:
			print("Failed to acquire file lock")
		finally:
			lock.release()
		
	def update():
		now = datetime.datetime.now()
		display_clock.set(now.strftime("%I:%M %p"))
		display_date.set(now.strftime("%a, %b-%d, %Y"))
	
	def get_local_ip():
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
		print("%s " % s.getsockname()[0])
		return "Please connect to: %s " % s.getsockname()[0]
	
	app = App(title="Mirror Mirror", width=1500, height=800, layout="grid", bg="black")

	now = datetime.datetime.now()
	cal = calendar.TextCalendar(calendar.SUNDAY)

	if(now.strftime("%h") < "12"):
	    display_greeting = Text(app, text = "Good Morning,",grid=[0,0], color="white", size="30")
	elif(now.strftime("%h") >= "12" and now.strftime("%h") < "19"):
	    display_greeting = Text(app, text = "Good Afternoon",grid=[0,0], color="white", size="30")
	elif(now.strftime("%h") >= "19"):
	    display_greeting = Text(app, text = "Good Evening",grid=[0,0], color="white", size="30")

	display_clock = Text(app, text = now.strftime("%I:%M %p"),grid=[0,1], color="white", size="30")
	display_date = Text(app, text = now.strftime("%a, %b-%d, %Y"), grid=[0,2], color="white", size="20")
	display_ip = Text(app, text = get_local_ip(), grid=[0,6], color="white", size="12")

	year = int(now.strftime("%Y"))
	month = int(now.strftime("%-m"))
	box = Box(app, grid=[0,3], align="left")
	display_calendar = Text(box, text = cal.formatmonth(year,month), color="white")


	app.repeat(1000,update)
	app.repeat(2000, check_settings)

	#sets full screen-Makes debug hard. To Get out: CTR+ALT+D
	#app.tk.attributes("-fullscreen", True)
	#app.tk.attributes("-nocursor", True)
	app.display()

event_loop = asyncio.get_event_loop()
try:
	run_gui()
	#asyncio.run_coroutine_threadsafe(setup_msg(), event_loop)
except KeyboardInterrupt:
	event_loop.close()

