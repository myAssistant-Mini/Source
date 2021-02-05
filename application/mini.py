import assistant

myAssistant = assistant.Mini()
myAssistant.talk("Welcome to MINI - Intelligent Search Engine")

while True:
    run = myAssistant.mini()
    if run == 'stop':
        break
