from gtts import gTTS
import os

f = open('text_to_speech.txt','r')
speech_text = f.read()

language = 'en'
audio = gTTS(text=speech_text,lang=language,slow=False)

audio.save('speech_1.wav')
os.system('speech_1.wav')