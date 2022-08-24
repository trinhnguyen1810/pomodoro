
import math
from tkinter import *
from PIL import Image, ImageTk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#B4EEB4"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
checkmark = ""
time = None


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer, text="Pomodoro Timer")
    canvas.itemconfig(timer_text, text="0:00")
    canvas.itemconfig(check, text="")
    global rep
    rep = 0

def count_down(count):
    minute = count // 60
    second = count % 60
    if second < 10:
        second = f'0{second}'
    canvas.itemconfig(timer_text, text=f'{minute}:{second}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checkmark = ""
        work_sessions = math.floor(rep / 2)
        for _ in range(work_sessions):
            checkmark += "✔"
        canvas.itemconfig(check, text=checkmark)


def start_timer():
    global rep,timer
    rep += 1

    long_break = 60 * LONG_BREAK_MIN
    short_break = 60 * SHORT_BREAK_MIN
    work_time = 60 * WORK_MIN

    if rep % 8 == 0:
        canvas.itemconfig(timer, text="ITS A LONG BREAKKK", fill=GREEN)
        count_down(long_break)


    elif rep % 2 == 0:
        canvas.itemconfig(timer, text="SHORT BREAK TIME", fill=GREEN)
        count_down(short_break)

    else:
        canvas.itemconfig(timer, text="GOTTA WORK WORK", fill=PINK)
        count_down(work_time)



window = Tk()
window.geometry("500x500")
window.title("Pomodoro")
canvas = Canvas(window, width=500, height=500)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("pomodoro.png"))
canvas.create_image(250, 250, image=img)
timer_text = canvas.create_text(260, 250, text="0:00", fill="white", font=(FONT_NAME, 60, "bold"))
timer = canvas.create_text(260, 50, text="Pomodoro Timer", fill="RED", font=(FONT_NAME, 30, "bold"))
check = canvas.create_text(260, 430, text= checkmark, fill="RED", font=(FONT_NAME, 20, "bold"))
startbutton = Button(text="start", command=start_timer, fg="black", bg="gray", highlightthickness=2)
startbutton.place(x=100, y=435)
resetbutton = Button(text="reset", command =reset, fg="black",bg="gray",highlightthickness=2 )
resetbutton.place(x=400, y=435)
window.mainloop()