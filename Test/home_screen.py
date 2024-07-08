import tkinter as tk
import ttwidgets
from tkinter import Tk, END, CENTER, Text, PhotoImage, Label, Button, messagebox, DISABLED
import os
import random

#__________________________CONSTANTS__________________________
BLACK = "#1C1C1E"
PLATINUM = "#E3E3E1"
BROWN = "#4E4544"
GREEN = "#308C73"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

hangman = Tk()
#Width first Height 2nd
hangman.geometry("1000x800")
hangman["background"]=BLACK
hangman.title("Hangman")

#__________________________IMAGES__________________________
#Start Screen
start_img = PhotoImage(file=f"{os.getcwd()}/Images/Start.png")

#Home Screen
hangman_img = PhotoImage(file=f"{os.getcwd()}/Images/Hangman.png")
home_img = PhotoImage(file=f"{os.getcwd()}/Images/Home_Screen.png")
single_player_img = PhotoImage(file=f"{os.getcwd()}/Images/Single_Player.png")
multiplayer_img = PhotoImage(file=f"{os.getcwd()}/Images/Multiplayer.png")
single_player_img = PhotoImage(file=f"{os.getcwd()}/Images/Single_Player.png")
instructions_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions.png")

#Categories
categories_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Categories.png")
ice_cream_img = PhotoImage(file=f"{os.getcwd()}/Images/Ice_Cream.png")
movies_img = PhotoImage(file=f"{os.getcwd()}/Images/Movies.png")
music_img = PhotoImage(file=f"{os.getcwd()}/Images/Music.png")
nostalgia_img = PhotoImage(file=f"{os.getcwd()}/Images/Nostalgia.png")
novels_img = PhotoImage(file=f"{os.getcwd()}/Images/Novels.png")
pes_img = PhotoImage(file=f"{os.getcwd()}/Images/PES.png")

#Multiplayer Screen
multiplayer_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Multiplayer_Header.png")
submit_img = PhotoImage(file=f"{os.getcwd()}/Images/Submit.png")

#Instructions Screen
instructions_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions_Header.png")
instructions_rules_img = PhotoImage(file=f"{os.getcwd()}/Images/Instructions_rules.png")

#Game Screen
dash_img = PhotoImage(file=f"{os.getcwd()}/Images/dash.png")
zero_img = PhotoImage(file=f"{os.getcwd()}/Images/Zero_Life.png")
one_img = PhotoImage(file=f"{os.getcwd()}/Images/One_Life.png")
two_img = PhotoImage(file=f"{os.getcwd()}/Images/Two_Life.png")
three_img = PhotoImage(file=f"{os.getcwd()}/Images/Three_Life.png")
four_img = PhotoImage(file=f"{os.getcwd()}/Images/Four_Life.png")
five_img = PhotoImage(file=f"{os.getcwd()}/Images/Five_Life.png")

#Win/Lose Screen
you_win_header = PhotoImage(file=f"{os.getcwd()}/Images/You_Won.png")
you_lost_header = PhotoImage(file=f"{os.getcwd()}/Images/You_Lost.png")
you_lost_img = PhotoImage(file=f"{os.getcwd()}/Images/you_lose.png")
you_win_img = PhotoImage(file=f"{os.getcwd()}/Images/you_win.png")
play_again_img = PhotoImage(file=f"{os.getcwd()}/Images/Play_Again.png")

#Extra
close_img = PhotoImage(file=f"{os.getcwd()}/Images/Close.png")
back_img = PhotoImage(file=f"{os.getcwd()}/Images/Back.png")

chosen_word = "Loudu"
def winner_screen():
    def destruction():
        you_win_label.destroy()
        word_answer.destroy()
        answer.destroy()
        playagain.destroy()

    def play_again():
        destruction()

    def close():
        hangman.destroy()

    you_win_label=Label(hangman,image=you_win_header, highlightthickness=0, borderwidth=0)
    you_win_label.place(x=255,y=40)
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    word_answer.place(x=50,y=320)
    answer=Label(hangman,text=chosen_word,bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    answer.place(x=50,y=475)
    playagain=Button(hangman, image=play_again_img, highlightthickness=0, borderwidth=0, command=play_again)  #add command=play_again
    playagain.place(x=50,y=525)

    
    close_button = Button(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, command=close)
    close_button.place(x=25, y=25)

#______________________________LOSE SCREEN_______________________________________
def loser_screen():

    def destruction():
        you_lose_label.destroy()
        word_answer.destroy()
        answer.destroy()
        playagain.destroy()
        
    def close():
        hangman.destroy()
        
    def play_again():
        destruction()
    you_lose_label=Label(hangman,image=you_lost_header, highlightthickness=0, borderwidth=0)
    you_lose_label.place(x=255,y=40)
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    word_answer.place(x=50,y=320)
    answer=Label(hangman,text=chosen_word,bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    answer.place(x=50,y=475)
    playagain=Button(hangman,text="Play Again",bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0,command=play_again)  #add command=play_again
    playagain.place(x=50,y=525)
    
    
    close_button = Button(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, command=close)
    close_button.place(x=25, y=25)
    
winner_screen()

hangman.mainloop()