Boot Mappings for Minimak
=========================

To use Minimak as your system layout, registry mappings are included in
the `boot_mappings` subdirectory.

Several versions are included:

- __minimak-beg.reg:__ The beginner layout.  5 keys changed.
- __minimak.reg:__  The intermediate layout.  9 keys changed.
- __minimak+backslock.reg:__ Intermediate layout with Backspace for
  CapsLock.
- __minimak-adv.reg:__  The advanced layout.  13 keys changed.
- __minimak-adv+backslock:__ The advanced layout with Backspace for
  CapsLock.

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

Portable Key Layout for Minimak
===============================

This is a copy of the [PKL](http://pkl.sourceforge.net/) project which
has been customized for Minimak.  It was created by us and is not
supported by the PKL folks.  It's in the `pkl` subdirectory.

It includes the following layouts:

- __Minimak:__  This is the intermediate, recommended layout that changes
  9 keys from QWERTY.  It is the default since it is the one that most
  people will end up using.
- __Minimak Inverse:__  This layout is for when you have Minimak loaded
  as a boot mapping (see the website for an explanation of boot
  mappings).  If you use this inverse layout, it maps the Minimak layout
  back to QWERTY.  You can use this if you want to let someone else use
  your computer without having to reboot.
- __Minimak Beginner:__  The beginner's step toward intermediate
  Minimak.  It changes 5 keys from QWERTY.
- __Minimak Advanced:__  For those users that don't care about closeness
  to QWERTY, this is a 13-key mapping that emphasizes typing feel.
- __Minimak Advanced Inverse:__  An inverse mapping for users of the
  advanced boot mappings.

There is no inverse mapping for basic.

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
