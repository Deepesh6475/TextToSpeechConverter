from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()


def text_to_speech():
    text = entry.get()
    audio = gTTS(text=text, lang='en', slow=FALSE)
    audio.save("gui_text.mp3")
    os.system("start gui_text.mp3")


label = Label(text="Enter your text to be converted: ")
canvas.create_window(200, 130, window=label)

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Convert", command=text_to_speech)
canvas.create_window(200, 230, window=button)

root.mainloop()
