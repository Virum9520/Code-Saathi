import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(counter, text='00:00')
    timer_text.config(text='Timer', fg=GREEN)
    tick.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        time = WORK_MIN
        timer_text.config(text='WORK', fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        time = SHORT_BREAK_MIN
        timer_text.config(text='Break', fg=PINK)
    elif reps == 8:
        time = LONG_BREAK_MIN
        timer_text.config(text='Break', fg=RED)
    else:
        time = 0
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minutes = int(count/60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(counter, text=f'{minutes}:{sec}')
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick['text'] += '✔'


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, background=YELLOW)

canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
counter = canvas.create_text(100, 122, text='00:00', font=(FONT_NAME, 35, 'bold '))
canvas.grid(row=1, column=1)

timer_text = tk.Label(text='Timer', font=(FONT_NAME, 40, 'normal'))
timer_text.config(foreground=GREEN, background=YELLOW)
timer_text.grid(row=0, column=1)

start_button = tk.Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

tick = tk.Label(text='', fg=GREEN, background=YELLOW)
tick.grid(row=3, column=1)

window.mainloop()
