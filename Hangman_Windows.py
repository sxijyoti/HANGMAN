import tkinter as tk
import pygame
from tkinter import Tk, END, CENTER, Text, PhotoImage, Label, Button, messagebox, DISABLED
import os
import random
from tkvideo import *

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
hangman.resizable(width=0, height=0)

#__________________________IMAGES__________________________
#Start Screen
start_img = PhotoImage(file=f"{os.getcwd()}/Images/Start.png")

#Home Screen
hangman_img = PhotoImage(file=f"{os.getcwd()}/Images/Hangman.png")
home_img = PhotoImage(file=f"{os.getcwd()}/Images/Hangman_Screen.png")
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

#__________________________SOUNDS__________________________
pygame.mixer.init()
win_soundtrack=f"{os.getcwd()}/Sound/golf_clap.wav"
lose_sountrack=f"{os.getcwd()}/Sound/super_mario_bros.wav"
rickroll_soundtrack=f"{os.getcwd()}/Sound/rick_roll.wav"

#__________________________VIDEOS__________________________
win_video=f"{os.getcwd()}/Videos/you_win_animation.mp4"
lose_video=f"{os.getcwd()}/Videos/you_lose_animation.mp4"
rickroll_video=f"{os.getcwd()}/Videos/rick_roll.mp4"

def play_win():
    pygame.mixer.music.load(win_soundtrack)
    pygame.mixer.music.play(loops=2)

def play_lose():
    pygame.mixer.music.load(lose_sountrack)
    pygame.mixer.music.play(loops=1)

#__________________________WORD LISTS__________________________
ice_cream_list = ["VANILLA", "CHOCOLATE", "STRAWBERRY", "MINT CHOCOLATE CHIP", "COOKIES AND CREAM", "ROCKY ROAD", "BUTTER PECAN", "COOKIE DOUGH", "PISTACHIO", "NEAPOLITAN", "COFFEE", "MANGO", "BLACK CHERRY", "CARAMEL SWIRL", "PEANUT BUTTER CUP", "TOFFEE CRUNCH", "DOUBLE CHOCOLATE FUDGE", "MAPLE WALNUT", "RUM RAISIN", "COCONUT", "HAZELNUT", "CHERRY GARCIA", "PRALINES AND CREAM", "BANANA SPLIT", "LEMON SORBET", "BLUEBERRY CHEESECAKE", "KEY LIME PIE", "RED VELVET", "SALTED CARAMEL", "WHITE CHOCOLATE"]

novels_list = ["HOUSE OF EARTH AND BLOOD", "VERITY", "BEFORE I FALL", "LOOKING FOR ALASKA", "RED QUEEN", "THE LOVE HYPOTHESIS", "TWISTED LOVE", "THE SANATORIUM", "PERCY JACKSON", "HARRY POTTER", "THE BROMANCE BOOK CLUB", "RED, WHITE AND ROYAL BLUE", "A COURT OF THORNS AND ROSES", "THE PUSH", "ALL THE BRIGHT PLACES", "THE FLATSHARE", "SHADOW AND BONE", "TUESDAYS WITH MORRIE", "THE CRUEL PRINCE", "THE GUEST LIST", "LEGENDBORN", "THE GILDED WOLVES", "THE DATING PLAYBOOK", "THE POPPY WAR", "BLACK SUN", "THEY BOTH DIE AT THE END", "PEOPLE WE MEET ON VACATION", "BEACH READ", "THE DIARY OF A WIMPY KID", "THRONE OF GLASS", "SHERLOCK HOLMES", "THE SILENT PATIENT", "THE BONE SEASON", "THE INHERITANCE GAMES", "CARAVAL", "THE HATE U GIVE", "GONE GIRL", "HERCULE POIROT", "MURDER ON THE ORIENT EXPRESS", "MALICE", "THE NIGHT SWIM", "SHATTER ME", "THE SEARCHER", "AURORA RISING", "IT HAPPENED ONE SUMMER", "THE MASK FALLING", "THE REVERSAL", "THE ALCHEMIST", "ONE OF US IS LYING", "CEMETERY BOYS", "FIVE FEET APART", "WILL NEWMAN", "THE FAULT IN OUR STARS", "THE SPANISH LOVE DECEPTION", "THE HATING GAME", "THE GREAT GATSBY", "SIX OF CROWS"]

