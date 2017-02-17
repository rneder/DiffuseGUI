#!/bin/sh
if( /bin/ps | /bin/grep XWin ); then
   export DISPLAY=':0';
   /bin/xterm -rightbar -sb -pob -title "Discus_Suite secondary window" -e /bin/python3 suite_gui.py;
else
   /bin/rm -f /tmp/.X*-lock
   /bin/xinit "/bin/xterm" -rightbar -sb -pob -title "Discus_Suite primary window exit last" -e /bin/python3 suite_gui.py -- "/usr/bin/XWin" :0 -multiwindow -logfile /dev/null;
fi
