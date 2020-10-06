# Gnome Flatpak Custom Theme Updater
maintained by: @hkdb

![screenshot](screenshot.png)

## SUMMARY

If you do what I do as described [here](https://medium.com/@hkdb/custom-gtk3-theme-for-flatpak-6d2c216e1496) to sync your custom theme with Flatpak apps, everytime your flatpak apps get updated, your theme folder gets deleted from the flapak Gnome runtime folder and your flatpak apps go back to the default theme that's out of sync with what you are using in Gnome. Here's a quick script to sync your custom theme with flatpak apps after they get updated to make it a little easier.

## DEPENDENCIES

- Gnome Desktop 3.3x running 64-bit
- Python 3.x

## USAGE

1. `git clone git@github.com:hkdb/gnome-ftu.git`
2. `cd gnome-ftu
3. `./gftu.py`

If you want to make things easier and execute this globally inside your terminal, you can do the following to alias it:

```
cd ~/.local/share/
git clone git@github.com:hkdb/gnome-ftu.git
echo "alias gftu='~/.local/share/gnome-ftu/gftu.py'" >> ~/.bash_aliases
exit
```
The next time you open up your terminal, you can just type `gftu` anywhere and it will do what it's supposed to do.

### DISCLAIMER
This repo is sponsored by 3DF OSI and is maintained by volunteers. 3DF Limited, 3DF OSI, and its volunteers in no way make any guarantees. Please use at your own risk!

To Learn more, please visit:

https://osi.3df.io

https://3df.io