music_list = ["SHAPE OF YOU", "DESPACITO", "TUM HI HO", "SENORITA", "LEAN ON", "MALHARI", "HAVANA", "WAKA WAKA", "JEENE LAGA HOON", "BELIEVER", "TERA BAN JAUNGA", "PERFECT", "INKEM INKEM INKEM KAAVALE", "CHEAP THRILLS", "BEKHAYALI", "MY HEART WILL GO ON", "FADED", "COUNTING STARS", "DANCE MONKEY", "SAY YOU WONT LET GO", "KAUN TUJHE", "UPTOWN FUNK", "BUTTERFLY", "ATTENTION", "SAY SOMETHING", "CANT STOP THE FEELING", "SHAPE OF YOU", "SORRY", "ROAR", "COUNTING STARS", "HAPPIER", "BLINDING LIGHTS", "WATERMELON SUGAR", "DYNAMITE", "SAVAGE LOVE", "GOOD FOR U", "LEAVE THE DOOR OPEN", "KISS ME MORE", "SAVE YOUR TEARS", "MONTERO", "PEACHES", "LEVITATING", "DEJA VU", "UP", "MOOD", "POKER FACE", "SHUT UP AND DANCE", "CANT FEEL MY FACE", "BAD ROMANCE", "NEVER GONNA GIVE YOU UP"]

nostalgia_list = ["LOCKDOWN", "NATIONAL TESTING AGENCY", "REVISION", "MACERENA", "MASK", "CRUSH", "FAILURE", "SOCIAL DISTANCING", "PHYSICS WALLAH", "INTEGRATION", "SRI CHAITANYA", "PTM", "CENGAGE", "JEE ADVANCED", "TRAUMA", "HC VERMA", "ONLINE CLASS", "COVID", "ZOOM", "MS CHOUHAN", "IIT JEE", "INORGANIC CHEMISTRY", "ORGANIC CHEMISTRY", "QUARANTINE", "JEENEETARDS", "ROTATIONAL MOTION", "SPORTS DAY", "UNACADEMY", "TIME MANAGEMENT", "EXPERIMENTAL BATCH", "SYLLABUS", "PEN FIGHT", "SEMICONDUCTORS", "JEE MAINS", "ALLEN", "NARAYANA", "HOPELESS", "AAKASH", "BOOK FAIR", "MESOMERIC EFFECT", "DEPRESSION", "KOTA FACTORY"]

movies_list = ["SHERSHAAH", "RAIDERS OF THE LOST ARK", "ROCKSTAR", "IT", "STAR WARS", "QUEEN", "CITY LIGHTS", "THE SHAPE OF WATER", "KUCH KUCH HOTA HAI", "JOKER", "FAST AND FURIOUS", "THE SOUND OF MUSIC", "PINK", "DILWALE DULHANIA LE JAYENGE", "PADMAAVAT", "DESPICABLE ME", "BARBIE", "KABHI KHUSHI KABHIE GHAM", "MADAGASCAR", "THE GODFATHER", "SHOLAY", "INCEPTION", "DEVDAS", "THE DARK KNIGHT", "OPPENHEIMER", "TITANIC", "FORREST GUMP", "CHHICHHORE", "TAARE ZAMEEN PAR", "PK", "THE LION KING", "ZINDAGI NA MILEGI DOBARA", "LAGAAN", "LA LA LAND", "CASABLANCA", "THE SILENCE OF THE LAMBS", "JAB WE MET", "SLUMDOG MILLIONAIRE", "FIGHT CLUB", "BHAAG MILKHA BHAAG", "THE LORD OF THE RINGS", "OM SHANTI OM", "DANGAL", "MOTHER INDIA", "JURASSIC PARK", "AVATAR", "DIL CHAHTA HAI", "GONE WITH THE WIND", "PULP FICTION", "THE AVENGERS", "THE MATRIX", "LIGHTS OUT", "TRAIN TO BUSAN", "BARFI", "JAWS", "GLADIATOR", "INTERSTELLAR", "CITIZEN KANE"]

pes_list = ["BUN SAMOSA", "SHAWARMA", "QUADRANGLE", "MRD AUDITORIUM", "COW", "HOSPITAL", "SKILL ISSUE", "JAGS", "MAAYA", "IN SEMESTER", "END SEMESTER", "SIXTY THREE ACRES", "NO INTERNET", "NO WIFI", "RIYAL", "NAATU NAATU", "RETRO DAY", "RICK ROLL", "FAILURE", "EMOTIONAL DAMAGE", "PESSIMISTIC", "HOPES CRUSHED", "SUPREMACY"]

