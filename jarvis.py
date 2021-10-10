import audioplayer
import pyttsx3                                  #pip install pyttsx3
import speech_recognition as sr                 #pip install speechRecognition
import datetime
import wikipedia                                #pip install wikipedia
import webbrowser 
import os
import smtplib
import pyautogui                                #pip install pyautogui
import psutil                                   #pip install psutil
import pyjokes                                  #pip install pyjokes
import random
import bs4 as bs
import urllib.request
import wolframalpha                             #pip install wolframalpha
from audioplayer import AudioPlayer                         
#from PyQt5 import QtWidgets, QtGui, QtCore
#from PyQt5.Qtcore import QTimer, QTime, QCate ,Qt
#from PyQt5.QtGui import QMovie
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *
#from PyQt5.uic import loadUiType
#from jarvisUI import ui_jarvisUI



class person:
    name = ''
    def setName(self, name):
        self.name = name

class jarvis:
    name = ''
    def setName(self, name):
        self.name = name

person_obj = person()
jarvis_obj = jarvis()
jarvis.name = ''
person_obj.name = ""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

newVoiceRate = 150  #voice rate 
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("jarvis at your service. How can i help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def open():
    url = "https://github.com/https-github-com-zameel28/J.A.R.V.I.S"
    webbrowser.get().open(url)

def sendEmail(to, content):                                   #makesure that you you turned on less secure apps in google account
    mail = "blynkofzameel@gmail.com"
    password = "Blynk123"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mail, password)
    mailto = to
    server.sendmail(mailto, to, content)
    server.close()

