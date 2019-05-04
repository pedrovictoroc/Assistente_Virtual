#-*- coding: utf-8 -*-

#importando os módulos do chatbot

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

import os

import speech_recognition as sr
import pyttsx3  #para usar o speak

speaker = pyttsx3.init()

bot = ChatBot('Stark',read_only = True)

"""
trainer = ListTrainer(bot) #definir o treinamento

for _file in os.listdir('chats'): #percorrer todos os arquivos em chats
    lines = open('chats/' + _file, 'r').readlines() #ler linhas

    trainer.train(lines)
"""
def speak(text):
    speaker.say(text)
    speaker.runAndWait()

r = sr.Recognizer() #reconhecer a voz

with sr.Microphone() as s:  #captar a voz na variavle s
    r.adjust_for_ambient_noise(s) #configurar o ruido

    while True:
        try:
            audio = r.listen(s)

            speech = r.recognize_google(audio,language = 'pt') #usando o googlee e a lingua portuguesa
            
            print("Você disse: ", speech)
            response = bot.get_response(speech)
            print("Bot:", response)
            print("")
            speak(response)
        except:
                speak('Algum erro ocorreu')   