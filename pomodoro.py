from tkinter import *
from random import randint
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#04009a"
BLUE = "#325288"

FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
mytimer = None
tick_list = []


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS, mytimer, tick_list

    window.after_cancel(mytimer)
    REPS = 1
    canvas.itemconfig(timer_text, text="00:00")
    mylabel.config(text="Timer", fg=GREEN)
    for i in tick_list:
        window.after(1, i.destroy)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    if REPS in [1, 3, 5, 7]:
        mylabel.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

    if REPS in [2, 4, 6]:
        mylabel.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)

    if REPS == 8:
        mylabel.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global REPS, mytimer, tick_list
    mins = count // 60
    sec = count % 60

    if mins < 10:
        mins = "{}".format('0' + str(mins))
    if sec < 10:
        sec = "{}".format('0' + str(sec))
    if count // 60 > 1:
        canvas.itemconfig(timer_text, text="{}:{}".format(mins, sec),fill="white")
    else:
        colors = [PINK,RED,GREEN,YELLOW,BLUE,BLACK]
        color = colors[randint(0,5)]
        canvas.itemconfig(timer_text, text="{}:{}".format(mins, sec),fill=color)

    if count > 0:
        mytimer = window.after(1000, count_down, count - 1)
    if count == 0:
        REPS += 1
        start_timer()
        if REPS % 2 == 0:
            mylabel1 = Label(text=checktext, fg=GREEN, bg=YELLOW, font=("Courier", "15"))
            mylabel1.grid(column=1, row=REPS + 2)
            tick_list.append(mylabel1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)

timer_text = canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(20)

mylabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Courier", "20", "bold"))
mylabel.grid(column=1, row=0)
checktext = "✔"
# mylabel1 = Label(text=checktext, fg=GREEN, bg=YELLOW, font=("Courier", "15"))
# mylabel1.grid(column=1, row=3)

button1 = Button(text="Start", bg="white", border="0", highlightthickness=0, font=("Courier", "10"),
                 command=start_timer)
button1.grid(column=0, row=2)
button2 = Button(text="Reset", bg="white", border="0", highlightthickness=0, font=("Courier", "10"),
                 command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()
