import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import datetime


#VIDEO FRAME
width, height = 900, 500
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



#WINDOW FRAME
root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
root.resizable(False, False)
root.geometry("1417x720")
lmain = tk.Label(root)
lmain.place(x=455, y=120)


bg = PhotoImage(file="banner.png")

bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)

icon = Image.open("icon.jpg")

#resize
resized = icon.resize((450,478), Image.ANTIALIAS)

#call
new_icon = ImageTk.PhotoImage(resized)


icon = ImageTk.PhotoImage(Image.open("icon.jpg"))
icon_label = Label(image=new_icon)
icon_label.place(x=1, y=183)

def snapshot():
    img = Image.fromarray(cv2image)
    time = str(datetime.datetime.now().today()).replace(":"," ")+ ".jpg"
    img.save(time)


def show_frame():
    global cv2image
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(5, show_frame)


Button(text="Time In", command=snapshot, font=('Verdana', 15, 'bold'), width=15, height=1, bg='SpringGreen4').place(x=625, y=670)
Button(text="Time Out", font=('Verdana', 15, 'bold'), width=15, height=1, bg='SpringGreen4').place(x=975, y=670)


show_frame()
root.mainloop()