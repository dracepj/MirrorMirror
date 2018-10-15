from guizero import App, Text, Picture, Box
import datetime
import calendar
#import tkinter


def update():
    now = datetime.datetime.now()
    display_clock.set(now.strftime("%I:%M %p"))
    display_date.set(now.strftime("%a, %b-%d, %Y"))
    

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

year = int(now.strftime("%Y"))
month = int(now.strftime("%-m"))
box = Box(app, grid=[0,3], align="left")
display_calendar = Text(box, text = cal.formatmonth(year,month), color="white")


app.repeat(1000,update)

#sets full screen-Makes debug hard. To Get out: CTR+ALT+D
#app.tk.attributes("-fullscreen", True)
#app.tk.attributes("-nocursor", True)
app.display()

