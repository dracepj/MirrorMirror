from guizero import App, Text, TextBox,PushButton, Slider, Picture

#used for pushbutton
def say_my_name():
    welcome_message.value = my_name.value
#used for slider
def change_text_size(slider_value):
    welcome_message.size = slider_value

#Title in Top Bar
app = App(title="Mirror Mirror")
#Text inside of frame
welcome_message = Text(app,text="Welcome to my App", size=40, font="Times New Roman", color="lightblue")
#TextBox
my_name = TextBox(app)
#PushButton Widget- updates takes the value from the Text Box
update_text = PushButton(app, command=say_my_name, text="Display my name")
#Slider Widget
text_size = Slider(app, command=change_text_size, start=10, end=80)
#Picture
my_pic = Picture(app, image="GIFS.gif")
#Displays the Window
app.display()
