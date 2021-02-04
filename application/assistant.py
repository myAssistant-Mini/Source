
# pip install pywhatkit
# pip install SpeechRecognition
# pip install PyAudio : Download the weheel file from src folder of the repository and then in command prompt give proper directory and then give command: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl


# Normal Working of Mini
# Oop madhe aapan data lapavto user pasun ani fkt tyala functionality deto :)
# mini.py ch run honar, aplyala fkt ikde je kai aahet te changes marave lagnr :)


from pyttsx3 import engine
import speech_recognition as rec
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Mini:

    def __init__(self):
        self.name = 10

    def talk(self, text):
        engine.say(text)
        engine.runAndWait()

    def mini(self):
        try:

            self.talk("Mini is Listening. What Can I do for you")

            with rec.Microphone() as source:
                voice = listener.record(source, 5)
                command = listener.recognize_google(voice)
                task = command.lower()

            if 'hello mini' in command:
                task = task.replace('hello mini', "")
                return task

            else:
                return 'invalid'
        except:
            pass

    def whatsapp(self):
        m = 0
        self.talk("Whom to Send")
        with rec.Microphone() as source:
            voice = listener.record(source, 3)
            contact = listener.recognize_google(voice)
            friend = contact.lower()

        self.talk("What is the message")

        with rec.Microphone() as source:
            voice = listener.listen(source)
            message = listener.recognize_google(voice)

        hour = datetime.datetime.now().strftime('%H')
        minute = datetime.datetime.now().strftime('%M')

        self.talk(f"Sending message to {friend}")

        mobile = {'bhavesh': '+919136298868', 'atharva': '+918097985835',
                  'yogesh': '+91918329863550', 'mom': '+919920130735'}

        if(mobile[friend] == None):
            self.talk('Sorry No Contact Found')
            return ''

        try:
            pywhatkit.sendwhatmsg(mobile[friend], message, int(
                hour), int(minute) + 1, 10, True)

        except:
            pass

    def run_mini(self):
        task = self.mini()
        try:
            self.talk("How Can I help You?")
            with rec.Microphone() as source:
                voice = listener.record(source, 5)
                command = listener.recognize_google(voice)
                task = command.lower()

            if 'play' in task:
                song = task.replace('play', "")
                self.talk(f"playing {song}")
                pywhatkit.playonyt(song)

            elif 'time' in task:
                time = datetime.datetime.now().strftime('%I: %M %p')
                self.talk("Current time is " + time)

            elif 'who' in task:
                person = task.replace('mini who is', "")
                answer = wikipedia.summary(person, 1)
                (answer)
                self.talk(answer)

            elif 'stop' in task:
                return 'stop'

            elif 'send a message' in task:
                self.whatsapp()

            else:
                self.talk('Sorry Could not Understand')
        except:
            pass


# Fkt Functionalitis add krayche!!!!  :)
