from modules import *
import googletrans
import gtts
import playsound

notify = ToastNotifier()
listener = rec.Recognizer()
translator = googletrans.Translator()
enginehere = pyttsx3.init()
voices = enginehere.getProperty('voices')
enginehere.setProperty('voice', voices[1].id)


class Mini:
    def __init__(self):
        self.contactList = ["bhavesh", "atharva", "yogesh",
                            "vaishu", "adika", "siddhi", "rahul"]

        self.taskDictionary = {'intro': self.introduceSelf, 'contact': self.getAContactNumber, 'time': self.tellTime,
                               'date': self.tellDate, 'selfie': self.takeASelfie, 'novel': self.readANovel,
                               'read': self.readMyNotes, 'note': self.makeAToDoList, 'do': self.tasksMiniCanPerform,
                               'weather': self.getWeatherInformation, 'instagram': self.scrollInstagram, 'email': self.sendAnEmail,
                               'creator': self.tellCreatorsInformation, 'message': self.makeWhatsappMessage, 'news': self.readNews,
                               'meeting': self.inviteForAGoogleMeet, 'engine': self.launchMiniSearchEngine, 'fun': self.startFunZone}

        self.taskArray = ['stop', 'intro', 'contact', 'time', 'date', 'selfie', 'novel', 'read', 'note', 'do', 'weather', 'fun', 'meeting',
                          'instagram', 'email', 'engine', 'creator', 'message', 'news', 'call', 'play', 'browse', 'who', 'what', 'where']

    def talk(self, text: str):
        enginehere.say(text)
        enginehere.runAndWait()

    def hearYou(self, time=3):

        try:
            with rec.Microphone() as source:
                voice = listener.record(source, time)
                command = listener.recognize_google(
                    voice, language='mr-IN')
                translated = translator.translate(
                    command, dest='en', src='mr')
                low = translated.text.lower()
                print(low)
            return low
        except:
            pass

    def makeWhatsappMessage(self):

        playsound.playsound("hindi_sounds/Whom to Send.mp3")
        friend = self.hearYou()

        playsound.playsound("hindi_sounds/What is the message.mp3")
        message = self.hearYou(5)

        hour = datetime.datetime.now().strftime('%H')
        minute = datetime.datetime.now().strftime('%M')

        playsound.playsound("hindi_sounds/Sending message to.mp3")
        self.talk(friend)
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Message will be sent in a minute", 'icon.ico', 20, True)

        mobile = {'bhavesh': '+919136298868', 'me': '+918097985835',
                  'yogesh': '+918329863550', 'rahul': '+919930656344'}

        if mobile[friend] is None:
            playsound.playsound('hindi_sounds/Sorry No Contact Found.mp3')
            return ''

        try:
            pywhatkit.sendwhatmsg(mobile[friend], message, int(
                hour), int(minute) + 1, 10, True)

        except:
            pass

    def summarizeWikipedia(self, task, command):
        task = task.replace(f'{command} is', "")
        person = task.replace('are', "")
        try:
            answer = wikipedia.summary(person, 1)
            notify.show_toast(
                f"MiniSearch :{person.upper()}", answer, 'icon.ico', 15, True)
            self.talk(answer)
        except:
            playsound.playsound(
                'hindi_sounds/Sorry Could not understand.mp3')

    def getWeatherInformation(self):
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

        playsound.playsound("hindi_sounds/Which city.mp3")
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

            self.talk(f'{city}')
            playsound.playsound('hindi_sounds/Weather For City.mp3')

            playsound.playsound('hindi_sounds/Temperature.mp3')
            self.talk(f"{temperature} degree celsius")
            playsound.playsound('hindi_sounds/Weather Report.mp3')
            self.talk(f"{report[0]['description']}")
            playsound.playsound('hindi_sounds/Pressure.mp3')
            self.talk(f"{pressure}")
            playsound.playsound('hindi_sounds/Humidity.mp3')
            self.talk(f"{humidity}")

        else:
            playsound.playsound(
                "hindi_sounds/Sorry Could Not Understand.mp3")

    def tellCreatorsInformation(self):
        try:
            playsound.playsound(
                "hindi_sounds/Which creator do you want to know.mp3")
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
        playsound.playsound(
            "hindi_sounds/Hello everyone, I am Mini . A intelligent Search Engine and a super useful voice Assistant..mp3")

    def takeASelfie(self):
        playsound.playsound(
            "hindi_sounds/Please Smile, I am taking a Selfie in 2 seconds.mp3")
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
        playsound.playsound(
            "hindi_sounds/Whose Contact number Do You want, Tell his name.mp3")
        contactNumber = self.hearYou()

        cont = self.contactList.index(contactNumber)

        with open("contacts.txt", "r") as con:
            conts = con.readlines()
        notify.show_toast("MINI - Intelligent Search Engine",
                          f"Contact Number of {contactNumber.upper()} is " + conts[cont], 'icon.ico', 8, True)
        self.talk(f"Contact Number of {contactNumber} " + conts[cont])

    def makeAToDoList(self):
        playsound.playsound(
            "hindi_sounds/Please Say your Name.mp3")
        name = self.hearYou()
        # print(f"Name : {name}")

        playsound.playsound(
            "hindi_sounds/what do you want to note. Please say. I will Note it for you.mp3")
        notes = self.hearYou(10)

        with open("notes.txt", "w") as note:
            for tasks in notes:
                note.write(tasks)

        playsound.playsound(
            "hindi_sounds/Successfully noted.mp3")

    def readMyNotes(self):
        playsound.playsound(
            "hindi_sounds/Please Say your Name.mp3")
        name = self.hearYou()

        # print(name)
        self.talk(name)
        playsound.playsound(
            "hindi_sounds/here is your list.mp3")

        with open("notes.txt", "r") as notes:
            self.talk(notes.read())

    def inviteForAGoogleMeet(self):
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Creating Google Meet Link and sending Invitation", 'icon.ico', 8, True)
        playsound.playsound(
            "hindi_sounds/Starting a call and inviting your friends in a minute.mp3")
        url = 'meet.google.com'
        webbrowser.open(url)
        time.sleep(13)
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
            'atharva.r.bhagat@gmail.com, 31bhavesh.mhadse2001@gmail.com , yogeshvghate@gmail.com , rahulprajapati3060@gmail.com')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(1170, 800)
        playsound.playsound(
            'hindi_sounds/Invitation sent to your colleagues. Do you want to keep your mic and camera on.mp3')
        vid = self.hearYou()
        if vid == 'no':
            pyautogui.click(1045, 975)
            time.sleep(2)
            pyautogui.click(870, 975)

    def scrollInstagram(self):
        playsound.playsound(
            'hindi_sounds/Sure, logging you in few seconds.mp3')
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

        playsound.playsound(
            "hindi_sounds/What else you wish to do.mp3")
        task = self.hearYou()
        if 'music' or 'search' in task:
            time.sleep(3)
            pyautogui.click(980, 120)
            pyautogui.write('musicbay_dmce')
            time.sleep(2)
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(8)

        playsound.playsound(
            "hindi_sounds/What else you wish to do.mp3")
        task = self.hearYou()
        if 'show' in task:
            pyautogui.click(430, 120)
            time.sleep(3)
            pyautogui.click(1210, 250)
            time.sleep(3)
            self.talk('What a wonderful profile')

    def sendAnEmail(self):
        playsound.playsound(
            "hindi_sounds/Whom to Send.mp3")
        friend = self.hearYou()
        # print(friend)

        playsound.playsound(
            "hindi_sounds/What is the subject.mp3")
        subject = self.hearYou(5)

        playsound.playsound(
            "hindi_sounds/What is the message.mp3")
        message = self.hearYou(5)

        emails = {"atharva": 'atharva.r.bhagat@gmail.com',
                  "bhavesh": 'bhaveshmhadse9@gmail.com',
                  "yogesh": 'yogeshvghate@gmail.com',
                  "creators": 'atharva.r.bhagat@gmail.com, bhaveshmhadse9@gmail.com, yogeshvghate@gmail.com , rahulprajapati3060@gmail.com'}

        receiver = emails[friend]
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Successfully Sent Email to :" + receiver, 'icon.ico', 5, True)
        playsound.playsound(
            "hindi_sounds/Successfully sent your email.mp3")

        self.send(subject, receiver, message)

    def readNews(self):
        url = "http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=1d500e94abb640a8be6d8330be36754b"
        news = requests.get(url).json()
        articles = news["articles"]

        result = []

        for a in articles:
            result.append(a["title"])

        for i in range(5):
            time.sleep(1)
            Headline = result[i]
            notify.show_toast("MINI - Trending News",
                              Headline, 'icon.ico', 5, True)
            self.talk(Headline)
        playsound.playsound(
            "hindi_sounds/These were the breaking news searched via Mini Search Engine.mp3")

    def readANovel(self):
        notify.show_toast("myAssistant MINI",
                          "Currently Reading: Murder on the Orient Express - Agatha Christie", 'icon.ico', 35, True)
        playsound.playsound(
            'hindi_sounds/Starting to read your favorite book.mp3')
        self.talk('Murder on the Orient Express')
        book = open('novel.pdf', 'rb')
        read = PyPDF2.PdfFileReader(book)
        pages = read.numPages
        for num in range(4, 5):
            page = read.getPage(num)
            text = page.extractText()
            self.talk(text)

    def tellTime(self):
        time = datetime.datetime.now().strftime('%I: %M %p')
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Current time is " + time, 'icon.ico', 6, True)
        playsound.playsound(
            'hindi_sounds/Current time is.mp3')
        self.talk(time)

    def tellDate(self):
        date = datetime.date.today()
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Today's date: ", date, 'icon.ico', 6, True)
        playsound.playsound(
            "hindi_sounds/Today's Date is.mp3")

    def playYouTubeVideos(self, task):
        song = task.replace('play', "")
        self.talk(f"playing {song}")
        pywhatkit.playonyt(song)

    def launchMiniSearchEngine(self):
        notify.show_toast("MINI - Intelligent Search Engine",
                          "Launching Search Engine", 'icon.ico', 6, True)
        webbrowser.open('http://127.0.0.1:8000/')

    def startFunZone(self):
        play = FunZone()
        notify.show_toast("MINI Intelligent Search Engine",
                          "Mini Fun Zone has started...", 'icon.ico', 6, True)
        playsound.playsound(
            'hindi_sounds/You have Entered MINI Fun Zone.mp3')
        while True:
            run = play.fun()
            if run == 'stop':
                break

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

    def scroll(self):
        for i in range(10):
            pyautogui.press('down')
        playsound.playsound(
            'hindi_sounds/Do you like this post.mp3')
        like = self.hearYou()
        if 'yes' in like:
            pyautogui.doubleClick(720, 380)
            time.sleep(3)
            playsound.playsound(
                'hindi_sounds/Do you want to keep scrolling.mp3')
            like = self.hearYou()
            if 'yes' in like:
                self.scroll()
            else:
                return

    def browseOnWeb(self, task, command):
        if command == 'play':
            song = task.replace('play', "")
            self.talk(f"playing {song}")
            pywhatkit.playonyt(song)
            return 0
        task = task.replace("browse ", "")
        webbrowser.open(f"www.{task}.com")

    def tasksMiniCanPerform(self):
        littlemini = Mini()
        tasks = littlemini.__dir__()
        i = 0
        for allthetasks in tasks:
            if i == 21:
                break
            if allthetasks.startswith('__') or allthetasks == 'contactList' or allthetasks == 'taskArray' or allthetasks == 'taskDictionary':
                continue
            self.talk(f"I can {allthetasks}")
            i += 1

    def mini(self):
        try:
            task = self.hearYou()

            if 'hello mini' in task:
                print('...')
                return self.run_mini()

            else:
                self.mini()
        except:
            pass

    def run_mini(self):
        try:
            notify.show_toast("MINI - Intelligent Search Engine",
                              "Mini is Listening...", 'icon.ico', 6, True)
            playsound.playsound(
                'hindi_sounds/Mini is Listening.. what help you need.mp3')

            task = self.hearYou()

            task = task.replace('mini', "")
            print(task)

            for variousTasks in self.taskArray:

                if variousTasks in task:
                    if variousTasks == 'stop':
                        playsound.playsound(
                            'hindi_sounds/Thank You. Have a nice day..mp3')
                        return 'stop'

                    if variousTasks == 'who' or variousTasks == 'where' or variousTasks == 'what':
                        self.summarizeWikipedia(task, variousTasks)
                        return 0

                    if variousTasks == 'play' or variousTasks == 'browse':
                        self.browseOnWeb(task, variousTasks)
                        return 0

                    self.taskDictionary[variousTasks]()
                    return 0

            playsound.playsound(
                "hindi_sounds/Sorry Could not understand.mp3")
        except:
            pass


fun = Mini()
# fun.run_mini()
#  use for fast debugging .. run assistant.py directly


class FunZone:

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
                fun.talk('See your watch. Dont disturb me for small things.')

            elif 'joke' in task:
                fun.talk(
                    'Open your selfie cam or go stand in front of a mirror. You will see the funniest joke in this world.')

            elif 'song' in task:
                fun.talk('I am bored right now. Go Hang out with your friends')

            elif 'created' in task:
                fun.talk('Some nerds like you')

            elif 'play' in task:
                fun.talk('I dont have time to play with humans.Get a life.')

            elif 'single' in task:
                fun.talk(
                    'Its none of your business. But yes, I am not single like you are')

            elif 'memory' in task:
                fun.talk(
                    'Do you remember? One day you proposed your crush and you got friendzoned. I laughed so much that day. lol')

            elif 'who' in task:
                fun.talk(
                    'Such a stupid question. You should have known about this. Go increase your general knowledge')

            else:
                fun.talk('I am busy. Go do it yourself')
        except:
            pass
