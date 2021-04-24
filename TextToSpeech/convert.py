from gtts import gTTS
import os

text = "Hey! Deepesh says Namaste!"
audio = gTTS(text=text, lang='en', slow=False)
audio.save('lol.mp3')

os.system("start lol.mp3")
