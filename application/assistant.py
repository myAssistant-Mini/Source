
# pip install pygame       
# pip install pywhatkit
# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio : Download the wheel file from src folder of the repository and then in command prompt give proper directory and then give command: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
# pip install tkvideo


# pip install win10toast
# added notifications for at start. is listening, contact, wikipedia,time , whatsapp, email



import cv2
import requests
import speech_recognition as rec
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from founders import bhavesh, atharva, yogesh
import webbrowser
import pyautogui
import time
import smtplib
from email.message import EmailMessage
from win10toast import ToastNotifier

notify = ToastNotifier()


listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Mini:

    def __init__(self):
        self.contactList = ["bhavesh", "atharva", "yogesh",
                            "vaishu", "adika", "siddhi"]

    def talk(self, text: str):
        engine.say(text)
        engine.runAndWait()

    def hearYou(self, time=3):
        with rec.Microphone() as source:
            voice = listener.record(source, time)
            command = listener.recognize_google(voice)
            low = command.lower()
        return low

    def makeWhatsappMessage(self):

        self.talk("Whom to Send")
        friend = self.hearYou()

        self.talk("What is the message")
        message = self.hearYou(10)

        hour = datetime.datetime.now().strftime('%H')
        minute = datetime.datetime.now().strftime('%M')

        self.talk(f"Sending message to {friend}")
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Message will be sent in a minute", 'icon.ico', 20, True)

        mobile = {'bhavesh': '+919136298868',
                  'atharva': '+918097985835',  'yogesh': '+918329863550'}

        if mobile[friend] is None:
            self.talk('Sorry No Contact Found')
            return ''

        try:
            pywhatkit.sendwhatmsg(mobile[friend], message, int(
                hour), int(minute) + 1, 10, True)

        except:
            pass

    def getWeatherInformation(self):
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

        self.talk("Which City")
        city = self.hearYou()

        URL = BASE_URL + "q=" + city + "&appid=" + '33998c345736e3692ba2a0fd8a10e828'
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()

            main = data['main']
            temperature = main['temp'] - 273.15
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']

            notify.show_toast(
                "Weather Report", f'''City: {city.upper()}
Temperature: {temperature} C | Report: {report[0]['description']}
Pressure: {pressure} | Humidity: {humidity}''', 'icon.ico', 10, True) #/n doesn't work.. please don't change

            self.talk(f'Weather For City {city}')
            self.talk(f"Temperature: {temperature} degree celsius")
            self.talk(f"Weather Report: {report[0]['description']}")
            self.talk(f"Pressure: {pressure}")
            self.talk(f"Humidity: {humidity}")

        else:
            print("Sorry Could Not Understand")

    def tellInformationAboutAnything(self, person):
        answer = wikipedia.summary(person, 1)
        notify.show_toast("miniSearch :" + person,
                          answer, 'icon.ico', 15, True)
        self.talk(answer)

    def tellCreatorsInformation(self):
        try:
            self.talk("Which creator you want to explore")
            name = self.hearYou()
            # print(name)

            if 'bhavesh' in name:
                info = bhavesh.get_info()
                for details in info:
                    self.talk(f"{bhavesh.get_name()} {details}")

            elif 'atharva' in name:
                info = atharva.get_info()
                for details in info:
                    self.talk(f"{atharva.get_name()} {details}")

            elif 'yogesh' in name:
                info = yogesh.get_info()
                for details in info:
                    self.talk(f"{yogesh.get_name()} {details}")

        except:
            pass

    def introduceSelf(self):
        self.talk("Hello everyone, I am Mini, a intelligent Search Engine and a super useful voice Assistant."
                  "I try my best to automate all tasks and help you in your work")

    def takeASelfie(self):
        self.talk("Please Smile, taking a Selfie in 2 seconds")
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        if cap.isOpened():
            _, frame = cap.read()
            # cv2.imshow('s', frame)
            cap.release()
            if _ and frame is not None:
                cv2.imwrite('selfie.png', frame)

    def getAContactNumber(self):
        self.talk("Whose Contact number Do You want?")
        contactNumber = self.hearYou()

        cont = self.contactList.index(contactNumber)

        with open("contacts.txt", "r") as con:
            conts = con.readlines()
        notify.show_toast("MINI - Intelligent Search Engine",
                          f"Contact Number of {contactNumber.upper()} is " + conts[cont], 'icon.ico', 8, True)
        self.talk(f"Contact Number of {contactNumber} is " + conts[cont])

    def makeAToDoList(self):
        self.talk("Please Say your Name")
        name = self.hearYou()
        # print(f"Name : {name}")

        self.talk(
            f"So {name} what do you want to note\n\nPlease say I will Note it for you")
        notes = self.hearYou(10)

        with open("notes.txt", "w") as note:
            for tasks in notes:
                note.write(tasks)

        self.talk("Successfully noted!")

    def readMyNotes(self):
        self.talk("Please Say your Name")
        name = self.hearYou()

        # print(name)
        self.talk(f"So {name} here\'s you to do list")

        with open("notes.txt", "r") as notes:
            self.talk(notes.read())

    def inviteForAGoogleMeet(self):
        url = 'meet.google.com'
        webbrowser.open(url)
        time.sleep(8)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('down')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(10)
        pyautogui.click(190, 250)
        time.sleep(2)
        pyautogui.click(810, 450)
        time.sleep(1)
        pyautogui.write(
            'atharva.r.bhagat@gmail.com, atharvabhagat218@gmail.com, 31bhavesh.mhadse2001@gmail.com')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(1170, 800)

    def scrollInstagram(self):
        self.talk('Sure, Opening and logging you in few seconds.')
        url = "https://www.instagram.com/accounts/login/"
        webbrowser.open(url)
        time.sleep(8)
        pyautogui.click(880, 312)
        pyautogui.write('mini.assistant')
        pyautogui.click(880, 365)
        pyautogui.write('Ramnathi@23')
        pyautogui.press('enter')
        time.sleep(8)

        self.scroll()

        self.talk('What else you wish to do')
        task = self.hearYou()
        if 'music' or 'search' in task:
            time.sleep(3)
            pyautogui.click(980, 120)
            pyautogui.write('musicbay_dmce')
            time.sleep(2)
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(8)

        self.talk('What else you wish to do')
        task = self.hearYou()
        if 'show' in task:
            pyautogui.click(430, 120)
            time.sleep(3)
            pyautogui.click(1210, 250)
            time.sleep(3)
            self.talk('What a wonderful profile')

    def scroll(self):
        for i in range(10):
            pyautogui.press('down')
        self.talk('Do you want to like this post')
        like = self.hearYou()
        if 'yes' in like:
            pyautogui.doubleClick(720, 380)
            time.sleep(3)
            self.talk('Do you want to keep scrolling')
            like = self.hearYou()
            if 'yes' in like:
                self.scroll()
            else:
                return

    def sendAnEmail(self):
        self.talk("Whom to Send")
        friend = self.hearYou()
        # print(friend)

        self.talk("What is the subject")
        subject = self.hearYou(5)

        self.talk("What is the message")
        message = self.hearYou(5)

        emails = {"atharva": 'atharva.r.bhagat@gmail.com',
                  "bhavesh": 'bhaveshmhadse9@gmail.com',
                  "yogesh": 'yogeshvghate@gmail.com',
                  "creators": 'atharva.r.bhagat@gmail.com, bhaveshmhadse9@gmail.com, yogeshvghate@gmail.com'}

        receiver = emails[friend]
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Successfully Sent Email to :" + receiver, 'icon.ico', 5, True)
        self.talk(f'Successfully sent your email to {receiver}')

        self.send(subject, receiver, message)

    def send(self, subject, friend, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('intelligent.mini.search@gmail.com', 'Ramnathi@23')
        email = EmailMessage()
        email['From'] = 'intelligent.mini.search@gmail.com'
        email['To'] = friend
        email['Subject'] = subject
        email.set_content(message)
        server.send_message(email)

    def mini(self):
        try:
            task = self.hearYou()

            if 'hello mini' in task:
                print('...')
                self.run_mini()

            elif 'stop' in task:
                print('...')
                self.talk('Thank You. Have a nice day.')
                return 'stop'

            else:
                self.mini()
        except:
            pass

    def run_mini(self):
        try:
            notify.show_toast("MINI - Intelligent Search Engine",
                              "Mini is Listening...", 'icon.ico', 6, True)
            self.talk("Mini is Listening.. How Can I help You?")

            task = self.hearYou()
            # print(task)
            task = task.replace('mini', "")

            if 'intro' in task:
                self.introduceSelf()

            elif 'play' in task:
                song = task.replace('play', "")
                self.talk(f"playing {song}")
                pywhatkit.playonyt(song)

            elif 'contact' in task:
                self.getAContactNumber()

            elif 'time' in task:
                time = datetime.datetime.now().strftime('%I: %M %p')
                notify.show_toast("MINI - Intelligent Search Engine",
                                  "Current time is " + time, 'icon.ico', 6, True)
                self.talk("Current time is " + time)

            elif 'date' in task:
                date = datetime.date.today()
                self.talk(f"Today's Date is {date}")

            elif 'who' in task:
                person = task.replace('who is', "")
                self.tellInformationAboutAnything(person)

            elif 'selfie' in task:
                self.takeASelfie()

            elif 'read' in task:
                self.readMyNotes()

            elif 'note' in task:
                self.makeAToDoList()

            elif 'do' in task:
                littlemini = Mini()
                tasks = littlemini.__dir__()
                i = 0
                for allthetasks in tasks:
                    if i == 12:
                        break
                    if(allthetasks.startswith('__')):
                        continue
                    self.talk(f"I can {allthetasks}")
                    i += 1

            elif 'weather' in task:
                self.getWeatherInformation()

            elif 'what' in task:
                person = task.replace('what is', "")
                self.tellInformationAboutAnything(person)

            elif 'where' in task:
                person = task.replace('where is', "")
                self.tellInformationAboutAnything(person)

            elif 'creator' in task:
                self.tellCreatorsInformation()

            elif 'send a message' in task:
                self.makeWhatsappMessage()

            elif 'browse' in task:
                task = task.replace("browse ", "")
                webbrowser.open(f"www.{task}.com")

            elif 'invite' in task:
                self.talk(
                    'Creating a meeting and inviting your friends in a minute')
                self.inviteForAGoogleMeet()

            elif 'instagram' in task:
                self.scrollInstagram()

            elif 'email' in task:
                self.sendAnEmail()

            elif 'engine' in task:
                webbrowser.open('http://127.0.0.1:8000/')

            else:
                self.talk('Sorry Could not Understand')
        except:
            pass
