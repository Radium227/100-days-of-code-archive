BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas as pd

window = Tk()
window.geometry("965x800")
window.title("Flashy")

window.config(background=BACKGROUND_COLOR, pady=65, padx=65)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="images/card_front.png")
canvas.create_image(410, 270, image=image)
canvas.create_text(400, 160, text="Title", font=("Ariel", 40, "italic"),tag="text")
canvas.create_text(400, 290, text="word", font=("Ariel", 60, "bold"), tag='text')
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")

with open("data/french_words.csv") as file:
    df = pd.read_csv(file)
    dict_data = df.to_dict(orient='dict')


def delete_text():
    canvas.delete("text")


def right_button():
    delete_text()
    canvas.create_text(400, 160, text="French", font=("Ariel", 40, "italic"),tag="text")
    canvas.create_text(400, 290, text=dict_data["French"][random.randint(1, 100)], font=("Ariel", 60, "bold"),tag="text")


def wrong_button():
    delete_text()
    canvas.create_text(400, 160, text="French", font=("Ariel", 40, "italic"),tag="text")
    canvas.create_text(400, 290, text=dict_data["French"][random.randint(1, 100)], font=("Ariel", 60, "bold"),tag="text")


button = Button(image=wrong, highlightthickness=0, command=wrong_button)
button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
button = Button(image=right, highlightthickness=0, command=wrong_button)
button.grid(row=1, column=1)

window.mainloop()
