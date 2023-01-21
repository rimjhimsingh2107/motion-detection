from tkinter import *
from finalpro import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
show_video
player = tkvideo("output.mp4v", my_label, loop = 1, size = (1280,720))
player.play()
root.mainloop()