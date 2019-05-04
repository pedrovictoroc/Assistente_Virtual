#-*- coding: utf-8 -*-

#import section

from chatterbot.trainers import ListTrainer #treinador do BOT
from chatterbot import ChatBot #Base para utilizar o BOT
import os   #Importa as funções do sistema operacional
import speech_recognition as sr #Base para o reconhecimento de voz
import pyttsx3  #Usado para devolução de resposta com audio pelo BOT
import time #Usado para funções de tempo

def saudar_ao_iniciar(hora,speaker):    #Iniciador com suadações Pyttsx3 e Time
    if(0 <= hora <=5):
        resposta = "Esta tarde, você deveria dormir!"
        speak(resposta,speaker)
    elif(6<= hora <=12):
        resposta = "Bom dia, como posso ajudar?"
        speak(resposta,speaker)   
    elif(13 <= hora <= 17):
        resposta = "Boa tarde, como posso ajudar?"
        speak(resposta,speaker)       
    elif(18 <= hora <= 23):
        resposta = "Boa noite, como posso ajudar?"
        speak(resposta,speaker)

def dizer_hora(speaker):    #Função de devolução de hora usando Pyttsx3 e Time 
    hora = time.localtime()[3]
    minuto = time.localtime()[4]
    segundo = time.localtime()[5]

    resposta = ("São " +str(hora)+ " horas e " +str(minuto)+ " minutos")
    speak(resposta,speaker)
    

def procedimento_de_fala(bot,speaker):  #Procedimento de fala que usa o banco de dados do BOT
    recognizer = sr.Recognizer() #Capta o reconhecedo de voz

    with sr.Microphone() as sound_user: #Captura a voz do usuario
        recognizer.adjust_for_ambient_noise(sound_user) #Ajusta para ignorar ruidos
        continuar = True
        
        while continuar:
            try:
                audio = recognizer.listen(sound_user)
                speech = recognizer.recognize_google(audio, language = 'pt')    #Usando a base google em português
                print("Você: ", speech) #Saída de terminal para verificação de entrada
                response = bot.get_response(speech) #Resposta compatível com o que foi dito
                #print("Bot: ", response)    #saída para terminal para verificação de saída
                #print("") #Quebra de linha
                
                if(speech == "Que horas são" or speech == "diga a hora"):
                    dizer_hora(speaker)
                if(speech == "finalizar" or "parar"): #Para a execução
                    continuar = False
                else:
                    speak(response,speaker) #Pronunciar a resposta do BOT
            except:
                speak("Algo errado ocorreu",speaker)    #Aviso de erro com som
    

def treinar_bot(bot):
    trainer = ListTrainer(bot) #Seta um treinador para o BOT
    for _file in os.listdir('chats'):
        
        #Para cada arquivo na pasta chats ler todas as linhas e captar respostas e perguntas

        lines = open('chats/' + _file, 'r').readlines() 
        trainer.train(lines)

def speak(text,speaker):    #Função para que o BOT responda com audio
    speaker.say(text)
    speaker.runAndWait()

def main():
    speaker = pyttsx3.init()    #Inicio o speaker

    bot = ChatBot('Jarvis',read_only = True)    #Defino o nome do meu bot e afirmo que somente lerá arquivos
    deve_treinar = input("Deseja treinar o BOT?: (S) (N)")  #Pergunta ao usuario se ocorreu alterações no Banco de Dados

    saudar_ao_iniciar(time.localtime()[3],speaker)  #Real Inicio do Programa

    if(deve_treinar.upper() == "S"):    #Inicia o programa treinando o BOT
        treinar_bot(bot)
        procedimento_de_fala(bot,speaker)
    else:
        procedimento_de_fala(bot,speaker)


main() #Inicia o programa