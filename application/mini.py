import assistant

myAssistant = assistant.Mini()
myAssistant.talk("Welcome to MINI, the Intelligent Search Engine")


def open_mini():
    myAssistant.talk("Welcome to my Assistant MINI. Try Speaking Something")
    while True:
        run = myAssistant.mini()
        if run == 'stop':
            break
