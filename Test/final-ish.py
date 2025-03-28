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

#__________________________WORD LISTS__________________________
ice_cream_list = ["CHOCOLATE FUDGE" , 
                  "CHOCOLATE MARSHMALLOW", 
                  "DEATH BY CHOCOLATE",
                  "CHOCO BROWNIE",
                  "SUNDAE",
                  "TIRAMISU",
                  "CASSATA", 
                  "TENDER COCONUT",
                  "GELATO", 
                  "CORNER HOUSE",
                  "BASKIN ROBBINS", 
                  "NATURALS", 
                  "CORNETTO",
                  "SORBET",
                  "VANILLA",
                  "WAFFLE", 
                  "CARAMEL",
                  "BLACK CURRANT",
                  "CHOCOBAR",
                  "ICE CREAM SANDWICH", 
                  "BUTTERSCOTCH", 
                  "CUSTARD",
                  "BLACK FOREST"]

novels_list = ["HARRY POTTER", 
               "PERCY JACKSON", 
               "ALL THE BRIGHT PLACES", 
               "SHATTER ME", 
               "SHERLOCK HOLMES", 
               "A COURT OF THORNS AND ROSES", 
               "THE SILENT PATIENT", 
               "TUESDAYS WITH MORRIE", 
               "FIVE FEET APART", 
               "WILL NEWMAN", 
               "THE DIARY OF A WIMPY KID", 
               "HERCULE POIROT", 
               "MURDER ON THE ORIENT EXPRESS", 
               "SHADOW AND BONE", 
               "SIX OF CROWS", 
               "THE CRUEL PRINCE", 
               "THE GREAT GATSBY", 
               "LOOKING FOR ALASKA", 
               "TWISTED LOVE", 
               "THE ALCHEMIST", 
               "THE FAULT IN OUR STARS"]

music_list = ["SENORITA",
              "TEETH",
              "ALL LOVE MINE ALL MINE",
              "THEHER JA",
              "COLOR GREEN",
              "MAYBE MY SOULMATE DIED",
              "DANCING WITH YOUR GHOST",
              "NUMB",
              "MASTER OF PUPPETS",
              "GIVE ME SOME SUNSHINE",
              "SHAPE OF YOU",
              "SUNFLOWER",
              "TALKING TO THE MOON",
              "NAATU NAATU",
              "YOUNGBLOOD",
              "NEVER GONNA GIVE YOU UP"]

nostalgia_list = ["CENGAGE", 
                  "HC VERMA", 
                  "JEE ADVANCED", 
                  "KOTA FACTORY", 
                  "SRI CHAITANYA", 
                  "NARAYANA", 
                  "AAKASH", 
                  "ALLEN", 
                  "JEE MAINS", 
                  "JEENEETARDS", 
                  "MESOMERIC EFFECT", 
                  "SEMICONDUCTORS", 
                  "ROTATIONAL MOTION",  
                  "INTEGRATION", 
                  "NATIONAL TESTING AGENCY", 
                  "ONLINE CLASS", 
                  "PHYSICS WALLAH", 
                  "UNACADEMY", 
                  "ZOOM", 
                  "DEPRESSION", 
                  "HOPELESS", 
                  "FAILURE", 
                  "EXPERIMENTAL BATCH", 
                  "MS CHOUHAN", 
                  "INORGANIC CHEMISTRY", 
                  "ORGANIC CHEMISTRY",
                  "TRAUMA", 
                  "REVISION", 
                  "TIME MANAGEMENT", 
                  "SYLLABUS"]

movies_list = ["JAB WE MET",
               "OM SHANTI OM", 
               "CHHICHHORE", 
               "KUCH KUCH HOTA HAI", 
               "MY NAME IS KHAN",
               "TITANIC", 
               "FORREST GUMP",
               "DESPICABLE ME",
               "PIKU",
               "BARFI",
               "ZINDAGI NA MILEGI DOBARA", 
               "DANGAL", 
               "PINK", 
               "TAARE ZAMEEN PAR",
               "JOKER",
               "AVATAR", 
               "MADAGASCAR", 
               "PADMAAVAT",
               "LA LA LAND", 
               "FAST AND FURIOUS",
               "ROCKSTAR",
               "BARBIE",
               "OPPENHEIMER",
               "INTERSTELLAR",
               "LIGHTS OUT",
               "TRAIN TO BUSAN"]

