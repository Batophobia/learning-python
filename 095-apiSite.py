import requests
import os
from dotenv import load_dotenv
from tools import getFullPath
import tkinter as tk
import json
from playsound import playsound

BASE_DIR = getFullPath()
load_dotenv(f"{BASE_DIR}/day87/secrets.env") # URL (not secret)
load_dotenv(f"{BASE_DIR}/day87/secrets.local.env") # KEY (secret)
KEY = os.getenv("KEY")
URL = os.getenv("URL")
# Daily Requests: 350 (Free Tier) [100KB per request]

with open("day95/voices.json") as file:
  voices = json.load(file)

def play():
  playsound("./day95/output.mp3")

def tts():
  params = {
    "key": KEY,
    "hl": getCode(),
    "v": voice.get(),
    "c": "MP3",
    "f": "16khz_16bit_stereo",
    "src": userInput.get(1.0, "end-1c")
  }
  resp = requests.get(URL, params=params)
  with open(f'./day95/output.mp3', 'wb') as f:
    f.write(resp.content)
  doneLabel.grid(column=2, row=0)
  playButton.grid(column=2, row=1, rowspan=2)

window = tk.Tk()
window.title("Text-To-Speech")
window.config(padx=20, pady=20)

userInput = tk.Text(height=20, width=40)
userInput.grid(column=0, row=0, rowspan=3)

def getVoices():
  return voices[country.get()]["voices"]

def getCode():
  return voices[country.get()]["code"]

def countryChange(*args):
  voice.set('')
  ddVoices['menu'].delete(0, 'end')

  for v in getVoices():
    ddVoices['menu'].add_command(label=v, command=tk._setit(voice, v))
  voice.set(getVoices()[0])

country = tk.StringVar(window)
country.set(next(iter(voices)))
country.trace("w", countryChange)
ddCountry = tk.OptionMenu(window, country, *voices.keys())
ddCountry.grid(column=1, row=0)

voice = tk.StringVar(window)
voice.set(getVoices()[0])
ddVoices = tk.OptionMenu(window, voice, getVoices())
ddVoices.grid(column=1, row=1)

goButton = tk.Button(text="Go", command = tts)
goButton.grid(column=1, row=2)

doneLabel = tk.Label(text="Completed successfully", fg="#9bdeac", font=("Arial", 20, "bold"))
playButton = tk.Button(text="Play", command = play)

window.mainloop()