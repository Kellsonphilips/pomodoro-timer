from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#B9FFF8"
DARK_GREEN = "#3CCF4E"
BLUE = "#3120E0"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(countdown_text, text="00:00")
    header_text.config(text="Timer")
    goal_check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown_timer(LONG_BREAK_MIN * 60)
        header_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown_timer(SHORT_BREAK_MIN * 60)
        header_text.config(text="Break", fg=PINK)
    else:
        countdown_timer(WORK_MIN * 60)
        header_text.config(text="Work", fg=DARK_GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    timing = f"{count_min}:{count_sec}"
    canvas.itemconfig(countdown_text, text=timing)
    if count > 0:
        global timer
        timer = window.after(1000, countdown_timer, count - 1)
    else:
        start_timer()
        success = ""
        work_section = math.floor(reps/2)
        for n in range(work_section):
            success += "✓"
        goal_check.config(text=success)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work Timer for productivity")
window.config(padx=100, pady=100, bg=GREEN)

canvas = Canvas(width=200, height=300, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 150, image=tomato_img)
countdown_text = canvas.create_text(100, 170, text="00:00", font=(FONT_NAME, 50, "bold"))
canvas.grid(column=1, row=1)

header_text = Label(text="Timer", font=(FONT_NAME, 70, "bold"), fg=DARK_GREEN, bg=GREEN)
header_text.grid(column=1, row=0)

goal_check = Label(font=(FONT_NAME, 50), fg=DARK_GREEN, bg=GREEN)
goal_check.grid(column=1, row=3)

timer_start = Button(text="Start", font=(FONT_NAME, 20, "bold"), fg=BLUE, highlightthickness=0, command=start_timer)
timer_start.grid(column=0, row=2)

timer_reset = Button(text="Reset", font=(FONT_NAME, 20), fg=RED, highlightthickness=0, command=reset_timer)
timer_reset.grid(column=2, row=2)

window.mainloop()
