import pyttsx3
import datetime
import gtts
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)                         # print voices 
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good morning Sir !")
    elif hour>=12 and hour<18:
            speak("Good afternoon Sir ! ")
    else :
            speak("Good Evening Sir!")

    speak ("I am  Zira, your virtual assistant Please tell me how may I help u ")
    print ("I am  Zira, your virtual assistant Please tell me how may I help u ")

def takeCommand():
    #it takes microphone inpt from user and returns string output 
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        #print(e)
        speak("Say that again Please")
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    speak("Configuring the system database Checking the vital issues .                  I am  online now")
    print("Configuring the system database Checking the vital issues .                  I am  online now")
    wishme()
    while True:
        query= takeCommand().lower()

        if 'wikipedia'  in query:
            speak('Searching wikipedia ')
            query=query.replace("Wikipedia: ","")
            results= wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "how are you" in query:
            speak(" I am Fine ,Sir")


        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music " in query:
            music_dir="G:\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        elif "the time " in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath="C:\\Users\\Debankan Sarkar\\Desktop\\Visual Studio Code"
            os.startfile(codePath)

        elif "play spotify" in query :
            spoti="C:\\Users\\Debankan Sarkar\\Desktop\\Spotify"
            os.startfile(spoti)

        elif "quit" in query :
            speak(" Have a Great Day ,Sir")
            print(" Have a Great Day ,Sir")
            endpa="C:\\Users\\Debankan Sarkar\\Desktop\\Visual Studio Code"
            exit()
