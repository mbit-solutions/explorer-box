Explorer Box AR+
===========
Augmented Reality Sandbox - simply mold the sand by hand and the landscape comes to life

# Hardware
You need following hardware:
- Raspberry Pi 4 - 2GB RAM
- Microsoft Kinect Sensor v1 (XBox 360) + Power supply (USB adapter and charger cable)
- Beamer BenQ MX631ST (Short-throw, ratio 4:3)
- Assembled sandbox (e.g. wood)

Instead of Raspberry Pi you can use any other computer e.g. Intel NUC running on Debian

# Installation
Install on Raspberry Pi latest version of Rasbian (desktop version). [You can find rasbian images here](https://www.raspberrypi.org/downloads/raspbian/)

## Update sources
```
sudo apt-get update
sudo apt-get upgrade
```

## Install prerequisites
```
sudo apt-get install cmake libudev0 libudev-dev freeglut3 freeglut3-dev libxmu6 libxmu-dev libxi6 libxi-dev git python
```

## Download and build libusb
Next we will build libusb, which is required by libfreenect. [You can find the libusb releases here](https://github.com/libusb/libusb/releases)
```
mkdir ~/src
cd ~/src
wget https://github.com/libusb/libusb/releases/download/v1.0.23/libusb-1.0.23.tar.bz2
tar -jxf libusb-1.0.23.tar.bz2
cd ~/src/libusb-1.0.23
./configure
make
sudo make install
```
## Download and build libfreenect
Finally download and build libfreenect. You can check for latest version at the [libfreenect Github page](https://github.com/OpenKinect/libfreenect/releases).

```
cd ~/src
wget https://github.com/OpenKinect/libfreenect/archive/v0.5.7.tar.gz
tar -xvzf v0.5.7.tar.gz
cd ~/src/libfreenect-0.5.7
mkdir build
cd build
cmake -L ..
make
sudo make install
```

## Clone repo
```
git clone https://github.com/mbit-solutions/explorer-box
```

# Run

## Kinect mode
Kinect sensor must be connect to Raspberry Pi
```
sudo python main.py
```

## Fake mode
No kinect sensor necessary - generates random depth image
```
sudo python main.py fakenect
```

## Calibrate kinect
Kinect sensor must be connect to Raspberry Pi
```
sudo python main.py kinect_calibrate
```

## Calibrate beamer
```
sudo python main.py beamer_calibrate
```

