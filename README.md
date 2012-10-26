Included in this readme:

- [Windows Boot Mappings for Minimak](#wbm)
- [Portable Key Layout for Minimak](#pkl)
- [Mac OSX Installation](#osx)
- [Linux Installation](#lnx)

Windows Boot Mappings for Minimak {: #wbm}
=================================

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

Installation
------------

You must be administrator on your machine.

Double-click the registry file you want and accept the changes.  Then
reboot.

Once you've rebooted, your layout is changed and you don't have to do
anything further to use it.

Portable Key Layout for Minimak {: #pkl}
===============================

This is a copy of the [PKL](http://pkl.sourceforge.net/) project which
has been customized for Minimak.  It was created by us and is not
supported by the PKL folks.  It's in the `pkl` subdirectory.

It includes the same layouts as above, as well as inverse mappings for
Minimak and the 8-key layout.  The inverse mappings are meant to be used
once you've adopted a boot mapping, but need to go back to QWERTY
temporarily.  For example, if you need someone else to use the keyboard
to enter a password.

None of these layouts include the Backspace to CapsLock mapping.

Installation
------------

PKL is located in the `pkl` subdirectory.

This is a portable executable, so it doesn't need to be installed to use
it.

If you'd like to install it like a normal program, I recommend
[ZipInstaller](http://www.nirsoft.net/utils/zipinst.html).

Usage
-----

- Run `pkl.exe`
- __To change layouts:__  right-click the icon in the system tray and
  select _Change Layout_.
- __To move the on-screen keyboard:__  float the mouse over the keyboard
  and it will move.
- __To get rid of the on-screen keyboard:__  press Win-F1.
- __To toggle the layout on and off:__  press both Alt keys.

Mac OSX Installation {: #osx}
====================

- Copy `Minimak.bundle` from the `osx` directory in the repository to `/Library/Keyboard Layouts` 
  You will need to enter your password
- Open _System Preferences > Keyboard > Input Sources_
- Turn on the layouts you wish to use

For information on Backslock on the Mac, see the [Colemak Mac page].

Linux Installation
==================

These are brand new mappings and untested since I don't have a machine
with X to test on.  The mappings are simple enough that I'm confident
most will work with the possible exception of the P and semicolon
mappings, since I'm not sure whether the semicolon keysym is spelled
out.

The `linux` directory holds [xmodmap] mapping files.  See the [Window
Boot Mapping section](#wbm) for descriptions of each of the files.

To try the keymappings for the length of your login session, run the
command:

    xmodmap filename

where filename is the name of the mapping you've chosen.

To install one for your login, first copy the file to `~/.Xmodmap`, then
add the following to `~/.xinitrc`:

    if [ -f $HOME/.Xmodmap ]; then
        /usr/bin/xmodmap $HOME/.Xmodmap
    fi

There are no Backslock mappings since many Linux systems have Backslock
as a possible configuraion choice in their keyboard settings.

[Colemak Mac page]: http://colemak.com/wiki/index.php?title=Mac 
[xmodmap]: https://wiki.archlinux.org/index.php/Xmodmap
