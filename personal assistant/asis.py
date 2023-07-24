import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("Shashank :" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand come again")
        return "None"
    return query


if __name__ == '__main__':

    speak("Your personal assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'who are you' in query:
            speak("I am Reema your personal assistance developed by Shashank Vengala")
        elif 'tell about yourself' in query:
            speak("Iam a piece of software allowed to perform routine tasks by speaking. Iam a combination many forms of artificial intelligence and machine learning to listen to and respond to human commands")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open kaggle' in query:
            speak("opening kaggle")
            webbrowser.open("kaggle.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            """loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"""
            """os.startfile(loc)"""
            webbrowser.open("whatsapp.com")
        elif 'play music' in query:
            speak("opening music")
            loc = "C:\\Users\\Shashank\\Music"
            os.startfile(loc)
        elif 'open hotstar' in query:
            speak("opening hotstar")
            webbrowser.open("hotstar.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D:\\")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C:\\")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E:\\")
        elif 'sleep' in query:
            exit(0)