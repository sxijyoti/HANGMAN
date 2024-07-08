import tkinter as tk
from tkinter import messagebox

# Constants
BLACK = "#1C1C1E"
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

def show_second_screen():
    # Hide elements from the first screen
    start_button.pack_forget()

    # Show elements for the second screen
    output_label.pack()
    for button in category_buttons:
        button.pack()

def handle_button_click(category):
    output_label.config(text=f"Selected category: {category}")
    print(category)

# First screen
hangman = tk.Tk()
hangman.geometry("1000x800")
hangman["background"] = BLACK
hangman.title("Hangman")

start_img = tk.PhotoImage(file="Start.png")

def Start():
    show_second_screen()

start_button = tk.Button(hangman, image=start_img, borderwidth=0, highlightthickness=0, command=Start)
start_button.pack(pady=50)

# Second screen elements
output_label = tk.Label(hangman, text="Select a category", font=("Helvetica", 30))

categories = ["Ice_Creams", "Bollywood_Movies", "Songs", "PES", "Nostalgia", "Novels"]
category_buttons = []

for category in categories:
    button = tk.Button(hangman, text=category, command=lambda c=category: handle_button_click(c),
                       width=20, height=3, font=("Helvetica", 14))
    category_buttons.append(button)

# Keep the second screen elements initially hidden
output_label.pack_forget()
for button in category_buttons:
    button.pack_forget()

hangman.mainloop()
