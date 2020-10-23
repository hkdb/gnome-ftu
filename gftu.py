#!/usr/bin/python3

###############################################################
### PROJECT:
### Gnome Flatpak Custom Theme Updater
### SCRIPT:
### gftu.py
### DESCRIPTION:
### Automated custom theme update for Flatpak Apps in Gnome
###
### MAINTAINED BY:
### hkdb <hkdb@3df.io>
### ############################################################

import os, datetime, sys, glob, shutil, string
from pathlib import Path

# Define Version
version = "v00.01"

# Never write same code, make function
def copyTheme(runtime_path, namespace, platforms, theme_path):
    for p in platforms:
        dest = runtime_path + "org." + namespace + ".Platform/x86_64/" + p + "/active/files/share/themes/"
        print("\nCOPYING TO: ", dest)
        command = "sudo -H cp -R " + theme_path + " " + dest
        print(command)
        os.system("sudo -H cp -R " + theme_path + " " + dest)

# Get HomeDir
homedir = str(Path.home())

# Set runtime path
runtime_sys = "/var/lib/flatpak/runtime/"
runtime_local = homedir + "/.local/share/flatpak/runtime/"
runtime = []
print("\nLooking for Flatpak runtime...")
if os.path.isdir(runtime_sys) == True:
    runtime.append(runtime_sys)
elif os.path.isdir(runtime_local) == True:
    runtime.append(runtime_local)
else:
    print("flatpak runtime not found in:" + runtime_local + runtime_sys)
    exit()

for r in runtime:
    print("flatpak runtime found in:", r)

# Get current theme being used
print("\nIdentifying which theme is currently being used...")
theme = os.popen('gsettings get org.gnome.desktop.interface gtk-theme').read()
theme = theme[1:-2]
print("THEME: " + theme)

# Check on where theme exists
theme_path = ""
print("\nChecking to see where the theme dir is...")
if os.path.isdir(homedir+"/.themes/"+theme) == True:
    theme_path = homedir+"/.themes/"+theme
elif os.path.isdir(homedir+"/.local/share/themes/"+theme) == True:
    theme_path = homedir+"/.local/share/themes/"+theme
else:
    if os.path.isdir("/usr/share/themes/"+theme) == True:
        theme_path = "/usr/share/theme/"+theme
    else:
        print("ERROR: No such theme available in the 3 common places to find them. Please move your theme folder to either ~/.local/share/themes/ , ~/.themes/ or /usr/share/themes/ and try again.\n")
        exit()
print("theme path: ", theme_path)



# Check what theme folders in flatpak exists
print("\nChecking Flatpak Platform Dependencies...")

for r in runtime:
    if os.path.isdir(r + "org.gnome.Platform/x86_64/"):
        namespace = "gnome"
        platforms_g = os.listdir(r + "org.gnome.Platform/x86_64/")
        print("\nGnome namespace: \nPlatforms:")
        for p in platforms_g:
            print(p)
        copyTheme(r, namespace, platforms_g, theme_path)
    if os.path.isdir(r + "org.freedesktop.Platform/x86_64/"):
        namespace = "freedesktop"
        platforms_fd = os.listdir(r + "org.freedesktop.Platform/x86_64/")
        print("\nFreedesktop namespace: \nPlatforms:")
        for p in platforms_fd:
            print(p)
        copyTheme(r, namespace, platforms_fd, theme_path)

print("\nDONE...\n")

exit()