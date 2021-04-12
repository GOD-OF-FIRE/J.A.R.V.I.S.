import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
    elif hour>=18 and hour<20:
        speak("Good Evening ")  
    else:
        speak("Hello")  
    speak(" I am JARVIS at your service sir, tell me how can i help you")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        #speak(f"You said: {query}\n")
        print(f"You said: {query}\n")
    except Exception as e:
        #print(e)
        print("I can't hear that sir, please say it again.")
        return "None"
    return query
if __name__ =="__main__":
    wishMe()
    while True:
        query = takecommand()
        if 'Wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open YouTube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open Google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open Gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        elif 'open classroom' in query:
            webbrowser.open("https://classroom.google.com/u/0/h")
        elif 'play music' in query:
            n=random.randint(0,150)
            music_dir ='E:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[n]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strTime} ")
        elif 'open Chrome' in query:
            chromePath ="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)
        elif 'jarvis are you there' in query:
            speak("At your service sir")
        elif 'my name' in query:
            speak("Your name is Kushagra Gupta, My creator and owner")
        elif 'who am I' in query:
            speak(" You are my BOSS , who created me ")
        elif 'shutdown' or 'shut down' in query:
            speak("Ok your beast laptop is going to shutdown")
            os.system('shutdown -s')




        

            
