XModMap script file for the Minimak layout
==========================================

This script file will convert, under your X11 environment, an US keyboard layout to
minimak.

You can use the left only variant to aid your learning.

How to switch to the Minimak layout
-----------------------------------

You can switch to the Minimak layout using the xmodmap command like this:

```
$ xmodmap us_to_minimak.xmodmap
```

or, if you would like the left only variant:

```
$ xmodmap us_to_minimak_left.xmodmap
```

The layout change will last only until the session end.

To return to the US layout
--------------------------


```
$ xmodmap minimak_to_us.xmodmap
```