#__________________________START SCREEN__________________________
def start_screen():  
    def on_button_click():
        start_button.destroy()
        home_screen()

    #Buttons
    start_button = Button(hangman, image=start_img, borderwidth=0, highlightthickness=0, command=on_button_click, bg=BLACK)
    start_button.place(x=300, y=325)

#__________________________HOME SCREEN__________________________
def home_screen():
    
    def destruction():
        hangman_txt.destroy()
        single_player_button.destroy()
        multiplayer_home_button.destroy()
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
    multiplayer_home_button = Button(hangman, image=multiplayer_img, background=BLACK, command=multiplayer_mode)
    multiplayer_home_button.place(x=50, y=430)
    instructions_button = Button(hangman, image=instructions_img, background=BLACK, command=instructions_mode)
    instructions_button.place(x=50, y=630)
    
    def back_btn():
        destruction()
        start_screen()
        
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    
#__________________________CATEGORIES SCREEN__________________________
def categories_screen():
    
    def destruction():
        output_label.destroy()
        back_button.destroy()
        for category_button in category_buttons:
            category_button.destroy()
    
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
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    
#__________________________MULTIPLAYER SCREEN__________________________
def multiplayer_screen():

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
    input_box = Text(hangman, font=("Helvatica", 96), background="#000000", foreground= PLATINUM, width=10, height=2)
    input_box.tag_configure("center", justify=CENTER)
    input_box.insert("1.0", " ")
    input_box.tag_add("center", "1.0", "end")
    input_box.place(x=135, y=255)
    submit_button = Button(hangman, image=submit_img, background=BLACK, highlightthickness=0, border=0, command=submit_txt)
    submit_button.place(x=325, y=600)
    
    def back_btn():
        destruction()
        home_screen()
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
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
    
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)
    
#__________________________GAME SCREEN__________________________
def game_screen(chosen_word):
    chosen_word = chosen_word.upper()
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
        
    def back_btn():
        destruction()
        #If try and except is not used, then the code throws a name error while blacking back button after using multiplayer screen
        try:
            if chosen_word in chosen_category:
                categories_screen()
            else:
                multiplayer_screen()
        except NameError:
            multiplayer_screen()
            
    def disable():
        for key in keyboard_list:
            key.config(state=DISABLED, bg=GREEN)
     
    #Lists for future refrence  
    keyboard_list = []     
    chosen_letter_list = []
    wrong_chosen_letters = []
    chosen_word_letters = []
    chosen_word_letters_backup = []
    replaced_dashes = []
    dashes=[]
    
    #Checking
    print(chosen_word)
    
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

        Letter_button = Button(hangman, text=letter, font=("Helvetica", 80), bg=BLACK, fg=GREEN, command=letter_click)
        Letter_button.place(x=x, y=y, height=100, width=width_two)
        return Letter_button

    button_positions = [(65, 75, 50, 90, 490, 90), (75, 83, 105, 100, 595, 100), (83, 91, 135, 90, 700, 90)]

    for start, end, x_pos, x_add, y_pos, width_two in button_positions:
        for i in range(start, end):
            Letter_button = create_button(chr(i), x_pos, y_pos)
            keyboard_list.append(Letter_button)
            x_pos += x_add
            j = chr(i).lower()
            try:
                hangman.bind(j, lambda event, button=Letter_button: button.invoke())
            except:
                pass
     
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
            if chosen_word=="RICK ROLL" or chosen_word == "NEVER GONNA GIVE YOU UP":
                go_to_rickroll_screen()
            else:
                go_to_lose_screen()
        
        sum = 0
        for i in chosen_word_letters_backup:
            if i in chosen_letter_list:
                sum+=1
        if sum == len(chosen_word_letters_backup):
            if chosen_word=="RICK ROLL" or chosen_word == "NEVER GONNA GIVE YOU UP":
                go_to_rickroll_screen()
            else:
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

    def go_to_rickroll_screen():
        disable()
        hangman.after(1000, destruction)
        hangman.after(1000, rickroll_screen)

    lives_img = Label(hangman, image=zero_img, borderwidth=0, highlightthickness=0, background=BLACK)
    lives_img.place(x=600, y=50)
    
    lives = [zero_img, one_img, two_img, three_img, four_img, five_img]
    
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)

