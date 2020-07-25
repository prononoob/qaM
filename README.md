# qaM
(pronounced "cum")

qaM is a minimalistic quick acces menu for websites and applications on linux systems

![Screenshot](https://raw.githubusercontent.com/prononoob/qaM/master/Screenshot%20from%202020-07-25%2017-10-53.png)

# Getting started
Needed python modules:
+ tkinter
+ webbrowser
+ time
+ os

After downloading the .py file bind ```python /path/to/file/qaM.py``` to a shortcut (for example in gnome go to keyboard shortcuts setting and set the command to "python path/to/file/qaM.py")

# Changing the buttons
To change the function of a button change the attribute of said function (by default lines 9 to 19)
for example:
```
def top():
    here type python command for example webbrowser.open_new_tab('here url')
    can be any command really, just type os.system('type any linux command here')
```
After doing this change the corespodnig text inside of the button (by default lines 27 to 31) for example:
```
b = Button(win, width = 8, height = 5, foreground='grey', text='HERE IS TEXT INSIDE THE BUTTON', command=top)
```

# Screen resolution
Depending on your screen resolution, qaM can appear not in  the center therefore change root.geometry('300x276+810+402') (by default line 44)
+ if your screen resolution is 1920x1080 the default values will work
+ if your screen resolution is different than above change to ```root.geometry('300x276+your screen width devided by 2 and minus 150 + your screen height devided by 2 and minus 138)```
