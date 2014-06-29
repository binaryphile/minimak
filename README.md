Included in this readme:

- Windows Boot Mappings for Minimak
- Portable Key Layout for Minimak
- Mac OSX Installation
- Linux Installation

## Windows Boot Mappings for Minimak

To use Minimak as your system layout, registry mappings are included in
the `boot_mappings` subdirectory.

Use the PKL layouts (below) if you're just learning and use these boot
mappings if you've settled on a layout for good.

Several versions are included:

- __minimak_4_key.reg:__ Swaps D, T, E and K (looped)
- __minimak_6_key.reg:__ Swaps 4-key as well as F, R
- __minimak_8_key.reg:__  Swaps 4-key as well as N, J and L, O
- __minimak_8_key+backslock.reg:__  Adds CapsLock as Backspace
- __minimak.reg:__ Swaps remaining keys for Minimak (no Backslock)
- __minimak+backslock.reg:__ Adds CapsLock as Backspace

If you want to use user mappings (on XP) instead of boot mappings, or
you want to experiment with your own layouts, I recommend [Key
Mapper](http://code.google.com/p/keymapper/).

#### Installation

You must be administrator on your machine.

Double-click the registry file you want and accept the changes.  Then
reboot.

Once you've rebooted, your layout is changed and you don't have to do
anything further to use it.

## Portable Key Layout for Minimak

This is a copy of the [PKL](http://pkl.sourceforge.net/) project which
has been customized for Minimak.  It was created by us and is not
supported by the PKL folks.  It's in the `pkl` subdirectory.

It includes the same layouts as above, as well as inverse mappings for
Minimak and the 8-key layout.  The inverse mappings are meant to be used
once you've adopted a boot mapping, but need to go back to QWERTY
temporarily.  For example, if you need someone else to use the keyboard
to enter a password.

None of these layouts include the Backspace to CapsLock mapping.

#### Installation

PKL is located in the `pkl` subdirectory.

This is a portable executable, so it doesn't need to be installed to use
it.

If you'd like to install it like a normal program, I recommend
[ZipInstaller](http://www.nirsoft.net/utils/zipinst.html).

#### Usage

- Run `pkl.exe`
- __To change layouts:__  right-click the icon in the system tray and
  select _Change Layout_.
- __To move the on-screen keyboard:__  float the mouse over the keyboard
  and it will move.
- __To get rid of the on-screen keyboard:__  press Win-F1.
- __To toggle the layout on and off:__  press both Alt keys.

## Mac OSX Installation

- Copy `Minimak.bundle` from the `osx` directory in the repository to
`/Library/Keyboard Layouts` You will need to enter your password
- Open _System Preferences > Keyboard > Input Sources_
- Turn on the layouts you wish to use

For information on Backslock on the Mac, see the [Colemak Mac page].

## Linux Installation

Allows minimak keyboard layouts to be loaded from _System
Settings -> Keyboard Layout_.

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

Finally copy the contents of the directory appropriate for your locale,
US or UK:

~~~
sudo cp gb /usr/share/X11/xkb/symbols/
 - or -
sudo cp us /usr/share/X11/xkb/symbols/
~~~

There are no Backslock mappings since many Linux systems have Backslock
as a possible configuration choice in their keyboard settings.

[Colemak Mac page]: http://colemak.com/wiki/index.php?title=Mac
