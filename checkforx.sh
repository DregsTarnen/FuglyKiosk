#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

XUP=`ps -e | grep X`
if [ -z "$XUP" ]
        then
            xinit /home/fuglykiosk/runkiosk.sh
fi
