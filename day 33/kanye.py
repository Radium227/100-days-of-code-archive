
from tkinter import *
import requests
response = requests.get(url="https://api.kanye.rest")

data = response.json()["quote"]
print(data)


def get_quote():

    response=requests.get(url="https://api.kanye.rest")
    print(response)
    data=response.json()["quote"]
    print(data)
    canvas.itemconfig(quote_text, text=data)



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=420)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=data, width=250, font=("Arial", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()