#!/bin/sh

rm -rfv ~/tmp
mkdir ~/tmp
chmod 777 ~/tmp

export DISPLAY=:0
Xvfb :0 -screen 0 1400x900x24 &
icewm-session &
x11vnc -display :0 -passwd change_pass -forever -noxdamage &
