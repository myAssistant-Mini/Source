
# pip install pywhatkit
# pip install SpeechRecognition
# pip install PyAudio : Download the weheel file from src folder of the repository and then in command prompt give proper directory and then give command: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl 


import speech_recognition as rec
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def mini():
    try:
        talk("Mini is Listening. What Can I do for you")
        with rec.Microphone() as source:
            voice = listener.record(source, 5)
            command = listener.recognize_google(voice)
            task = command.lower()
        if 'hello mini' in command:
            task = task.replace("hello mini", "")
            # print(task)
            return task
        else:
            return 'invalid'
    except:
        pass



def whatsapp():
    talk("Whom to Send")
    with rec.Microphone() as source:
        voice = listener.record(source, 3)
        contact = listener.recognize_google(voice)
        friend = contact.lower()
    talk("What is the message")
    with rec.Microphone() as source:
        voice = listener.listen(source)
        message = listener.recognize_google(voice)
    hour = datetime.datetime.now().strftime('%H')
    minute = datetime.datetime.now().strftime('%M')
    talk(f"Sending message to {friend}")
    mobile = ['+918097985835', '+919136298868', '+91918329863550', '+919920130735']
    if 'myself' in friend:
        m = 0
    elif 'bhavesh' in friend:
        m = 1
    elif 'yogesh' in friend:
        m = 2
    elif 'mom' or 'mum' in friend:
        m = 3
    else:
        talk('Sorry No Contact Found')
    try:
        pywhatkit.sendwhatmsg(mobile[m], message, int(hour), int(minute) + 1, 10, True)
    except:
        pass


def run_mini():
    task = mini()
    try:
        if 'play' in task:
            song = task.replace('play', "")
            talk(f"playing {song}")
            pywhatkit.playonyt(song)
        elif 'time' in task:
            time = datetime.datetime.now().strftime('%I: %M %p')
            talk("Current time is " + time)
        elif 'who' in task:
            person = task.replace('mini who is', "")
            answer = wikipedia.summary(person, 1)
            print(answer)
            talk(answer)
        elif 'send a message' in task:
            whatsapp()
        else:
            talk('Sorry Could not Understand')
    except:
        pass
    
    run_mini()
