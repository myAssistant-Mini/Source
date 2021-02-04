
import assistant

myAssistant = assistant.Mini()

while True:
    run = myAssistant.run_mini()
    if (run == 'stop'):
        break
