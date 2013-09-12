Ubuntu Minimak Keymaps
======================

Allows minimak keyboard layouts to be loaded from _System
Settings -> Keyboard Layout_.

Installation
------------

First, make backup copies the originals of these files:

~~~
/usr/share/X11/xkb/rules/evdev.lst
/usr/share/X11/xkb/rules/evdev.xml
~~~

Then open a shell and run the following commands:

~~~
cd minimak/linux
sudo cp evdev.lst /usr/share/X11/xkb/rules/
sudo cp evdev.xml /usr/share/X11/xkb/rules/
~~~

Finally backup the symbols file for your locale (US or UK only), then
copy the local file to the symbols directory:

~~~
sudo cp gb /usr/share/X11/xkb/symbols/
 - or -
sudo cp us /usr/share/X11/xkb/symbols/
~~~