pes_list = ["BUN SAMOSA",
            "SHAWARMA",
            "QUADRANGLE",
            "MRD AUDITORIUM",
            "COW", 
            "HOSPITAL",
            "SKILL ISSUE",
            "JAGS",
            "MAAYA",
            "RIYAL",
            "NAATU NAATU",
            "RETRO DAY",
            "RICK ROLL",
            "FAILURE",
            "EMOTIONAL DAMAGE",
            "PESSIMISTIC",
            "HOPES CRUSHED", 
            "SUPREMEC"]

# #__________________________CLOSE BUTTON__________________________
# def close():
#     def close_game():
#         hangman.destroy()
#     close_button = Button(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, background=BLACK, foreground=BLACK, command=close_game)
#     close_button.place(x=25, y=25)

#__________________________START SCREEN__________________________
def start_screen():  
    global start_button    
    def on_button_click():
        start_button.destroy()
        home_screen()

    #Buttons
    start_button = Button(hangman, image=start_img, borderwidth=0, highlightthickness=0, command=on_button_click)
    start_button.place(x=300, y=325)
    #close()

#__________________________HOME SCREEN__________________________
def home_screen():
    
    def destruction():
        hangman_txt.destroy()
        single_player_button.destroy()
        multiplayer_button.destroy()
        instructions_button.destroy()
        home_txt.destroy()
        back_button.destroy()
        
    def single_player_mode():
        destruction()
        categories_screen()
        
    def multiplayer_mode():
        destruction()
        multiplayer_screen()
    
    def instructions_mode():
        destruction()
        instructions_screen()
        
    #Buttons/Labels
    hangman_txt = Label(hangman, image=hangman_img, background=BLACK)
    hangman_txt.place(x=225, y=40)
    home_txt = Label(hangman, image=home_img, background=BLACK)
    home_txt.place(x=450, y=230)
    single_player_button = Button(hangman, image=single_player_img, background=BLACK, command=single_player_mode)
    single_player_button.place(x=50,y=230)
    multiplayer_button = Button(hangman, image=multiplayer_img, background=BLACK, command=multiplayer_mode)
    multiplayer_button.place(x=50, y=430)
    instructions_button = Button(hangman, image=instructions_img, background=BLACK, command=instructions_mode)
    instructions_button.place(x=50, y=630)
    
    def back_btn():
        destruction()
        start_screen()
    back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    #close()
    
#__________________________CATEGORIES SCREEN__________________________

def categories_screen():
    
    def destruction():
        output_label.destroy()
        back_button.destroy()
        for category_button in category_buttons:
            category_button.destroy()
    
    global chosen_word
    def handle_button_click(category):
        global chosen_word, chosen_category
        chosen_category = category
        chosen_word = random.choice(chosen_category)
        game_screen(chosen_word)
        destruction()
        

    def create_button(category, category_img, x, y):
        def on_button_click():
            handle_button_click(category)
        category_button = Button(hangman, image=category_img, borderwidth=0, highlightthickness=0, highlightcolor=BLACK, command=on_button_click)
        category_button.place(x=x, y=y)
        category_buttons.append(category_button)

    # Create a label
    output_label = Label(hangman, image=categories_header_img, font=("Helvetica", 64), background=BLACK)
    output_label.place(x=240, y=90)

    # Create buttons for different categories

    categories = [ice_cream_list, novels_list, music_list, nostalgia_list, movies_list, pes_list]
    category_imgs = [ice_cream_img, novels_img, music_img, nostalgia_img, movies_img, pes_img]
    button_coordinates = [(80, 300), (570, 300), (80, 450), (570, 450), (80, 600), (570, 600)]
    category_buttons = []
    
    for i in range(len(categories)):
        category = categories[i]
        category_img = category_imgs[i]
        x, y = button_coordinates[i]
        category_button = create_button(category, category_img, x, y)
        
    def back_btn():
        destruction()
        home_screen()
    back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    #close()
    
