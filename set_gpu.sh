#!/bin/sh

# delete nvidia-driver
sudo nvidia-uninstall

# 'lightdm' demon stop
sudo service lightdm stop

# reinstall nvidia-driver
sudo ./install/NVIDIA-Linux-x86_64-384.59.run --no-opengl-files

# restart 'lightdm'
sudo service lightdm start
