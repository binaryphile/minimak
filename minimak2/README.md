XModMap script file for the Minimak layout
==========================================

This script file will convert, under your X11 environment, an US keyboard layout to
minimak2.

How to switch to the Minimak layout
-----------------------------------

You can switch to the Minimak layout using the xmodmap command like this:

```
$ xmodmap minimak2.xmodmap
```

The layout change will last only until the session end.

To return to the US layout
--------------------------


```
$ xmodmap orig.xmodmap
```
