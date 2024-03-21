BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas as pd

new = {}
try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    old=pd.read_csv("data/french_words.csv")
    to_learn=old.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=new["English"], fill="white")
    canvas.itemconfig(background, image=image_back, )


def new_card():
    global new, flip_timer
    window.after_cancel((flip_timer))
    new = random.choice(dict_data)
    canvas.itemconfig(background, image=image)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=new["French"], fill="black")
    flip_timer = window.after(1000, func=flip_card)

def is_known():
    dict_data.remove(new)
    new_card()
    data=pd.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv",index=False)



window = Tk()
window.geometry("965x800")
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, pady=65, padx=65)
flip_timer = window.after(1000, func=flip_card)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")
background = canvas.create_image(410, 270, image=image)
canvas_title = canvas.create_text(400, 160, text="Title", font=("Ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 290, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")

with open("data/french_words.csv") as file:
    df = pd.read_csv(file)
    dict_data = df.to_dict(orient='records')


def delete_text():
    canvas.delete("text")


button = Button(image=wrong, highlightthickness=0, command=new_card)
button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
button = Button(image=right, highlightthickness=0, command=is_known)
button.grid(row=1, column=1)

new_card()
window.mainloop()
