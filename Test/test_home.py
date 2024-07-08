import tkinter as tk

root = tk.Tk()
root.geometry("500x100")

# Creating a label with the text "EXp Batch" where "Batch" is on the next line
chosen_word = "the fault in our stars"
index_of_space = chosen_word.find(" ", 15)
chosen_word_edit = chosen_word[:index_of_space + 1] + "\n" + chosen_word[index_of_space + 1:]

label = tk.Label(root, text=chosen_word_edit)
label.pack()

root.mainloop()
