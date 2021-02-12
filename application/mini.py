import assistant
from win10toast import ToastNotifier

myAssistant = assistant.Mini()
myAssistant.talk("Welcome to MINI, the Intelligent Search Engine")


notify = ToastNotifier()

def open_mini():
    
    notify.show_toast("MINI Intelligent Search Engine",
                              "Welcome to Mini Intelligent Search", 'icon.ico', 4, True)
    myAssistant.talk("Welcome to my Assistant MINI. Try Speaking Something")
    while True:
        run = myAssistant.mini()
        if run == 'stop':
            break
