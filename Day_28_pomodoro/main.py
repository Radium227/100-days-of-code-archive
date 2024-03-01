from tkinter import *
import math

window = Tk()
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1.1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer=0


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    label.config(text="TIMER", bg=YELLOW, fg="black",font=(FONT_NAME, 40))
    canvas.itemconfig(timer_text, text="00:00")
    tick.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_seconds = 2
    short_break = SHORT_BREAK_MIN*60
    long_seconds = LONG_BREAK_MIN*60

    reps += 1
    if reps % 2 != 0:
        count_down(work_seconds)
        label.config(text="WORK", bg=YELLOW, fg=RED, font=(FONT_NAME, 40,"bold"))

    elif reps % 8 == 0:
        count_down(long_seconds)
        label.config(text="CHILL", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40,"bold"))
    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="BREAK", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40,"bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2, column=2)


def count_down(num):
    minute = math.floor(num / 60)
    second = num % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if num > 0:
        global timer
        timer=window.after(1000, count_down, num - 1)

    else:
        start_timer()
        mark = ""
        for n in range(math.floor(reps / 2)):
            mark += text
            tick.config(text=mark)


fg = GREEN
text = "✓"

label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40,"bold"))
label.grid(row=1, column=2)

button = Button(text="Start", command=start_timer)
button.grid(row=3, column=1)

reset = Button(text="Reset",command=reset)
reset.grid(row=3, column=3)

tick = Label(bg=YELLOW, fg=fg, font=("Arial", 20, "bold"))
tick.grid(row=4, column=2)

window.mainloop()
