from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✓"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 
def onReset():
  window.after_cancel(TIMER)
  titleLabel.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timerText, text="00:00")
  global REPS
  REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def onStart():
  global REPS
  if REPS == 8:
    titleLabel.config(text="Break", fg=RED)
    onTick(LONG_BREAK_MIN * 60)
  elif REPS % 2 == 0:
    titleLabel.config(text="Work", fg=GREEN)
    onTick(WORK_MIN * 60)
  else:
    titleLabel.config(text="Break", fg=PINK)
    onTick(SHORT_BREAK_MIN * 60)
  REPS += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def onTick(count):
  minute = int(count / 60)
  second = count % 60
  canvas.itemconfig(timerText, text=f"{minute:02.0f}:{second:02.0f}")
  if count > 0:
    global TIMER
    TIMER = window.after(1000, onTick, count - 1)
  else:
    if REPS % 2 == 1:
      addCheckmark()
    onStart()

def addCheckmark():
  output = ""
  for _ in range(int((REPS+1)/2)):
    output += CHECKMARK
  checkLabel.config(text=output)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

titleLabel = Label(text = "Timer", fg=GREEN, bg=YELLOW, font = (FONT_NAME, 30, "bold"))
titleLabel.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100,112, image=img)
timerText = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

leftButton = Button(text = "START", command = onStart, highlightthickness=0)
leftButton.grid(column=0, row=2)
rightButton = Button(text = "RESET", command = onReset, highlightthickness=0)
rightButton.grid(column=2, row=2)

checkLabel = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "normal"))
checkLabel.grid(column=1, row=3)

window.mainloop()