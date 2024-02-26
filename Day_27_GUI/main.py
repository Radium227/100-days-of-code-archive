from tkinter import *


# # Creating a new window and configurations

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
# Adding padding to the window
window.geometry("320x200")

# Creating a frame to contain all widgets with padding
frame = Frame(window, padx=7, pady=20)
frame.pack()

miles = Entry(frame, width=15)
miles.grid(row=1, column=2)

label_1 = Label(frame, text="Miles")
label_1.grid(row=1, column=3)

cable = Label(frame, text="is equal to ")
cable.grid(row=2, column=1)

km = Label(frame, text="km ")
km.grid(row=2, column=3)

label = Label(frame, text="0 ")
label.grid(row=2, column=2)


def button_click():
    value = miles.get()

    answer = float (value) * 1.6
    answer_round=round(answer, 2)
    label.config(text=answer_round)
    print(answer_round)


button = Button(frame, text="Calculate", command=button_click)
button.grid(row=4, column=2)

window.mainloop()


# from tkinter import *
#
# window = Tk()
# window.title("My first GUI")
# window.minsize(width=300, height=300)
# # Label
#
# label = Label(text="It's a label", font=("Arial", 30, "bold"))
# label.pack()
#
# label["text"] = "New Game"
# label.config(text="GAMER")
#
# # Entry
# input = Entry(width=25)
# input.pack()
#
#
# def button_click():
#     label.config(text=input.get(), font=("Arial", 40, "bold"))
#
#
# # BUTTON
# button = Button(text="Do you want free money?", command=button_click)
# button.pack()
#


# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
# #
# #
# # Buttons
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
#
# # Spinbox
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
#
# # Scale
# # Called with current scale value.
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
#
# # Checkbutton
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
#
# # Radiobutton
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