def screenshot():
     img = pyautogui.screenshot()
     img.save("screen.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    speak("battery is at ")
    speak(percent+'% | '+plugged)

def jokes():
    speak(pyjokes.get_joke())
 
def there_exists(terms):
    for term in terms:
        if term in query:
            return True

def record_audio(ask=""):
    r = sr.Recognizer()
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        query = ''
        try:
            query = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            print('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        print(">>", query.lower()) # print what user said
        return query.lower()

def date():
    year = int(datetime.datetime.now().year)   
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def tellDay():
      
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)

def null():
    while  True:
        query = takeCommand().lower() 
        if  "jarvis" in query:
            speak("ready")
            break         

def setup():
    audioplayer.AudioPlayer("Jarvis Welcome Back Sir _ Jarvis Voice.mp3").play(block=True)

def intro():
    audioplayer.AudioPlayer("Ironman Jarvis.mp3").play(block=True)


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if there_exists(["hey jarvis" , "ok jarvis", "hello jarvis", "hi jarvis","jarvis"]):
            setup()
            wishMe()
            while True:
            # if 1:
                query = takeCommand().lower()

       
                if there_exists(['wikipedia search', 'tell about']):
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)                         
                    null()
                elif there_exists(['play music', 'play songs']):
                    music_dir = 'songs'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                    null()
                elif 'time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                    null()
                elif there_exists(["date"]):
                    date()    
                    null()
                elif 'send email' in query:
                    try:
                        speak("What should I say?")
                        content = takeCommand()
                        to = str(input("Enter Recvers Mail ID : "))    
                        sendEmail(to, content)
                        speak("Email has been sent!")
                    except Exception as e:
                        print(e)
                        speak("Sorry i can't send mail sir") 
                    null()    
                elif there_exists(['about you','say about you', 'introduce yourself']):
                    intro() 
                    speak("I am created by zameel ali, subhash and naveen")
                    speak("I was made by using python")
                    speak("i am born on 25th may 2020")
                    speak("hope you got the information")
                    null()
                elif there_exists(["exit", "quit", "bye","offline"]):
                    speak("i am turning off systems")
                    quit()
                elif "logout" in query:
                    os.system("shutdown - 1")

                elif "shutdown" in query:
                    os.system("shutdown /s /t 1")

                elif "restart" in query:
                    os.system("shutdown /r /t 1") 

                elif there_exists(['remember this', 'save this messeage']):
                    speak("what should i remember? sir")
                    data = takeCommand()
                    speak("you said me to remember" + data)
                    remember = open("data.txt", "w")
                    remember.write(data)
                    remember.close()
                    null()   
                elif there_exists(['do you remember?', 'what did i say', 'do you know anything']):
                    remember = open("data.txt", "r")
                    speak("you said me to remember this" + remember.read())
                    null()
                elif "take a screenshot" in query:
                    screenshot()
                    speak("Done!")
                    null()                
                elif "cpu clock" in query:
                    cpu()
                    null()   
                elif there_exists(['tell me a joke', "let's make some fun"]):
                    jokes()
                    null()
                elif there_exists(["weather forecast"]):
                    search_term = query.split("for")[-1]
                    url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
                    webbrowser.get().open(url)
                    speak("Here is what I found for on google")
                    null()
                elif there_exists(["support","contact"]):
                    open()
                elif "stock price of" in query:
                    search_term = query.split("for")[-1]
                    url = "https://google.com/search?q=" + search_term
                    webbrowser.get().open(url)
                    speak("Here is what I found for " + search_term + " on google")    
                    null()
                elif "open youtube" in query:
                    search_term = query.split("for")[-1]
                    search_term = search_term.replace("open youtube","").replace("search","")
                    url = "https://www.youtube.com/results?search_query=" + search_term
                    webbrowser.get().open(url)
                    speak("Here is what I found for " + search_term + "on youtube")    
                    null()
                elif there_exists(["where am i"]):
                    url = "https://www.google.com/maps/search/Where+am+I+?/"
                    webbrowser.get().open(url)
                    speak("You must be somewhere near here, as per Google maps")
                    null()
                elif there_exists(['hey','hi','hello','ok']):
                    greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
                    greet = greetings[random.randint(0,len(greetings)-1)]
                    speak(greet)
                    null()
                elif there_exists(["what is your name","what's your name","tell me your name"]):

                    if person_obj.name:
                        speak(f"My name is {jarvis.name}, {person_obj.name}") #gets users name from voice input
                    else:
                        speak(f"My name is {jarvis_obj.name}. what's your name sir?") #incase you haven't provided your name.
                    null()
                elif there_exists(["my name is"]):
                    person_name = query.split("is")[-1].strip()
                    speak("okay, i will remember that sir" + person_name)
                    person_obj.setName(person_name) # remember name in person object
                    null()
                elif there_exists(["what is my name"]):
                    speak("Your name must be " + person_obj.name)
                    null()
                elif there_exists(["your name should be"]):
                    jarvis_name = query.split("be")[-1].strip()
                    speak("okay, i will remember that my name is " + jarvis_name)
                    jarvis.setName(jarvis_name) # remember name in asis object
                    null()
                elif there_exists(["how are you","how are you doing"]):
                    speak("I'm very well, thanks for asking " + person_obj.name + "sir")
                    null()
                elif there_exists(["toss coin","flip coin"]):
                    moves=["head", "tails"]   
                    cmove=random.choice(moves)
                    speak("I chose " + cmove)
                    null()
                if there_exists(["plus","minus","multiply","divide","power","+","-","*","/"]):
                    opr = query.split()[1]

                    if opr == '+':
                        speak(int(query.split()[0]) + int(query.split()[2]))
                    elif opr == '-':
                        speak(int(query.split()[0]) - int(query.split()[2]))
                    elif opr == 'multiply' or 'x':
                        speak(int(query.split()[0]) * int(query.split()[2]))
                    elif opr == 'divide':
                        speak(int(query.split()[0]) / int(query.split()[2]))
                    elif opr == 'power':
                        speak(int(query.split()[0]) ** int(query.split()[2]))
                    else:
                        speak("Wrong Operator")
                    null()
                elif there_exists(["game","let's play a game"]):
                    voice_data = record_audio("choose among rock paper or scissor")
                    moves=["rock", "paper", "scissor"]
    
                    cmove=random.choice(moves)
                    pmove=voice_data
        

                    speak("The computer chose " + cmove)
                    speak("You chose " + pmove)
                    #speak("hi")
                    if pmove==cmove:
                        speak("the match is draw")
                    elif pmove== "rock" and cmove== "scissor":
                        speak("Player wins")
                    elif pmove== "rock" and cmove== "paper":
                        speak("Computer wins")
                    elif pmove== "paper" and cmove== "rock":
                        speak("Player wins")
                    elif pmove== "paper" and cmove== "scissor":
                        speak("Computer wins")
                    elif pmove== "scissor" and cmove== "paper":
                        speak("Player wins")
                    elif pmove== "scissor" and cmove== "rock":
                        speak("Computer wins")
                    null()
                elif there_exists(["definition of"]):
                    definition=record_audio("what do you need the definition of")
                    url=urllib.request.urlopen('https://en.wikipedia.org/wiki/'+definition)
                    soup=bs.BeautifulSoup(url,'lxml')
                    definitions=[]
                    for paragraph in soup.find_all('p'):
                        definitions.append(str(paragraph.text))
                        if definitions:
                            if definitions[0]:
                                speak('im sorry i could not find that definition, please try a web search')
                            elif definitions[1]:
                                speak('here is what i found '+definitions[1])
                            else:
                                speak ('Here is what i found '+definitions[2])
                        else:
                            speak("im sorry i could not find the definition for "+definition)
                    null()
                elif there_exists(["search for"]) and 'youtube' not in query:
                    search_term = query.split("for")[-1]
                    url = "https://google.com/search?q=" + search_term
                    webbrowser.get().open(url)
                    speak("Here is what I found for" + search_term + "on google")
                    null()
                elif there_exists(["my mail","my gmail"]):
                    url = "https://mail.google.com/mail/u/0/?tab=rm#inbox"
                    webbrowser.get().open(url)
                    null()
                elif there_exists(["calender"]):
                    url="https://calendar.google.com/calendar/u/0/r?tab=rc"
                    webbrowser.get().open(url)
                    null()
                elif there_exists(["news"]):
                    url="https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen"
                    webbrowser.get().open(url)
                    null()
                elif there_exists(["where is"]):
                    query = query.replace("where is", "")
                    location = query
                    speak("User asked to Locate")
                    speak(location)
                    webbrowser.open("https://www.google.co.in/maps/place/" + location + "")
                    null()
                elif there_exists(["open home dashboard"]):
                    url="https://portal.sinric.pro/dashboard"
                    webbrowser.get().open(url) 
                    speak("here it is.")
                    null()  

                elif "how are you" in query:
                    speak("I'm fine, glad you me that")
                    null()
                elif "i love you" in query:
                    speak("It's hard to understand")
                    null()
                elif "write a note" in query:
                    speak("What should i write, sir")
                    note = takeCommand()
                    file = open('jarvis.txt', 'w')
                    speak("Sir, Should i include date and time")
                    snfm = takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%H:%M")
                        file.write(strTime)
                        file.write(" :- ")
                        file.write(note)
                    else:
                        file.write(note)
                    null()    
                elif "show note" in query:
                    speak("Showing Notes")
                    file = open("jarvis.txt", "r")
                    print(file.read())
                    speak(file.read())
                    null()
                elif there_exists(['ask',"question"]):
                    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                    question=takeCommand()
                    app_id="QTLYH7-WKR48VLLLA"
                    client = wolframalpha.Client('QTLYH7-WKR48VLLLA')
                    res = client.query(question)
                    answer = next(res.results).text
                    speak(answer)
                    print(answer)
                    null()
                elif "day" in query:
                    tellDay()  
                    null()
                elif there_exists(["route to"]):
                    search_term = query.split("to")[-1]
                    url = "https://www.google.co.in/maps/dir/" + search_term
                    webbrowser.get().open(url)
                    speak("Here is what I found for" + search_term + "on google maps")  
                    null()
