import os
from tkinter import Button, PhotoImage
from home_screen import home_screen

BLACK = "#1C1C1E"

def start_screen(root):
    start_img = PhotoImage(file=f"{os.getcwd()}/Images/Start.png")

    def on_button_click():
        start_button.destroy()
        home_screen(root)

    start_button = Button(root, image=start_img, borderwidth=0, highlightthickness=0, command=on_button_click)
    start_button.place(x=300, y=325)

start_img = PhotoImage(file=f"{os.getcwd()}/Images/Start.png")