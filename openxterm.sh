#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
#for some reason I do not understand this allows us to get focus to the xterm
sleep 1
#open chrome tab
DISPLAY=:0 xdotool key ctrl+shift+n
sleep 0.1
#close chrome tab
DISPLAY=:0 xdotool key ctrl+w
sleep 0.1
#open xterm
DISPLAY=:0 /usr/bin/xterm -maximized
