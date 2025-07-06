import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "yourkey"


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key="your key")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"your key")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            #Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        #let open ai handle request
        output = aiProcess(c)
        speak(ouput)
        


if __name__ == "__main__":
    speak("hey initializing jarvis")
    while True:
        # listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        # recognize speech using Sphinx

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening!...")
                audio = r.listen(source, timeout =10,phrase_time_limit=5)
            
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("hello there how have u been do u need help with anything")
            #listen for command 
            with sr.Microphone() as source:
                print("jarvis active!...")
                audio = r.listen(source)
                command= r.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
    
