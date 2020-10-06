#!/usr/bin/python3

###############################################################
### PROJECT:
### Flatpak Custom Theme Update
### SCRIPT:
### ftu.py
### DESCRIPTION:
### Automated custom theme update for Flatpak Apps
###
### MAINTAINED BY:
### hkdb <hkdb@3df.io>
### ############################################################

import os, datetime, sys, glob, shutil, string
from pathlib import Path

# Define Version
version = "v00.01"

# Get HomeDir
homedir = str(Path.home())

# Get current theme being used
print("\nIdentifying which theme is currently being used...")
theme = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
theme = theme[1:-2]
print("THEME: " + theme)

# Check what theme folders in flatpak exists
print("\nChecking Flatpak Gnome Platform Dependencies...")
platforms = os.listdir(homedir + "/.local/share/flatpak/runtime/org.gnome.Platform/x86_64/")
for p in platforms:
    print("Gnome " + p)

# Check on where theme exists
orig = ""
print("\nChecking to see where the theme dir is...")
home = os.path.isdir(homedir+"/.local/share/themes/"+theme)
print("HOME: ", home)
if home == True:
    orig = homedir+"/.local/share/themes/"+theme
else:
    system = os.path.isdir("/usr/share/themes/"+theme)
    print("SYSTEM: ", system)
    if system == True:
        orig = "/usr/share/theme/"+theme
    else:
        print("ERROR: No such theme available in the 2 common places to find them. Please move your theme folder to either ~/.local/share/themes/ or /usr/share/themes/ and try again.\n")
        exit()

# copy theme over to all available platforms
print("\nCopying theme to all available platforms...")
for p in platforms:
    print("COPYING TO: ",  p)
    os.system("cp -R " + orig + " " + homedir + "/.local/share/flatpak/runtime/org.gnome.Platform/x86_64/" + p + "/active/files/share/themes/")
    # print("cp -R " + orig + " " + homedir + "/.local/share/flatpak/runtime/org.gnome.Platform/x86_64/" + p + "/active/files/share/themes/")

print("\nDONE...\n")
