import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

recognizer = sr.Recognizer()
engine = pyttsx3.init()

newsapi = os.getenv("NEWS_API_KEY")
api_key=os.getenv("OPENAI_API_KEY")

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    client = OpenAI(api_key=api_key)

    response = client.responses.create(
    model="gpt-5.6",
    input="Write a one-sentence bedtime story about a unicorn.",
)

    return(response.output_text)    


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
            webbrowser.open("https://github.com/satyamsharma786")    
    elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        
        if r.status_code==200:
            #parse the JSON response
            data=r.json()
            
            #extract the articles
            articles=data.get("articles",[])
            
            #print the headlines
            for article in articles:
                speak(article["title"])
        else:
            #let OpenAI handle the requests
            output = aiProcess(c)
            speak(output)
            
        

if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
        #listen for the wake word jarvis
        # obtain audio from the microphone
        
        r = sr.Recognizer()
        
            
        print("Recognizing....")    
        
        
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() =="jarvis":
                speak("Ya")
                
            #listen for the command
            with sr.Microphone() as source:
                print("Jarvis Active....")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)
                command=r.recognize_google(audio)
            
                processCommand(command)    
        
        except Exception as e:
            print("Error; {0}".format(e))