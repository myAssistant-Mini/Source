
# pip install pywhatkit
# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio : Download the wheel file from src folder of the repository and then in command prompt give proper directory and then give command: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl

#IMPORTANT pip install pyowm 

# Changed control flow because it was inappropriate. 'Hello mini' input was of no meaning due to that flow. 
# Now mini.py calls mini() -> if user speaks Hello Mini -> run_mini() and asks for what he wants -> executes task -> if user says nothing then back to Mini is Listening
#                          -> if user says stop -> EXIT
#             -> if user says nothing (which we will have to while explaining) -> it will recursivelyy say Mini is listening after each 10 sec until says Stop or Hello mini 
# Added current weather, today's date, what is and where is for wiki summary, added self intro, explore creators and miscellaneous changes like time.sleep()

import requests
import speech_recognition as rec
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

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

    def whatsapp(self):
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

        mobile = {'bhavesh': '+919136298868', 'atharva': '+918097985835',  'yogesh': '+918329863550'}

        if mobile[friend] is None:
            self.talk('Sorry No Contact Found')
            return ''

        try:
            pywhatkit.sendwhatmsg(mobile[friend], message, int(hour), int(minute) + 1, 10, True)
        except:
            pass

    def weather(self):
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

        self.talk("Which City")
        with rec.Microphone() as source:
            voice = listener.record(source, 3)
            city = listener.recognize_google(voice)

        URL = BASE_URL + "q=" + city + "&appid=" + '33998c345736e3692ba2a0fd8a10e828'
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            main = data['main']
            temperature = main['temp'] - 273.15
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']

            print(f'City: {city}')
            self.talk(f'Weather For City {city}')
            print(f"Temperature: {temperature} C")
            self.talk(f"Temperature: {temperature} degree celsius")
            print(f"Weather Report: {report[0]['description']}")
            self.talk(f"Weather Report: {report[0]['description']}")
            print(f"Pressure: {pressure}")
            self.talk(f"Pressure: {pressure}")
            print(f"Humidity: {humidity}")
            self.talk(f"Humidity: {humidity}")

        else:
            print("Sorry Could Not Understand")

    def info(self, person):
        answer = wikipedia.summary(person, 1)
        print(answer)
        self.talk(answer)

    def creators(self):
        try:
            self.talk("Which creator you want to explore")
            with rec.Microphone() as source:
                voice = listener.record(source, 3)
                command = listener.recognize_google(voice)
                name = command.lower()

                self.talk(f'Here are some cool facts about {name}')
                self.talk(f'{name} is a student of Datta Meghe College of Engineering.')
                self.talk(f'{name} loves to play cricket and hang out with his friends.')
                self.talk(f'{name} took great efforts to create me.')
            time.sleep(5)
        except:
            pass

    def intro(self):
        self.talk("Hello everyone, I am Mini, a intelligent Search Engine and a super useful voice Assistant."
                  "I try my best to automate all tasks and help you in your work")

    def mini(self):
        try:
            self.talk("Mini is Listening")
            with rec.Microphone() as source:
                voice = listener.record(source, 5)
                command = listener.recognize_google(voice)
                task = command.lower()

            if 'hello mini' in task:
                self.run_mini()
            elif 'stop' in task:
                self.talk('Thank You. Have a nice day.')
                return 'stop'
            else:
                time.sleep(10)
                self.mini()
        except:
            pass

    def run_mini(self):
        try:
            self.talk("How Can I help You?")
            with rec.Microphone() as source:
                voice = listener.record(source, 5)
                command = listener.recognize_google(voice)
                task = command.lower()

            if 'intro' in task:
                self.intro()

            elif 'play' in task:
                song = task.replace('play', "")
                self.talk(f"playing {song}")
                pywhatkit.playonyt(song)

            elif 'time' in task:
                time = datetime.datetime.now().strftime('%I: %M %p')
                self.talk("Current time is " + time)

            elif 'date' in task:
                date = datetime.date.today()
                self.talk(f"Today's Date is {date}")

            elif 'who' in task:
                person = task.replace('who is', "")
                self.info(person)

            elif 'what' in task:
                person = task.replace('what is', "")
                self.info(person)

            elif 'where' in task:
                person = task.replace('where is', "")
                self.info(person)

            elif 'explore' in task:
                self.creators()

            elif 'send a message' in task:
                self.whatsapp()

            elif 'weather' in task:
                self.weather()

            else:
                self.talk('Sorry Could not Understand')
        except:
            pass
        finally:
            time.sleep(3)
