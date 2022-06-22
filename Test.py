
# import the opencv library
import cv2
from tkinter import Label, Tk, Canvas, Entry, Text, Button, PhotoImage
from pathlib import Path
import cv2
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

  
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

CamLabel = Label(window, height=549, width=517)
CamLabel.place(x=261.0, y=80.0)



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg="#FFFFFF",
    highlightthickness=0,
    command= lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=353.0,
    y=647.0,
    width=373.0,
    height=87.0
)



width, height = 450,450  # set the size of the frame
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def show_frame():
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    CamLabel.imgtk = imgtk
    CamLabel.configure(image=imgtk)
    CamLabel.after(10, show_frame)

def show_frame():
    vid = cv2.VideoCapture(0)
    
    while(True):
        

        ret, frame = vid.read()
        CamLabel.configure(image=frame)
        CamLabel.after(10, show_frame)
        #cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#vid = cv2.VideoCapture(0)
  
# while(True):
      

#     ret, frame = vid.read()
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# vid.release()
# cv2.destroyAllWindows()

show_frame()
window.mainloop()