import os
from tkinter import Button, Label, PhotoImage
from home_screen import home_screen
from categories_screen import categories_screen
from multiplayer_screen import multiplayer_screen

BLACK = "#1C1C1E"

def instructions_screen(hangman):
    
    def destruction():
        instructions_txt.destroy()
        instructions_rules_txt.destroy()
        single_player_button.destroy()
        multiplayer_button.destroy()
        back_button.destroy()
    
    def single_player_mode():
        destruction()
        categories_screen()
        
    def multiplayer_mode():
        destruction()
        multiplayer_screen()
    
    instructions_txt = Label(hangman, image=instructions_header_img, background=BLACK)
    instructions_txt.place(x=255, y=40)
    instructions_rules_txt = Label(hangman, image=instructions_rules_img, background=BLACK)
    instructions_rules_txt.place(x=50, y=230)
    single_player_button = Button(hangman, image=single_player_img, background=BLACK, command=single_player_mode)
    single_player_button.place(x=600,y=340)
    multiplayer_button = Button(hangman, image=multiplayer_img, background=BLACK, command=multiplayer_mode)
    multiplayer_button.place(x=600, y=520)
    
    def back_btn():
        destruction()
        home_screen()
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0)
    back_button.place(x=25, y=25)

single_player_img = PhotoImage(file=f"{os.getcwd()}/Images/Single_Player.png")
multiplayer_img = PhotoImage(file=f"{os.getcwd()}/Images/Multiplayer.png")
instructions_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions_Header.png")
instructions_rules_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions_rules.png")
back_img = PhotoImage(file=f"{os.getcwd()}/Images/Back.png")