from modules import *
from tkinter import Image

notify = ToastNotifier()
notify.show_toast("MINI - Intelligent Search Engine",
                  "Mini has Started", 'icon.ico', 4, True)


root = Tk()
root.title('MINI Search Engine')
p1 = PhotoImage(file='favicon.png')
btn = PhotoImage(file='btn.png', height=38, width=399)
root.iconphoto(False, p1)
my_label = Label(root)

my_label.pack()


player = tkvideo("miniGUI.mp4", my_label, loop=1, size=(399, 700))
start = tk.Button(root, image=btn, height=38,
                  width=399, command=selectLanguage)

start.pack()
player.play()
pygame.init()
mixer.music.load('miniAudio.mp3')
mixer.music.play(-1)
root.mainloop()
