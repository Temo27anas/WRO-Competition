from pathlib import Path
from select import select

from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from pygrabber.dshow_graph import FilterGraph
import serial.tools.list_ports

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


global selectedCAM

window2 = Tk()
window2.geometry("1157x746")
window2.configure(bg = "#FFFFFF")
window2.resizable(False, False)
window2.title('Settings - WRO 2022')

canvas = Canvas(
    window2,
    bg = "#FFFFFF",
    height = 746,
    width = 1157,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

#Function to distoroy current window and open new window in another file
def open_dashboard():
    window2.destroy()
    import gui

def open_about():
    window2.destroy()
    import about

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
    command=open_about,
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
    command=open_dashboard, #open dashboard window
    relief="flat"
)
button_4.place(
    x=21.0,
    y=139.0,
    width=160.0,
    height=126.0
)



graph = FilterGraph()

listCamera = graph.get_input_devices()# list of camera device 

def camindex(i):

    if i == 0:
        return "Default camera"
    elif i == -1:
        return "No camera"
    else:
        return "Camera " + str(i)

def selectcam(i):
    if i == 0:
        return "  Selected ✅"


canvas.create_text(
    271.0,
    26.0,
    anchor="nw",
    text="Camera Devices Available :",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 31 * -1)
)

for i in range(len(listCamera)):
    canvas.create_text(
        271.0,
        56.0 + (i+1) * 25,
        anchor="nw",
        text= camindex(i) + " - "+ listCamera[i] + selectcam(i) ,
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )


canvas.create_text(
    271.0,
    26.0 + 300,
    anchor="nw",
    text="COM Ports:",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 31 * -1)
)



#----------------------------------------------------------------------------------------------------------------------

 

comList = serial.tools.list_ports.comports()

labelselectedlist = []


def selectCOM(i):
    global selectedCOM     
    selectedCOM = comList[i].device[3]
    print("Selected COM : " + str(selectedCOM))
    # update COM port label
    canvas.itemconfig(labelselectedlist[i], text="Selected ✅")
    


for i in range(len(comList)):
    canvas.create_text(
        271.0,
        56.0 + (i+1) * 25 + 300,
        anchor="nw",
        text=  comList[i].device + " - " + comList[i].description,
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    )
    #create select buttons for  each COM port
    button = Button(
        text="Select",
        borderwidth=0,
        highlightthickness=0,
        command= lambda i=i: selectCOM(i),  
        relief="flat",
        bg="#4CAF50"
    )
    button.place(
        x=671.0,
        y=56.0 + (i+1) * 25 + 300,
        width=100.0,
        height=22.0)


    labelselected = canvas.create_text(
        671.0 + 130,
        56.0 + (i+1) * 25 + 300,
        anchor="nw",
        text=  "",
        fill="#000000",
        font=("OpenSansRoman SemiBold", 21 * -1)
    
    )

    labelselectedlist.append(labelselected)    
    





window2.mainloop()