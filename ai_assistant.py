import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
    

engine = pyttsx3.init('sapi5')

# Say a text
# engine.say("I will speak this text")

# # Adjust voice properties (rate, volume, voice)
# engine.setProperty('rate', 225)  # Set the speaking rate
# engine.setProperty('volume', 1.0)  # Set the volume level (between 0 and 1)

# Change the voice (optional)
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
# engine.setProperty('voice', voices[1].id)  # Use the second voice (female)
# function recive the text and execute
def speak(audio):
    engine.say(audio)
    engine.runAndWait()      # Run the engine
def wishMe():
    # hour = int(datetime.datetime.now().hour)
    # if hour > 5 and hour < 12:
    #     speak('Good morning, sir')
    # elif hour > 12 and hour < 18:
    #     speak('Good noon, sir')
    # elif hour > 18 and hour < 21:
    #     speak('Good evening, sir')
    # else:
    #     speak('its night. sir')
    speak('hi razim. How may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What's your command")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio, language = 'en-bd')
        print(f'user said : {query}')

    except Exception as e:
        print('try to say again')
        return 'None'
    return query
def sendEmail(to, content):
    pass
#pass the text 
if __name__ == '__main__':
    wishMe()
    
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching..')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 2)
            speak(f'in wikipedia{result}')
        elif "open youtube" in query:
            webbrowser.open('youtube.com')
        elif "open facebook" in query:
            webbrowser.open('facebook.com')
        elif "open google" in query:
            webbrowser.open('google.com')
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the time is {strtime}")
        elif "open vs code" in query:
            codepath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open whatsapp" in query:
            codepath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        # elif 'email to razim' in query:
        #     try:
        #         speak('what do you want to say')
        #         content = takeCommand()
        #         to = ashraful180067@diit.edu.bd
        #         sendEmail(to, content)
        #         speak('send')
        #     except Exception as e:
        #         print(e)
        #         speak("sorry razim, im unable to send this mail")
        elif 'shut' in query:
            exit()
        
