# Garden Project
Description: A terrarium project that reads sensor data (i.e. sht31, SBT444t and others) and posted it to the IO.Adafuit IoT dashboard

## Dependencies:
### Raspberry Pi:
Run apt-get to update all packaged and run rpi-update to update the Pi. I run them all at once because it will make sure the whole platform is good.
	sudo apt-get update && apt-get upgrade –y && rpi-update && reboot
### Adafruit-IO-Basic:
#### Easy Installation:
If you have [pip installed](https://pip.pypa.io/en/latest/installing.html)
(typically with ````apt-get install python-pip```` on a Debian/Ubuntu-based
system) then run:

    sudo pip install adafruit-io

This will automatically install the Adafruit IO Python client code for your Python scripts to use. Along with this installation, there is a example folder from which some of this code is derived from.
#### Manual Installation:
Clone or download the contents from Adafruit’s [IO] (https://github.com/adafruit/io-client-python).  Then navigate to the folder
in a terminal and run the following command:

    sudo python setup.py install
