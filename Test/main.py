import tkinter as tk
from start_screen import start_screen

#__________________________CONSTANTS__________________________
BLACK = "#1C1C1E"
PLATINUM = "#E3E3E1"
BROWN = "#4E4544"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

hangman = tk.Tk()
#Width first Height 2nd
hangman.geometry("1000x800")
hangman["background"]=BLACK
hangman.title("Hangman")

start_screen(hangman)

hangman.mainloop()