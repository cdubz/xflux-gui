f.lux indicator applet
======================
Better lighting for your computer

The f.lux indicator applet `fluxgui` is an indicator applet to control
`xflux`, an application that makes the color of your computer's
display adapt to the time of day, warm at nights and like sunlight
during the day. Reducing blue light exposure in the evening can help
you fall asleep at night. See https://justgetflux.com/research.html
for more details.

This project -- https://github.com/xflux-gui/xflux-gui -- is only
concerned with the `fluxgui` indicator applet program, not with the
underlying `xflux` program the indicator applet controls. The `xflux`
program is responsible for actually changing the color of your
screen. See https://justgetflux.com/linux.html for more information
about `xflux`.

This fork
---------
**This is a fork of the official `fluxgui` project and is only 
intended to be used as a temporary workaround. See 
https://github.com/xflux-gui/xflux-gui for the latest version of
`fluxgui`.**

This fork is a very slightly modified `fluxgui` applet that *may* work
in situations where the standard applet does not. Specifically, this 
fork was created as a workaround to issues with Ubuntu-based systems
using certain NVidia graphics cards and drivers. See 
https://forum.justgetflux.com/topic/2373/ for more discussion.

If you execute `xflux` in a terminal and receive an error message 
similar to the one below, this fork may help you.

```
Welcome to xflux (f.lux for X)
This will only work if you're running X on console.

Found 1 screen.
Sorry, we only support 8 and 10-bit displays right now.
```

Install Instructions
--------------------

### Remove PPA Version

If you have previously installed `fluxgui` from a PPA, you'll need to
uninstall that first:

```bash
sudo apt-get remove fluxgui
```

### Ubuntu/Debian Manual Install

Next, follow the typical manual install instructions, using this 
repository:

```bash
# Install dependencies
sudo apt-get install git python-appindicator python-xdg python-pexpect python-gconf python-gtk2 python-glade2 libxxf86vm1

# Download xflux-gui
cd /tmp
git clone "https://github.com/cdubz/xflux-gui.git"
cd xflux-gui
python download-xflux.py

# EITHER install globally
sudo python setup.py install
# EXCLUSIVE OR, install in your home directory. The binary installs
# into ~/.local/bin, so be sure to add that to your PATH if installing locally.
python setup.py install --user

# Run flux
fluxgui
```

### Ubuntu/Debian Launcher

To take advantage of the launchcer, simply copying from the `desktop`
folder to the appropriate location on your system. E.g.:

```bash
# From the cloned repo directory

# EITHER install globally
sudo cp desktop/fluxgui.desktop /usr/share/applications
# EXCLUSIVE OR, loccally
cp desktop/fluxgui.desktop ~/.local/share/applications
```

### Ubuntu/Debian Manual Uninstall

Uninstall by making `setup.py` tell you where it installed files and
then removing the installed files.

```bash
# EITHER uninstall globally
sudo python setup.py install --record installed.txt
sudo xargs rm -vr < installed.txt

# EXCLUSIVE OR uinstall in your home directory
python setup.py install --user --record installed.txt
xargs rm -vr < installed.txt
```

License
-------

The f.lux indicator applet is released under the [MIT License](https://github.com/cdubz/xflux-gui/blob/master/LICENSE).
