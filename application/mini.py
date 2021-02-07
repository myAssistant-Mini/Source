import assistant
import webbrowser

myAssistant = assistant.Mini()
myAssistant.talk("Welcome to MINI, the Intelligent Search Engine")

def open_mini():
    myAssistant.talk("Welcome to my Assistant MINI. Try Speaking Something")
    while True:
        run = myAssistant.mini()
        if run == 'stop':
            break

def open_search():
    webbrowser.open('http://127.0.0.1:8000/')

