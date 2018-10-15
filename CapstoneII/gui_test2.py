from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

def do_booking():
    info("Booking", "Thank you for Booking")

app = App(title="My Second GUI App", width=300, height=200, layout="grid")
#Dropdown Box
film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion King"], grid=[1,0], align="left")
film_discription = Text(app, text="Which film?", grid=[0,0], align="left")
#Checkbox
vip_seat = CheckBox(app, text="VIP Seat?", grid=[1,1], align="left")
#ButtonGroup
row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"], ["Back", "B"] ], selected="M", horizontal = True, grid=[1,2], align="left")
#Push Button
book_seats = PushButton(app, command=do_booking, text = "Book Seat", grid=[1,3], align="left")

app.display()
