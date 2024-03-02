from tkinter import *
from tkinter import messagebox
import random
from typing import List, Any
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_random():
    code.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = letter.get()
    nr_symbols = symbol.get()
    nr_numbers = num.get()

    password_list: list[Any] = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    [password_list.append(random.choice(letters)) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    [password_list .append (random.choice(symbols)) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    [password_list.append (random.choice(numbers)) for char in range(nr_numbers) ]

    random.shuffle(password_list)

    password = "".join(password_list)
    code.insert(0, password)


    pyperclip.copy(password)
    #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def write():

    web_name = website.get()
    email_Name = email.get()
    password_name = code.get()

    if len(web_name) == 0 or len(password_name) == 0 or len(email_Name) == 0:
        messagebox.showinfo(title="Error!", message="Dont leave any fields Empty!")

    elif len(password_name) < 8:
        messagebox.showinfo(title="Error!", message="The password must be of 8 characters")
    else:
        answer = messagebox.askokcancel(title=web_name,
                                        message=f"These are you details: \n\nEmail: {email_Name}\nPassword: {password_name}\n\nAre they correct?")

        if answer:
            f = open("data.txt", "a")
            f.write(f"{web_name}  |  {email_Name}  |  {password_name}\n")

            website.delete(0, END)
            code.delete(0, END)
        else:
            code.delete(0, END)
            website.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=350, height=263)
lock = PhotoImage(file="new1.png")
canvas.create_image(175, 131, image=lock)

canvas.grid(row=0, column=1)

label = Label(text="Website:")
label.grid(row=1, column=0)

website = Entry(width=52)
website.grid(row=1, column=1, columnspan=2)
website.focus()

label = Label(text="Email/Username:")
label.grid(row=2, column=0)

email = Entry(width=52)
email.grid(row=2, column=1, columnspan=2)
email.insert(0, "example@gmail.com")

label = Label(text="Password:")
label.grid(row=3, column=0)

code = Entry(width=52)
code.grid(row=3, column=1,columnspan=2)


generate = Button(text="Generate Password",command=pass_random)
generate.grid(row=3, column=3)


add = Button(text="Add", width=44, command=write)
add.grid(row=4, column=1, columnspan=2)

label = Label(text="Total Letters:")
label.grid(row=6, column=0)

letter = Scale( from_=8, to=30, orient=HORIZONTAL,length=320)
letter.grid(row=6,column=1,columnspan=2)

label = Label(text="Total Numbers:")
label.grid(row=7, column=0)

num = Scale( from_=2, to=10, orient=HORIZONTAL,length=320)
num.grid(row=7  ,column=1)

label = Label(text="Total Symbols:")
label.grid(row=8, column=0)

symbol = Scale( from_=2, to=10, orient=HORIZONTAL,length=320)
symbol.grid(row=8,column=1)

window.mainloop()
