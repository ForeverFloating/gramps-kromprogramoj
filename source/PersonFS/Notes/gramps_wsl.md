# Using Gramps on Windows with WSL

prerequisites: Windows 10 >= 22H2, or Windows 11


## Install WSL
Go to "Settings"
* --> System
* --> Optional Features
* --> More Windows features
* --> Check "Windows Subsystem for Linux" and "Virtual Machine Platform"
* --> OK, reboot

## update WSL to the latest version:
* Launch "Microsoft"
* Search for WSL, click get

## install Ubuntu
still in "Microsoft Store":
* search for Ubuntu 22.04, click get then open
* enter a username and password.
* install French language support:
```
sudo apt-get -y install language-pack-fr language-pack-fr-base language-pack-gnome-fr language-pack-gnome-fr-base
sudo locale-gen
sudo update-locale LANG=fr_FR.UTF-8
```

## install Gramps
in the Ubuntu command line:
```
sudo add-apt-repository universe
sudo apt install gramps python3-pip -y
gsettings set org.gnome.desktop.interface cursor-theme whiteglass
gramps
```

## optional: install the vGPU driver
