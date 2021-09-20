#!/usr/bin/env python3
from tkinter import *
import os
import subprocess
#window parameters
window = Tk()
window.geometry("1000x1000")
window.title("Fugly Kiosk Setup")
#user feedback labels
geturl = "cat /home/fuglykiosk/setupkiosk.sh | grep KIOSK= | cut -b 7-"
data = subprocess.check_output(geturl, shell=True)
cururl = data.decode("utf-8")
cururltxt = "Current Kiosk URL: "+cururl
lblcururl = Label(window, text=cururltxt, font=("Arial", 22))
lblcururl.pack()
lblurl = Label(window, text="Enter kiosk URL: (prefix with 'https://')", font=("Arial", 22))
lblurl.pack()
#command to clear textfield
def cleartext(event):
    txturl.delete(1.0, END)
#textfield for url text entry for kiosk
txturl = Text(window, height=2, width=50, font=("Arial", 16))
txturl.insert(1.0, 'https://localkioskurl')
txturl.pack()
txturl.bind("<Button-1>", cleartext)
#command for submitting url text entry to local shell script
def submitted():
    contents = txturl.get(1.0, END)
    lblurl.configure(text="Your kiosk URL is: "+contents)
    writecontent = "sed -i '/KIOSK/c\KIOSK="+contents+"' setupkiosk.sh"
    restartkiosk = "pkill chrome"
    os.system(writecontent)
    os.system(restartkiosk)
#command function for opening nmtui app. we open the terminal to ask for credentials
def netconfig():
    os.system('xterm -maximized -e sudo nmtui &')
#command function for closing setup app
def closeapp():
    os.system('pkill python')
#command to write screen rotation file right
def rotateright():
    os.system('DISPLAY=:0 xrandr -o right')
    directions = "DISPLAY=:0 xrandr -o right"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1080' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1920' setupkiosk.sh"
    restartkiosk = "pkill chrome"
    os.system(writewidth)
    os.system(writeheight)
    os.system(restartkiosk)
#command to write screen rotation file left
def rotateleft():
    os.system('DISPLAY=:0 xrandr -o left')
    directions = "DISPLAY=:0 xrandr -o left"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1080' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1920' setupkiosk.sh"
    restartkiosk = "pkill chrome"
    os.system(writewidth)
    os.system(writeheight)
    os.system(restartkiosk)
#command to invert screen
def invertdisplay():
    os.system('DISPLAY=:0 xrandr -o inverted')
    directions = "DISPLAY=:0 xrandr -o inverted"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1920' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1080' setupkiosk.sh"
    restartkiosk = "pkill chrome"
    os.system(writewidth)
    os.system(writeheight)
    os.system(restartkiosk)
#commad to display normally
def normaldisplay():
    os.system('DISPLAY=:0 xrandr -o normal')
    directions = "DISPLAY=:0 xrandr -o normal"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1920' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1080' setupkiosk.sh"
    restartkiosk = "pkill chrome"
    os.system(writewidth)
    os.system(writeheight)
    os.system(restartkiosk)
#button submit url entry
btnsubmit = Button(window, text="SUBMIT", command=submitted)
btnsubmit.pack()
#button network configure
btnnetconfig = Button(window, text="NETWORK CONFIGURE", command=netconfig)
btnnetconfig.pack()
#button to rotate display right
btnrotateright = Button(window, text="ROTATE DISPLAY RIGHT", command=rotateright)
btnrotateright.pack()
#button to rotate display left
btnrotateleft = Button(window, text="ROTATE DISPLAY LEFT", command=rotateleft)
btnrotateleft.pack()
#button to invert display
btninvert = Button(window, text="INVERT DISPLAY", command=invertdisplay)
btninvert.pack()
#button for normal display
btnnormaldisplay = Button(window, text="DISPLAY NORMALLY", command=normaldisplay)
btnnormaldisplay.pack()
#window main loop
window.mainloop()
        
