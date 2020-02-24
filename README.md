# openrazer-effects
custom effects for razer devices using the openrazer driver

All effects have been tested on Ubuntu with the Razer Ornata Chroma. The [OpenRazer](https://github.com/openrazer/openrazer) driver is required to run them. 


### [manager.py](manager.py)
manager.py is a simple interface to switch between effects or set the brightness. All effects can be ran on their own without the manager. 


### [rainbowRGB.py](rainbowRGB.py)
This effect sets every key to a different color every second like an rainbow.

### [raindrops.py](raindrops.py)
This effect sets the light to a light grey background then randomly colors keys blue. Its like rain against a window. The background color and key color can both be changed at the top of the file. 

### [sections-randomRGB.py](sections-randomRGB.py)
This effect sets each section of the keyboard to a different color out of a list of color options. The keyboard is split into 15 sections and each section pulls a random color out of the color list. The color list contains Red,Green & Blue. These can be switched out with other colors at the top of the file. (currently 10key is split with top and bottom but in future updates will be all one color.)

### [stripes.py](stripes.py)
This effect set the keyboard effect to alternating stripes that swich back and forth. 

### [set-brightness.py](set-brightness.py)
This will set the brightness to 100 if no arguments are passed. You can also pass the brightness lvl you want set like <code>set-brightness.py 25</code> to set the brightness to 25%
