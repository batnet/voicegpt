

import speech_recognition as sr
import requests
from gtts import gTTS
from playsound import playsound
import random
import os
from colorama import Fore

r = sr.Recognizer()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def record():
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr_TR')
            response = requests.get("https://dev-gpts.pantheonsite.io/wp-admin/js/apis/GPT-3.php?text=" + str(voice))
            cevap = response.text
            print("---------------------\nAlgılanan Cümle: "+ Fore.GREEN + str(voice)+ Fore.RESET +"\n---------------------\nVoiceGPT Cevabı: "+ Fore.RED + str(cevap) + Fore.RESET +"\n---------------------")
            speak(cevap)
        except sr.UnknownValueError:
            print("Algıda sorun yaşıyorum, bip bop bip!")
        except sr.RequestError:
            print("Teknik sorunlar! bitmek bilmiyor...")
        return voice



while True:
    print("\nVoiceGPT Sizi Dinliyor...")
    voice = record()
    clear_console()