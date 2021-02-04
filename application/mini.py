import assistant

myAssistant = assistant.Mini()

while True:
    run = myAssistant.mini()
    if run == 'stop':
        break

