import os
import random
from tkinter import Label, Button, PhotoImage
from home_screen import home_screen
from game_screen import game_screen

BLACK = "#1C1C1E"

def categories_screen(hangman):
    
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
    back_button = Button(hangman, image=back_img,  command=back_btn, highlightthickness=0, borderwidth=0, bg=BLACK)
    back_button.place(x=25, y=25)


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
                  "NATURALS", "CORNETTO","SORBET",
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
              "YOUNGBLOOD"]

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
                  "3 IDIOTS", 
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
                  "PRABHAKAR", 
                  "TRAUMA", 
                  "REVISION", 
                  "TIME MANAGEMENT", 
                  "SYLLABUS"]

movies_list = ["3 IDIOTS", 
               "JAB WE MET",
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

#__________________________IMAGES__________________________ 
categories_header_img = PhotoImage(file=f"{os.getcwd()}/Images/Categories.png")
ice_cream_img = PhotoImage(file=f"{os.getcwd()}/Images/Ice_Cream.png")
movies_img = PhotoImage(file=f"{os.getcwd()}/Images/Movies.png")
music_img = PhotoImage(file=f"{os.getcwd()}/Images/Music.png")
nostalgia_img = PhotoImage(file=f"{os.getcwd()}/Images/Nostalgia.png")
novels_img = PhotoImage(file=f"{os.getcwd()}/Images/Novels.png")
pes_img = PhotoImage(file=f"{os.getcwd()}/Images/PES.png")
back_img = PhotoImage(file=f"{os.getcwd()}/Images/Back.png")