from gtts import gTTS
import os

text = open("demo.txt", 'r', encoding='utf-8').read()
# Google speech language codes: official link for language codes
audio = gTTS(text=text, lang='en', slow=False)
audio.save("demo.mp3")
os.system("start demo.mp3")