#__________________________MULTIPLAYER SCREEN__________________________
def multiplayer_screen():
    #chosen_category = []
    def destruction():
        multiplayer_txt.destroy()
        input_box.destroy()
        submit_button.destroy()
        back_button.destroy()
        
    def submit_txt():
        global chosen_word
        def click(event):
            input_box.delete("1.0", END)
            input_box.insert("1.0", " ")
            input_box.tag_configure("center", justify=CENTER)
            input_box.tag_add("center", "1.0", "end")
            
        
        chosen_word = input_box.get("1.0", "end-1c")
        chosen_word = chosen_word.upper()
        chosen_word = chosen_word.strip()
        
        if chosen_word=="":
            input_box.tag_configure("center", justify=CENTER)
            input_box.insert("1.0", "Try Again")
            input_box.tag_add("center", "1.0", "end")
            input_box.bind('<Button-1>', click)
            
        elif any(ord(i) not in range(65, 91) and ord(i) != 32 for i in chosen_word):
                input_box.delete("1.0", END)
                input_box.insert("1.0", " ")
                input_box.tag_configure("center", justify=CENTER)
                input_box.insert("1.0", f"Please enter \n letters only")
                input_box.tag_add("center", "1.0", "end")
                input_box.bind('<Button-1>', click)

        else:
            destruction()
            game_screen(chosen_word)
    
    multiplayer_txt = Label(hangman, image=multiplayer_header_img, background=BLACK, highlightthickness=0, borderwidth=0)
    multiplayer_txt.place(x=250, y=40)
    input_box = Text(hangman, font=("Helvatica", 96), width=12, height=2)
    input_box.tag_configure("center", justify=CENTER)
    input_box.insert("1.0", " ")
    input_box.tag_add("center", "1.0", "end")
    input_box.place(x=135, y=255)
    submit_button = Button(hangman, image=submit_img, background=BLACK, highlightthickness=0, border=0, command=submit_txt)
    submit_button.place(x=325, y=600)
    
    def back_btn():
        destruction()
        home_screen()
    back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    
#__________________________INSTRUCTIONS SCREEN__________________________
def instructions_screen():
    
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
    
    back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    
    
#__________________________GAME SCREEN__________________________
def game_screen(chosen_word):
    
    #Destroying all buttons for back
    def destruction():
        for dash in dashes:
            dash.destroy()
        for key in keyboard_list:
            key.destroy()
        for replaced_dash in replaced_dashes:
            replaced_dash.destroy()
        lives_img.destroy()
        back_button.destroy()
        
    def disable():
        for key in keyboard_list:
            key.config(state=DISABLED, bg=GREEN)
    
    def back_btn():
        destruction()
        if chosen_word in chosen_category:
            categories_screen()
        else:
            multiplayer_screen()
     
    #Lists for future refrence  
    keyboard_list = []     
    chosen_letter_list = []
    right_chosen_letters = []
    wrong_chosen_letters = []
    chosen_word_letters = []
    chosen_word_letters_backup = []
    replaced_dashes = []
    dashes=[]
    
    #Checking
    print(chosen_word)
    
    #Used in future
    for i in chosen_word:
        chosen_word_letters.append(i)
        if i != " ":
            if i not in chosen_word_letters_backup:
                chosen_word_letters_backup.append(i)
    print(chosen_word_letters)
    
    #Creating Dashes for the game  
    x = 75
    y = 150

    for i in chosen_word:
        if i != " ":
            dash = Label(hangman, image=dash_img, borderwidth=0, highlightthickness=0)
            dash.place(x=x,y=y)
            dashes.append(dash)
            replaced_dash = Label(hangman, text="", font=("Helvatica", 45), borderwidth=0, highlightthickness=0, bg=BLACK, fg=GREEN)
            replaced_dash.place(x=x-10, y=y-25, width=50, height=50)
            replaced_dashes.append(replaced_dash)
            x += 45
            
        else:
            x = 75
            y += 55
    
    #Making keyboard and setting it up
    def create_button(letter, x, y):
        def letter_click():
            global chosen_letter
            Letter_button.config(state=DISABLED, bg=GREEN, fg=BLACK)
            chosen_letter = Letter_button.cget("text")
            chosen_letter_list.append(chosen_letter)
            print(chosen_letter_list)
            replace()

        Letter_button = ttwidgets.TTButton(hangman, text=letter, font=("Helvetica", 80), bg=BLACK, fg=GREEN, command=letter_click)
        Letter_button.place(x=x, y=y, height=100, width=width_two)
        return Letter_button

    button_positions = [(65, 75, 50, 90, 490, 90), (75, 83, 105, 100, 595, 100), (83, 91, 135, 90, 700, 90)]

    for start, end, x_pos, x_add, y_pos, width_two in button_positions:
        for i in range(start, end):
            Letter_button = create_button(chr(i), x_pos, y_pos)
            keyboard_list.append(Letter_button)
            x_pos += x_add
     
    #Editing guessed words
    def replace():
        for i in range(chosen_word_letters.count(" ")):
            chosen_word_letters.remove(" ")
        
        wrong = 0
        for i in chosen_letter_list:
            if i in chosen_word_letters:
                if chosen_word_letters.count(i) == 1:
                    replaced_dashes[chosen_word_letters.index(i)].config(text=i)
                else:
                    for j in range(chosen_word_letters.count(i)):
                        replaced_dashes[chosen_word_letters.index(i)].config(text=i)
                        chosen_word_letters[chosen_word_letters.index(i)] = "0"
            elif i not in chosen_word_letters_backup:
                wrong +=1
                lives_img.config(image=lives[wrong])
                wrong_chosen_letters.append(i)
                
            
        #Going to the next screen
        if wrong == 5:
            go_to_lose_screen()
        
        suar = 0
        for i in chosen_word_letters_backup:
            if i in chosen_letter_list:
                suar+=1
        if suar == len(chosen_word_letters_backup):
            go_to_win_screen()

                
    print(chosen_word_letters_backup)
    def go_to_lose_screen():
        disable()
        hangman.after(1000, destruction)
        hangman.after(1000, loser_screen)
    
    def go_to_win_screen():
        disable()
        hangman.after(1000, destruction)
        hangman.after(1000, winner_screen)
       
    lives_img = Label(hangman, image=zero_img, borderwidth=0, highlightthickness=0, background=BLACK)
    lives_img.place(x=600, y=50)
    
    #Setting up images for wrong thingy
    lives = [zero_img, one_img, two_img, three_img, four_img, five_img]
    
    back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)

