
from operator import is_
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
import serial
import time
import cv2
from PIL import Image, ImageTk


#ask for the port number
port = input("Enter the port number: COM")
port = "COM" + port


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


#Layout 
########################################################################################################################
window = Tk()
window.geometry("1157x746")
window.configure(bg = "#FFFFFF")
window.resizable(False, False)
window.title('Dashboard - WRO 2022')

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 746,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)


############################## Button Started ##############################################################

is_on= 1 


def camera_button_click(button, cap):
    global photo1 
    global is_on
    if is_on == 1: 
        photo1 = PhotoImage(file=relative_to_assets("button_1_stop.png"))
        button.configure(image=photo1)
        print("stopping....")  
        #stop the camera
        cap.release()
        is_on = 0                      
        window.update()
    elif is_on == 0:
        photo1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button.configure(image=photo1)
        print("Starting....")   
        is_on = 1
        show_frame()
        window.update()

        #start the camera



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg="#FFFFFF",
    highlightthickness=0,
    #command= lambda: camera_button_click(button_1, cap)
    relief="flat"
)
button_1.place(
    x=353.0,
    y=647.0,
    width=373.0,
    height=87.0
)


############################## Button Stopped ##############################################################

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    101.0,
    373.0,
    image=image_image_1
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    bg="#008DF3",
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=21.0,
    y=311.0,
    width=160.0,
    height=132.0
)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    bg="#008DF3",
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=21.0,
    y=515.0,
    width=160.0,
    height=122.0
)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    bg="#008DF3",
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=21.0,
    y=139.0,
    width=160.0,
    height=126.0
)


canvas.create_text(
    804.0,
    25.0,
    anchor="nw",
    text="Sensors :",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 31 * -1)
)
canvas.create_text(
    271.0,
    26.0,
    anchor="nw",
    text="Camera :",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 31 * -1)
)




Heartbeat_Text = canvas.create_text(
    804.0,
    123.0,
    anchor="nw",
    text="Heartbeat sensor :      " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

AmbientTemperature_Text =  canvas.create_text(
    804.0,
    265.0,
    anchor="nw",
    text="Ambient temperature :    " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

BodyTemperature_Text = canvas.create_text(
    804.0,
    407.0,
    anchor="nw",
    text="Body temperature  :      " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

Gyro_Text = canvas.create_text(
    804.0,
    478.0,
    anchor="nw",
    text="Gyro(xyz axis)  :      " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

Speed_Text = canvas.create_text(
    804.0,
    549.0,
    anchor="nw",
    text="Speed(m/s) :      " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

CO2Rate_Text = canvas.create_text(
    804.0,
    194.0,
    anchor="nw",
    text="CO2 level :      " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

AmbientHumidity_Text = canvas.create_text(
    804.0,
    336.0,
    anchor="nw",
    text="Ambient Humidity :     " + str(0) + "\n",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)


canvas.create_rectangle(
    261.0,
    80.0,
    778.0,
    629.0,
    fill="#0000FF",
    outline="")

########################################################################################################################
# start camera stream and get frame

CamLabel = Label(window, height=549, width=517)
CamLabel.place(x=261.0, y=80.0)


width, height = 450,450  # set the size of the frame
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    CamLabel.imgtk = imgtk
    CamLabel.configure(image=imgtk)
    CamLabel.after(10, show_frame)




########################################################################################################################

ser = serial.Serial(port = port,baudrate=9600)

def do_update():
    
    data = ser.readline()
    data = data.decode("utf-8")
    data = data.split(",")
    print(data)
    if len(data) == 8:
        canvas.itemconfig(Heartbeat_Text, text="Heartbeat sensor :      " + str(data[0]) + "\n")
        canvas.itemconfig(AmbientTemperature_Text, text="Ambient temperature :    " + str(data[1]) + "\n")
        canvas.itemconfig(BodyTemperature_Text, text="Body temperature  :      " + str(data[2]) + "\n")
        canvas.itemconfig(Gyro_Text, text="Gyro(xyz axis)  :      " + str(data[3]) + "\n")
        canvas.itemconfig(Speed_Text, text="Speed(m/s) :      " + str(data[4]) + "\n")
        canvas.itemconfig(CO2Rate_Text, text="CO2 level :      " + str(data[5]) + "\n")
        canvas.itemconfig(AmbientHumidity_Text, text="Ambient Humidity :     " + str(data[6]) + "\n")        
    window.after(1000, do_update)
            

        

do_update()
show_frame()

window.mainloop()