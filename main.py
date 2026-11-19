import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

r = sr.Recognizer()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open google" in c. lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():    
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():    
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():    
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)         


if __name__=="__main__":
    speak("Initializing jarvis...")
    while True:
        #Listen for the wake word "Jarvis"
         # obtain audio from the microphone 
        r = sr.Recognizer()
        
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak("Ya")
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout=3, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.WaitTimeoutError:
            pass
        except sr. UnknownValueError:
            print("Samajh nahi aaya, dobara bolo")
        except Exception as e:
            print("Error:",e)
               
            
            