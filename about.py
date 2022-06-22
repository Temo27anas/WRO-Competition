
from pathlib import Path
from select import select

from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from pygrabber.dshow_graph import FilterGraph
import serial.tools.list_ports

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



window3 = Tk()
window3.geometry("1157x746")
window3.configure(bg = "#FFFFFF")
window3.resizable(False, False)
window3.title('About - WRO 2022')

canvas = Canvas(
    window3,
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
    window3.destroy()
    import gui

def open_settings():
    window3.destroy()
    import settings


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
    command=open_settings,
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
    command=open_dashboard, #open dashboard window
    relief="flat"
)
button_4.place(
    x=21.0,
    y=139.0,
    width=160.0,
    height=126.0
)


canvas.create_text(
    500.0,
    326.0,
    anchor="nw",
    text="About :",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 31 * -1)
)

canvas.create_text(
    500.0,
    326.0 + 50,
    anchor="nw",
    text="Coded by : Anas Temouden - @Temo27anas ",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

canvas.create_text(
    500.0,
    326.0 + 100,
    anchor="nw",
    text="AUI Mechatronics Team - WRO 2022 ",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)

canvas.create_text(
    500.0,
    326.0 + 150,
    anchor="nw",
    text="Copyright © 2022",
    fill="#000000",
    font=("OpenSansRoman SemiBold", 21 * -1)
)
window3.mainloop()