# FLASH CARD PROJECT

from tkinter import *
from tkinter import messagebox      # This module is separate from tkinter hence we've to import it
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}       # this global variable represents the current card which is being displayed
# to_learn represents the list of dictionaries {French:____, English:____} i.e. words which user doesn't know
to_learn = []


# ---------------------------------------------------------------------------------------------------------------------#
# this is the 1st part of code in which we are reading the words from either french_words.csv or updated_words.csv
# based on the progress of user (first time when the program runs, it takes the words from 'french_words.csv')
# otherwise it tries to take from the 'updated_words.csv'
try:
    data = pandas.read_csv("data/updated_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
# ---------------------------------------------------------------------------------------------------------------------#


# ---------------------------------------------------------------------------------------------------------------------#
# this is 2nd part of the code in which we are defining different functions for different tasks

# this function is for displaying the next French word in the card
def next_card():
    # Note: flip_timer is the time object (we can assume as time also) which refers to the time from the button clicking
    # to the current time
    global current_card, flip_timer
    window.after_cancel(flip_timer)        # <----Try to understand this line
    # firstly when this function next_card() is called, then tell the window to reset the timer from flip_timer so that
    # when next word is displayed, then the count is again started from zero (otherwise no matter when we click on
    # button, it will display the English word whenever 4 seconds completed)

    try:
        current_card = random.choice(to_learn)
    except IndexError:      # if there are no cards to chose from to_learn
        messagebox.showinfo(title="CONGRATULATIONS !!", message="You know most of the frequently used French Words")
    else:
        canvas.itemconfigure(title, text="French", fill="black")        # set title to French
        canvas.itemconfigure(word, text=current_card["French"], fill="black")       # and word to French word fm dict. current_card
        canvas.itemconfig(card_background, image=card_front_img)        # set background to card_front_img
        flip_timer = window.after(4000, flip_card)      # <----Try to understand this line


def flip_card():
    canvas.itemconfig(card_background, image=card_back_img)     # changing background image
    canvas.itemconfig(title, text="English", fill="white")      # Setting the english words corresponding to current French word
    canvas.itemconfig(word, text=current_card["English"], fill="white")


def is_known():
    try:
        to_learn.remove(current_card)      # whenever user knows the French word, remove that word from list of to_learn
    except ValueError:      # if there is no word in to_learn
        messagebox.showinfo(title="CONGRATULATIONS !!", message="You know most of the frequently used French Words")
    else:
        # print(len(to_learn))
        updated_data = pandas.DataFrame(to_learn)
        updated_data.to_csv("data/updated_words.csv", index=False)
        # after removing that word, we are using pandas to convert this updated list to a CSV file (using DataFrame)
        # and then further we are fetching the next card from this CSV only
        next_card()     # calling next_card() becoz whether user knows or don't, it should see a new card from that new CSV file
# ---------------------------------------------------------------------------------------------------------------------#


# ---------------------------------------------------------------------------------------------------------------------#
# this is 3rd part of code, in which we are creating our GUI with tkinter and calling our above defined functions.
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, flip_card)      # ONLY for the first time (to initiate) countdown is started

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

next_card()     # for fisrt time when the user hasn't clicked any button

window.mainloop()
