import os
import tkinter as tk
from tkinter import Label, Button, PhotoImage
from home_screen import *
from game_screen import *

def multiplayer_screen(hangman):
    global chosen_word, chosen_category
    chosen_category = []
    def destruction():
        multiplayer_txt.destroy()
        input_box.destroy()
        submit_button.destroy()
        back_button.destroy()
        
    def submit_txt():

        def click(event):
            input_box.delete("1.0", "END")
            input_box.tag_configure("center", justify="CENTER")
            input_box.insert("1.0", " ")
            input_box.tag_add("center", "1.0", "end")
            
        
        chosen_word = input_box.get("1.0", "end-1c")
        chosen_word = chosen_word.upper()
        chosen_word = chosen_word.strip()
        if chosen_word=="":
            input_box.tag_configure("center", justify="CENTER")
            input_box.insert("1.0", "Try Again")
            input_box.tag_add("center", "1.0", "end")
            input_box.bind('<Button-1>', click)

        else:
            destruction()
            game_screen(chosen_word)
    
    multiplayer_txt = Label(hangman, image=multiplayer_header_img, background=BLACK, highlightthickness=0, borderwidth=0)
    multiplayer_txt.place(x=250, y=40)
    input_box = tk.Text(hangman, font=("Helvatica", 96), width=12, height=2)
    input_box.tag_configure("center", justify="CENTER")
    input_box.insert("1.0", " ")
    input_box.tag_add("center", "1.0", "end")
    input_box.place(x=135, y=255)
    submit_button = Button(hangman, image=submit_img, background=BLACK, highlightthickness=0, border=0, command=submit_txt)
    submit_button.place(x=325, y=600)
    
    def back_btn():
        destruction()
        home_screen()
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0)
    back_button.place(x=25, y=25)
    
multiplayer_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Multiplayer_Header.png")
submit_img = PhotoImage(file=f"{os.getcwd()}/Images/Submit.png")
back_img = PhotoImage(file=f"{os.getcwd()}/Images/Back.png")