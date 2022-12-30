#!/bin/sh

# Redshift
redshift-gtk -l 39.990879:4.093830 &
# Automount Devices
udiskie -t &
# Battery
cbatticon -n -l 25 -r 10 -u 5 &
# Volume Icon
pa-applet &
# Bluetooth
blueman-applet &
# Thunar Daemon (Faster Start Up)
thunar --daemon &
# Polkit Gui
lxpolkit &
# Whatsapp
#whatsapp-nativefier &

#Nextcloud
#nextcloud &
