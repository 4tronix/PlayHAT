PlayHAT v0.1
============

PlayHAT has 9 neopixels organised in a 3x3 grid

Each pixel is individually addressable and has 8 bits to define the brightnes of each colour (Red, Green and Blue).

The LEDs are on pin 12 (GPIO 18) of the Raspberry Pi GPIO connector and can be driven in python using the rpi_ws281x.py base library and neopixel.py wrapper

Buttons and beeper on physical and GPIO pins as follows:

Button	Phys	GPIO
--------------------
Red	7	04
Green	11	17
Yellow	13	27
Blue	15	22
Beeper	16	23

When the button is pressed, the corresponding GPIO Input pin is LOW

To make the Beeper sound, raise the GPIO Output pin HIGH


Software Installation
=====================

Ensure your Raspberry Pi is connected to the internet

$ git clone https://github.com/4tronix/PlayHAT
$ cd ~/PlayHAT
$ sudo apt-get install python-pip python-dev
$ sudo python setup.py install

NB. For Raspbian Jessie release 10th May 2016 (and probbly later versions also) you will need to add the following lines in config.txt:
  hdmi_force_hotplug=1
  hdmi_force_edid_audio=1

Now you can run the strandtest.py demo as follows:
$ sudo python strandtest.py

Also included is a dice simulator which runs continuously
$ sudo python playhat.py


