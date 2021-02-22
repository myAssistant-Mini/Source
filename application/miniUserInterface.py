from modules import *

notify = ToastNotifier()
notify.show_toast("MINI - Intelligent Search Engine",
                  "Mini has Started", 'icon.ico', 4, True)


root = Tk()
root.title('MINI Search Engine')
p1 = PhotoImage(file='favicon.png')
btn = PhotoImage(file='btn.png', height=33, width=399)
root.iconphoto(False, p1)
my_label = Label(root)

my_label.pack()

player = tkvideo("gui.mp4", my_label, loop=1, size=(399, 700))
start = tk.Button(root, image=btn, height=33, width=399, command=open_mini)
start.pack()
player.play()
pygame.init()
mixer.music.load('song.mp3')
mixer.music.play(0)
root.mainloop()
