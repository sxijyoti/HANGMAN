import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from string import ascii_uppercase
import random

hangman=tk.Tk()
#hangman.geometry("756x461")
#hangman.resizable(width=0,height=0)
#hangman["background"]="BLACK"

word_list=["hello world","python","curse"]

#GameScreen_Hangman
hangman_photo=[PhotoImage(file=f"{os.getcwd()}/tempp/1.png"),PhotoImage(file=f"{os.getcwd()}/tempp/2.png"),PhotoImage(file=f"{os.getcwd()}/tempp/3.png"),PhotoImage(file=f"{os.getcwd()}/tempp/4.png"),PhotoImage(file=f"{os.getcwd()}/tempp/5.png")]

word_with_space=""
no_of_guess=0
def newgame():
    global word_with_space
    global no_of_guess
    no_of_guess=0
    imglabel.config(image=hangman_photo[0])
    chosen_word=random.choice(word_list)
    word_with_space=" ".join(chosen_word)
    lblword.set(" ".join("_"*len(chosen_word)))

imglabel=Label(hangman)
imglabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
imglabel.config(image=hangman_photo[0])

lblword=StringVar()
Label(hangman,textvariable=lblword,font=("calibri","24")).grid(row=0,column=3,columnspan=6,padx=10)

def guess(letter):
    global no_of_guess
    txt=list(word_with_space)
    guessed=list(lblword.get())
    if word_with_space.count(letter)>0:
        for c in range(len(txt)):
            if txt(c)==letter:
                guessed[c]==letter
            lblword.set("".join(guessed))
    else:
        no_of_guess+=1
        imglabel.config(image=hangman_photo[no_of_guess])


n=0
for c in ascii_uppercase:
    Button(hangman,text=c,command=lambda c=c: guess(c),font=("calibri","18"),width=3).grid(row=1+n//9,column=n%9)
    n+=1



hangman.mainloop()
