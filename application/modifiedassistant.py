
# pip install pygame
# pip install pywhatkit
# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio : Download the wheel file from src folder of the repository and then in command prompt give proper directory and then give command: pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
# pip install tkvideo
# pip install win10toast

# pip install PyPDF2
# added funzone , audiobook


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
import PyPDF2

notify = ToastNotifier()
listener = rec.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


class Mini:
    def __init__(self):
        self.contactList = ["bhavesh", "atharva", "yogesh",
                            "vaishu", "adika", "siddhi"]

        self.taskDictionary = {'intro': self.introduceSelf, 'contact': self.getAContactNumber, 'time': self.tellTime,
                               'date': self.tellDate, 'selfie': self.takeASelfie, 'novel': self.readAudioBook,
                               'read': self.readMyNotes, 'note': self.makeAToDoList, 'do': self.tasksMiniCanPerform,
                               'weather': self.getWeatherInformation, 'instagram': self.scrollInstagram, 'email': self.sendAnEmail,
                               'creator': self.tellCreatorsInformation, 'message': self.makeWhatsappMessage, 'news': self.readNews,
                               'invite': self.googleMeet, 'engine': self.miniEngine, 'fun': self.miniFun}

        self.taskArray = ['intro', 'contact', 'time', 'date', 'selfie', 'novel', 'read', 'note', 'do', 'weather',
                          'instagram', 'email', 'creator', 'message', 'news', 'invite', 'play', 'browse', 'who', 'what', 'where']

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
            Pressure: {pressure} | Humidity: {humidity}''', 'icon.ico', 10, True)

            self.talk(f'Weather For City {city}')
            self.talk(f"Temperature: {temperature} degree celsius")
            self.talk(f"Weather Report: {report[0]['description']}")
            self.talk(f"Pressure: {pressure}")
            self.talk(f"Humidity: {humidity}")

        else:
            print("Sorry Could Not Understand")

    def tellInformationAboutAnything(self, person):
        answer = wikipedia.summary(person, 1)
        notify.show_toast("MiniSearch :" + person.upper,
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

    def readNews(self):
        url = "http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=1d500e94abb640a8be6d8330be36754b"
        news = requests.get(url).json()
        articles = news["articles"]

        result = []

        for a in articles:
            result.append(a["title"])

        for i in range(5):
            time.sleep(3)
            Headline = result[i]
            notify.show_toast("MINI - Trending News",
                              Headline, 'icon.ico', 5, True)
            self.talk(Headline)
        self.talk('These were the top headlines powered by Mini Search Engine')

    def readANovel(self):
        book = open('novel.pdf', 'rb')
        read = PyPDF2.PdfFileReader(book)
        pages = read.numPages
        for num in range(4, pages):
            page = read.getPage(num)
            text = page.extractText()
            self.talk(text)

    def readAudioBook(self):
        notify.show_toast("myAssistant MINI",
                          "Currently Reading: Murder on the Orient Express - Agatha Christie", 'icon.ico', 35, True)
        self.talk('Reading your favorite novel - Murder on the Orient Express')
        self.readANovel()

    def tellTime(self):
        time = datetime.datetime.now().strftime('%I: %M %p')
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Current time is " + time, 'icon.ico', 6, True)
        self.talk("Current time is " + time)

    def tellDate(self):
        date = datetime.date.today()
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Today's date: ", date, 'icon.ico', 6, True)
        self.talk(f"Today's Date is {date}")

    def tasksMiniCanPerform(self):
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

    def googleMeet(self):
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Creating Google Meet Link and sending Invitation", 'icon.ico', 8, True)
        self.talk('Creating a meeting and inviting your friends in a minute')
        self.inviteForAGoogleMeet()

    def miniEngine(self):
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Launching Search Engine", 'icon.ico', 6, True)
        webbrowser.open('http://127.0.0.1:8000/')

    def miniFun(self):
        play = FunZone()
        notify.show_toast("MINI Intelligent Search Engine",
                          "Mini Fun Zone has started...", 'icon.ico', 6, True)
        self.talk("You have Entered MINI Fun Zone")
        while True:
            run = play.fun()
            if run == 'stop':
                break

    def specialTask(self, task, command):
        if command == 'play':
            song = task.replace('play', "")
            self.talk(f"playing {song}")
            pywhatkit.playonyt(song)
            return 0
        task = task.replace("browse", "")
        webbrowser.open(f"www.{task}.com")

    def specialTask2(self, task: str, command):
        person = task.replace(f'{command} is', "")
        self.tellInformationAboutAnything(person)

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

            task = task.replace('mini', "")

            for variousTasks in self.taskArray:
                if variousTasks in task:
                    if variousTasks == 'play' or variousTasks == 'browse':
                        self.specialTask(task, variousTasks)
                        return 0

                    if variousTasks == 'who' or variousTasks == 'what' or variousTasks == 'where':
                        self.specialTask2(task, variousTasks)
                        return 0

                    self.taskDictionary[variousTasks]()
                    return 0

            self.talk("Sorry reeee Samjha Nai")
        except:
            pass


fun = Mini()


class FunZone:
    def search(self):
        fun.talk(
            'Such a stupid question. You should have known about this. Go increase your general knowledge')

    def playASong(self):
        fun.talk('I am bored right now. Go Hang out with your friends')

    def whatTime(self):
        fun.talk('See your watch. Dont disturb me for small things.')

    def creator(self):
        fun.talk('Some nerds like you')

    def boyfriend(self):
        fun.talk('Its none of your business. But yes, I am not single like you are')

    def letsPlay(self):
        fun.talk('I dont have time to play with humans.Get a life.')

    def joke(self):
        fun.talk(
            'Open your selfie cam or go stand in front of a mirror. You will see the funniest joke in this world.')

    def memory(self):
        fun.talk(
            'Do you remember? One day you proposed your crush and you got friendzoned. I laughed so much that day. lol')

    def fun(self):

        try:
            task = fun.hearYou()

            if 'hello mini' in task:
                print('...')
                self.runFunZone()

            elif 'exit' in task:
                print('...')
                notify.show_toast("MINI FunZone Exited",
                                  "Entering into Mini Intelligent Search", 'icon.ico', 4, True)
                fun.talk('Exiting Fun Zone.')
                return 'stop'

            else:
                self.fun()
        except:
            pass

    def runFunZone(self):
        try:
            notify.show_toast("MINI FunZone",
                              "Mini is Waiting...", 'icon.ico', 6, True)
            fun.talk("I am waiting.. say fast")

            task = fun.hearYou()
            print(task)
            task = task.replace('mini', "")

            if 'time' in task:
                self.whatTime()

            elif 'joke' in task:
                self.joke()

            elif 'song' in task:
                self.playASong()

            elif 'created' in task:
                self.creator()

            elif 'play' in task:
                self.letsPlay()

            elif 'single' in task:
                self.boyfriend()

            elif 'memory' in task:
                self.memory()

            elif 'who' in task:
                self.search()

            else:
                fun.talk('I am busy. Go do it yourself')
        except:
            pass
