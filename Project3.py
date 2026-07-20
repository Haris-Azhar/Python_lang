import speech_recognition as sr
import webbrowser
import pyttsx3 as pt

recogniser = sr.Recognizer()
r = recogniser
engine = pt.init()
def speak(text):
    engine.say(text)
    engine.runAndWait() 

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com") 
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    


speak("Initialize Jarvis...")
while True:
    r = sr.Recognizer()
    print("recognize....")

    try:
        with sr.Microphone() as source:
            print("Lisning...")
            audio = r.listen(source,timeout=2,phrase_time_limit=1)
        word = r.recognize_google(audio)
        if word.lower() == "jarvis":
            speak("Ya")
            with sr.Microphone() as source:
                print("Jarvis activate....")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                process_command(command)

    except Exception as e:
        print(e)
        break


       