#__________________________EASTER EGG__________________________
def rickroll_screen():
    def play_rick_roll():
        pygame.mixer.music.load(rickroll_soundtrack)
        pygame.mixer.music.play(loops=0)
        player = tkvideo(rickroll_video, rickroll_label,loop=0, size =(1000,563))
        player.play()

    def destruction():
        rickroll_label.destroy()
    
    hangman.after(1000, play_rick_roll)
    hangman.after(13500,destruction)
    hangman.after(13500, home_screen)

    rickroll_label=Label(hangman, background=BLACK)
    rickroll_label.place(width=1000, height=800)
    play_rick_roll()

#______________________________WIN SCREEN_______________________________________
def winner_screen():
    
    play_win()

    def destruction():
        you_win_label.destroy()
        word_answer.destroy()
        answer.destroy()
        close_button.destroy()
        playagain.destroy()
        winner_video_lbl.destroy()

    def play_again():
        destruction()
        home_screen()
        pygame.mixer.music.stop()

    def close():
        pygame.mixer.music.stop()
        hangman.destroy()
    
    chosen_word_2 = chosen_word
    index_of_space = chosen_word.find(" ", 10)
    chosen_word_edit = chosen_word_2[:index_of_space + 1] + "\n" + chosen_word_2[index_of_space + 1:]
    
    you_win_label=Label(hangman,image=you_win_header, highlightthickness=0, borderwidth=0)
    you_win_label.place(x=255,y=40)
    winner_video_lbl=Label(hangman, background=BLACK)
    winner_video_lbl.place(x=450, y=240, width=500, height=500)
    winner_video=tkvideo(win_video, winner_video_lbl, loop=69, size=(500,500))
    winner_video.play()
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica 35"),highlightthickness=0,borderwidth=0, justify=CENTER)
    word_answer.place(x=50,y=320, width=350, height=100)
    answer=Label(hangman,text=chosen_word_edit,bg=BLACK,fg=GREEN,font=("Helvetica 35 underline"),highlightthickness=0,borderwidth=0, justify=CENTER)
    answer.place(x=50,y=400, width=350, height=150)
    playagain=Button(hangman,image= play_again_img, highlightthickness=0, borderwidth=0, command=play_again)
    playagain.place(x=50,y=575)

    close_button = Button(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, background=BLACK, foreground=BLACK, command=close)
    close_button.place(x=25, y=25)
    
#______________________________LOSE SCREEN_______________________________________
def loser_screen():

    play_lose()
    
    def destruction():
        you_lose_label.destroy()
        word_answer.destroy()
        answer.destroy()
        close_button.destroy()
        playagain.destroy()
        loser_video_lbl.destroy()
    
    def play_again():
        destruction()
        home_screen()
        pygame.mixer.music.stop()
        
    def close():
        pygame.mixer.music.stop()
        hangman.destroy()

    chosen_word_2 = chosen_word
    index_of_space = chosen_word.find(" ", 10)
    chosen_word_edit = chosen_word_2[:index_of_space + 1] + "\n" + chosen_word_2[index_of_space + 1:]
        
    you_lose_label=Label(hangman,image=you_lost_header, highlightthickness=0, borderwidth=0)
    you_lose_label.place(x=255,y=40)
    loser_video_lbl=Label(hangman, background=BLACK)
    loser_video_lbl.place(x=450, y=240, width=500, height=500)
    loser_video=tkvideo(lose_video, loser_video_lbl, loop=69, size=(500,500))
    loser_video.play()
    word_answer=Label(hangman,text="The Word is:",bg=BLACK,fg=PLATINUM,font=("Helvetica 35"),highlightthickness=0,borderwidth=0, justify=CENTER)
    word_answer.place(x=50,y=320, width=350, height=100)
    answer=Label(hangman,text=chosen_word_edit,bg=BLACK,fg=GREEN,font=("Helvetica 25 underline"),highlightthickness=0,borderwidth=0, justify=CENTER)
    answer.place(x=50,y=400, width=350, height=150)
    playagain=Button(hangman,image= play_again_img, highlightthickness=0, borderwidth=0, command=play_again) 
    playagain.place(x=50,y=575)
    
    close_button = Button(hangman, image=close_img, highlightbackground=BLACK, highlightthickness=0, borderwidth=0, background=BLACK, foreground=BLACK, command=close)
    close_button.place(x=25, y=25)

start_screen()

hangman.mainloop()