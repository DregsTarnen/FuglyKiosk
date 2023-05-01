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
    window.destroy()
#command to write screen rotation file right
def rotateright():
    os.system('xrandr -d :0 --output HDMI-1 --mode 1080x1920 --rotate right')
    directions = "xrandr -d :0 --output HDMI-1 --mode 1080x1920 --rotate right"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1080' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1920' setupkiosk.sh"
    os.system(writewidth)
    os.system(writeheight)
#command to write screen rotation file left
def rotateleft():
    os.system('xrandr -d :0 --output HDMI-1 --mode 1080x1920 --rotate left')
    directions = "xrandr -d :0 -output HDMI-1 --mode 1080x1920 --rotate left"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1080' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1920' setupkiosk.sh"
    os.system(writewidth)
    os.system(writeheight)
#command to invert screen
def invertdisplay():
    os.system('xrandr -d :0 --output HDMI-1 --mode 1920x1080 --rotate inverted')
    directions = "xrandr -d :0 --output HDMI-1 --mode 1920x1080 --rotate inverted"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1920' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1080' setupkiosk.sh"
    os.system(writewidth)
    os.system(writeheight)
#commad to display normally
def normaldisplay():
    os.system('xrandr -d :0 --output HDMI-1 --mode 1920x1080 --rotate normal')
    directions = "xrandr -d :0 --output HDMI-1 --mode 1920x1080 --rotate normal"
    with open('displayorient.sh', 'w') as file:
        file.write(directions)
    writewidth = "sed -i '/WINWID/c\WINWID=1920' setupkiosk.sh"
    writeheight = "sed -i '/WINHT/c\WINHT=1080' setupkiosk.sh"
    os.system(writewidth)
    os.system(writeheight)
#button submit url entry
btnsubmit = Button(window, text="SUBMIT", command=lambda: [submitted(), closeapp()])
btnsubmit.pack()
#button network configure
btnnetconfig = Button(window, text="NETWORK CONFIGURE", command=netconfig)
btnnetconfig.pack()
#button to rotate display right
btnrotateright = Button(window, text="ROTATE DISPLAY RIGHT", command=lambda: [closeapp(), rotateright()])
btnrotateright.pack()
#button to rotate display left
btnrotateleft = Button(window, text="ROTATE DISPLAY LEFT", command=lambda: [closeapp(), rotateleft()])
btnrotateleft.pack()
#button to invert display
btninvert = Button(window, text="INVERT DISPLAY", command=lambda: [closeapp(), invertdisplay()])
btninvert.pack()
#button for normal display
btnnormaldisplay = Button(window, text="DISPLAY NORMALLY", command=lambda: [closeapp(), normaldisplay()])
btnnormaldisplay.pack()
#button to close window
btnclose = Button(window, text="CLOSE", command=closeapp)
btnclose.pack()
#window main loop
window.mainloop()
        
