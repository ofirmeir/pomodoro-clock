from tkinter import Tk, Button, Label, Canvas, PhotoImage
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 0.2
# SHORT_BREAK_MIN = 5
SHORT_BREAK_MIN = 0.2
# LONG_BREAK_MIN = 20
LONG_BREAK_MIN = 0.2
reps = 0
timer = None
check_marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global timer
    global reps
    # stops the window timer
    window.after_cancel(timer)
    # reset timer text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # change timer_label to "Timer"
    timer_title.config(text="Timer", fg=GREEN)
    # reset check_marks
    label_check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def btn_start_clicked():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        timer_title.config(text="Long Break", fg=RED)
        count_down(long_break_seconds)
    elif reps % 2 == 0:
        timer_title.config(text="Short Break", fg=PINK)
        count_down(short_break_seconds)
    else:
        timer_title.config(text="Work", fg=GREEN)
        count_down(work_seconds)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(counter):
    global check_marks
    global timer
    minuets = floor(counter / 60)
    seconds = counter % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    if counter > 0:
        canvas.itemconfig(timer_text, text=f"{minuets}:{seconds}")
        timer = window.after(1000, count_down, counter - 1)
    else:
        btn_start_clicked()
        work_cycles = floor(reps / 2)
        marks = ""
        for _ in range(work_cycles):
            marks += "✔"
        label_check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

btn_start = Button(text="Start", command=btn_start_clicked)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", command=reset_timer)
btn_reset.grid(row=2, column=2)

label_check_marks = Label(fg=GREEN, bg=YELLOW)
label_check_marks.grid(row=3, column=1)

window.mainloop()
