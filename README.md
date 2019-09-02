AR Sandbox
===========
Augmented Reality Sandbox - simply mold the sand by hand and the landscape comes to life

# Hardware
- 1x Raspberry Pi 4 (2GB RAM)
- 1x Microsoft Kinect Sensor v1 (XBox 360)
- 1x Beamer BenQ MX631ST (4:3)
- Assembled sandbox (e.g. wood)

# Installation
Install on Raspberry Pi latest version of Rasbian.

## Update sources
```
sudo apt-get update
sudo apt-get upgrade
```

## Install prerequisites for libusb and libfreenect
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
wget https://github.com/OpenKinect/libfreenect/archive/v0.5.3.tar.gz
tar -xvzf v0.5.3.tar.gz
cd ~/src/libfreenect-0.5.3
mkdir build
cd build
cmake -L ..
make
sudo make install
```

# Run
