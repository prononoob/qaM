import time
from tkinter import Tk, Button, mainloop
import webbrowser
import os


root = Tk()

def topB():
    webbrowser.open_new_tab('www.reddit.com/r/unixporn')

def leftB():
    webbrowser.open_new_tab('www.gmail.com')

def rightB():
    webbrowser.open_new_tab('www.youtube.com')

def bottomB():
    webbrowser.open_new_tab('www.github.com')

def GExit():
    exit()

while True:
    root.configure(background = '#303030')
    root.overrideredirect(1)
    b = Button(root, width = 8, height = 5, foreground='grey', text="UNIXPORN", command=topB)
    b1 = Button(root, width = 8, height = 5, foreground = 'grey', text="GMAIL", command=leftB)
    b2 = Button(root, width = 8, height = 5, foreground = 'grey', text = "YOUTUBE", command=rightB)
    b3 = Button(root, width = 8, height = 5, foreground = 'grey', text = "GITHUB", command=bottomB)
    b4 = Button(root, width = 6, height = 4, foreground = 'grey', text = "EXIT", command=GExit)

    b.configure(background = '#303030')
    b1.configure(background = '#303030')
    b2.configure(background = '#303030')
    b3.configure(background = '#303030')
    b4.configure(background = '#303030')

    b.pack(side='top')
    b1.place(x=0, y=93, in_=root)
    b2.place(x=208, y=93, in_=root)
    b3.pack(side='bottom')
    b4.place(x=111, y=100, in_=root)
    root.geometry('300x276+810+402')
    mainloop()
