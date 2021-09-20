#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
export DISPLAY=:0
/bin/bash displayorient.sh
source setupkiosk.sh
xset dpms 0 0 0 && xset s noblank && xset s off
xrdb -merge ~/.Xresources
xbindkeys
KIOSKURL="$KIOSK"
WINWID=$WINWID
WINHT=$WINHT
echo $KIOSKURL
ETHUP=`/sbin/ifconfig enp1s0 | grep 'inet'`
THIS=`pgrep chrome`
THAT=`pgrep vino`
if [ -z "$THAT" ]
        then
            if [ -z "$THIS" ]
                    then
                        /opt/google/chrome/google-chrome --window-position=0,0 --window-size=$WINWID,$WINHT --enable-viewport --incognito --kiosk --disable-cache $KIOSKURL
            fi
fi

            
