
from gtts import gTTS
import os
import pygame.mixer
from time import sleep

user_text=input("plese type something to teanslate : ")

translate=gTTS(text=user_text ,lang='en')
translate.save('chatbot.wav')
pygame.mixer.init()

path_name=os.path.realpath('chatbot.wav')
real_path=path_name.replace('\\','\\\\')
pygame.mixer.music.load(open(real_path,"rb"))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
