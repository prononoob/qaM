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

def topB2():
    webbrowser.open_new_tab('www.messenger.com')

def leftB2():
    webbrowser.open_new_tab('www.thrashermagazine.com')

def rightB2():
    webbrowser.open_new_tab('www.allegro.pl')

def bottomB2():
    webbrowser.open_new_tab('www.gnome-look.org')

def GExit():
    exit()

def gext():
    b.pack_forget()
    b1.place_forget()
    b2.place_forget()
    b3.pack_forget()
    bn.place_forget()

    b5.pack(side='top')
    b6.place(x=0, y=93, in_=root)
    b7.place(x=208, y=93, in_=root)
    b8.pack(side='bottom')
    bb.place(x=229, y=216, in_=root)

def gack():
    b5.pack_forget()
    b6.place_forget()
    b7.place_forget()
    b8.pack_forget()
    bb.place_forget()

    b.pack(side='top')
    b1.place(x=0, y=93, in_=root)
    b2.place(x=208, y=93, in_=root)
    b3.pack(side='bottom')
    bn.place(x=229, y=216, in_=root)


while True:
    root.configure(background = '#303030')
    root.overrideredirect(1)
    b = Button(root, width = 8, height = 5, foreground='grey', text = "UNIXPORN", command=topB)
    b1 = Button(root, width = 8, height = 5, foreground = 'grey', text = "GMAIL", command=leftB)
    b2 = Button(root, width = 8, height = 5, foreground = 'grey', text = "YOUTUBE", command=rightB)
    b3 = Button(root, width = 8, height = 5, foreground = 'grey', text = "GITHUB", command=bottomB)
    b4 = Button(root, width = 6, height = 4, foreground = 'grey', text = "EXIT", command=GExit)
    b5 = Button(root, width = 8, height = 5, foreground = 'grey', text = "MESSENGER", command=topB2)
    b6 = Button(root, width = 8, height = 5, foreground = 'grey', text = "THRASHER", command=leftB2)
    b7 = Button(root, width = 8, height = 5, foreground = 'grey', text = "ALLEGRO", command=rightB2)
    b8 = Button(root, width = 8, height = 5, foreground = 'grey', text = "GNOME-LOOK", command=bottomB2)

    bn = Button(root, width = 2, height = 1, foreground = 'grey', text = "NEXT", command=gext)
    bb = Button(root, width = 2, height = 1, foreground = 'grey', text = "BACK", command=gack)

    b.configure(background = '#303030')
    b1.configure(background = '#303030')
    b2.configure(background = '#303030')
    b3.configure(background = '#303030')
    b4.configure(background = '#303030')
    b5.configure(background = '#303030')
    b6.configure(background = '#303030')
    b7.configure(background = '#303030')
    b8.configure(background = '#303030')
    bn.configure(background = '#303030')
    bb.configure(background = '#303030')

    b.pack(side='top')
    b1.place(x=0, y=93, in_=root)
    b2.place(x=208, y=93, in_=root)
    b3.pack(side='bottom')
    b4.place(x=111, y=100, in_=root)
    bn.place(x=229, y=216, in_=root)
    root.geometry('300x276+810+402')
    mainloop()