#__________________________LOSER SCREEN__________________________
# def loser_screen():
#     def destruction():
#         you_lost_title.destroy()
#         back_button.destroy()
        
#     def back_btn():
#         destruction()
#         home_screen()
        
#     back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
#     back_button.place(x=25, y=25) 

#     you_lost_title = Label(hangman, image=you_lost_header, borderwidth=0, highlightthickness=0)
#     you_lost_title.place(x=255, y=40)
    


# #__________________________WINNER SCREEN__________________________
# def winner_screen():
#     def destruction():
#         you_win_title.destroy()
#         back_button.destroy()
        
#     def back_btn():
#         destruction()
#         home_screen()
    
#     you_win_title = Label(hangman, image=you_win_header, borderwidth=0, highlightthickness=0)
#     you_win_title.place(x=255, y=40)
    
#     back_button = ttwidgets.TTButton(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
#     back_button.place(x=25, y=25)

#______________________________WIN SCREEN_______________________________________
def winner_screen():
    def destruction():
        you_win_label.destroy()
        word_answer.destroy()
        answer.destroy()
        playagain.destroy()

    def play_again():
        destruction()
        home_screen()

    def close():
        hangman.destroy()
    
    you_win_label=Label(hangman,image=you_win_header, highlightthickness=0, borderwidth=0)
    you_win_label.place(x=255,y=40)
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    word_answer.place(x=50,y=320)
    answer=Label(hangman,text=chosen_word,bg=BLACK,fg=GREEN,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    answer.place(x=50,y=425)
    playagain=Button(hangman,image= play_again_img, highlightthickness=0, borderwidth=0, command=play_again)  #add command=play_again
    playagain.place(x=50,y=525)

    
    close_button = ttwidgets.TTButton(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, background=BLACK, foreground=BLACK, command=close)
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
        home_screen()
    you_lose_label=Label(hangman,image=you_lost_header, highlightthickness=0, borderwidth=0)
    you_lose_label.place(x=255,y=40)
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    word_answer.place(x=50,y=320)
    playagain=Button(hangman, image=play_again_img, highlightthickness=0, borderwidth=0, command=play_again)  #add command=play_again
    playagain.place(x=50,y=525)
    answer=Label(hangman,text=chosen_word,bg=BLACK,fg=GREEN,font=("Helvetica",35),highlightthickness=0,borderwidth=0)
    answer.place(x=50,y=425)
    
    
    close_button = ttwidgets.TTButton(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, background=BLACK, foreground=BLACK, command=close)
    close_button.place(x=25, y=25)

start_screen()

hangman.mainloop()