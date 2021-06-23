from win10toast import ToastNotifier
import assistant
import assistantMarathi
import assistantHindi
import assistantGerman
import pygame
from pygame import mixer
import playsound

myAssistant = assistant.Mini()
myAssistant.talk("Welcome to MINI, the Intelligent Search Engine")

marathiAssistant = assistantMarathi.Mini()
hindiAssistant = assistantHindi.Mini()
germanAssistant = assistantGerman.Mini()


notify = ToastNotifier()


def selectLanguage():
    pygame.init()
    mixer.music.stop()
    myAssistant.talk("Select your Language")
    lang = myAssistant.hearYou()
    # print(lang)   This will now make choice based on user input and decide to run the specific module
    if lang == 'english':
        open_mini()
    elif lang == 'marathi':
        open_mini_marathi()
    elif lang == 'hindi':
        open_mini_hindi()
    elif lang == 'german':
        open_mini_german()
    else:
        myAssistant.talk("Language not supported yet")


def open_mini():

    notify.show_toast("MINI Intelligent Search Engine",
                      "Welcome to Mini Intelligent Search", 'icon.ico', 4, True)
    myAssistant.talk("Welcome to my Assistant MINI. Try Speaking Something")

    while True:
        run = myAssistant.mini()

        if run == 'stop':
            break


def open_mini_marathi():

    notify.show_toast("MINI Intelligent Search Engine - MARATHI",
                      "Welcome to Mini Intelligent Search", 'icon.ico', 4, True)
    playsound.playsound(
        'marathi_sounds/Welcome to marathi Assistant MINI. Speak Something.mp3')

    while True:
        run = marathiAssistant.mini()

        if run == 'stop':
            break


def open_mini_hindi():

    notify.show_toast("MINI Intelligent Search Engine - HINDI",
                      "Welcome to Mini Intelligent Search", 'icon.ico', 4, True)
    playsound.playsound(
        'hindi_sounds/Welcome to Hindi Assistant MINI. Speak Something.mp3')

    while True:
        run = hindiAssistant.mini()

        if run == 'stop':
            break


def open_mini_german():

    notify.show_toast("MINI Intelligent Search Engine - GERMAN",
                      "Welcome to Mini Intelligent Search", 'icon.ico', 4, True)
    germanAssistant.talk(
        "Welcome to my Assistant MINI. Try Speaking Something")

    while True:
        run = germanAssistant.mini()

        if run == 'stop':
            break
