# Preface
Overall, following [this webpage from AGL](https://wiki.automotivelinux.org/agl-distro/agl-raspberrypi)
gives you right directions.

The official instructions didn't 100% for me, though.
I experienced some difficulties during building,
and below are what finally worked for me.


# Set Up Operating System
**AGL must be built on a Linux OS.**

I used VirtualBox to set up a virtual machine,
and installed Ubuntu 16.04 LTS on it.
Check [this video](https://youtu.be/wBp0Rb-ZJak?t=15m57s) for how to install VirtualBox and Ubuntu.

I recommend at least 8GB memory and 100GB disk space allocated on the Ubuntu machine.
The building eats a lot of disk space.

Besides Ubuntu, Debian, Fedora, CentOS, OpenSUSE should also be OK.

When inside Ubuntu, run the following command in Terminal.
These are a bunch of tools that AGL needs for building.

```bash
sudo apt-get install gawk wget git-core diffstat unzip texinfo gcc-multilib \
    build-essential chrpath socat libsdl1.2-dev xterm cpio curl
```

# Prepare `repo` Tool
`repo` is a source code managing tool developed by Google.
It is built on top of `git` (so you need to have `git` ready on your Ubuntu).
`repo`'s job is to help manage many git repositories.

Run these commands to install `repo`:
```bash
mkdir -p ~/bin
export PATH=~/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
```

# Download AGL Source Code
The "Download source" section in the [official AGL for Raspberry Pi instructions](https://wiki.automotivelinux.org/agl-distro/agl-raspberrypi)
says "you can choose your source code release", which, for a beginner doesn't make a lot of sense at the beginning.

Actually it just means which version of AGL source code you want to download.

AGL has versions A, B, C, D, E so far.
However, to sound more creative, they expand ABCDE to bizarre names of fishes.
Therefore the versions are:

|Version|Fish Name|
|:---:|---|
|A|Agile Albacore|
|B|Brilliant Blowfish|
|C|Charming Chinook|
|D|Daring Dab|
|E|Electric Eel|

The Eel 5.0.1 worked for me.  
(I experienced tons of building errors when I first tried downloading the master branch,
not recommend that.)

To download the Eel 5.0.1 version of AGL source code:
```bash
mkdir ~/AGL-Eel
cd ~/AGL-Eel
repo init -b eel -m eel_5.0.1.xml -u https://gerrit.automotivelinux.org/gerrit/AGL/AGL-repo
repo sync
```

I just chose to make a directory named `AGL-Eel` to put all the stuff.
It can be any name.

# Build AGL Demo Platform fro Raspberry Pi 2
Run these commands:
```
source meta-agl/scripts/aglsetup.sh -m raspberrypi3 agl-demo agl-netboot agl-appfw-smack

bitbake agl-demo-platform
```

The first command runs a script and set up some configuration variables.
The second line starts the actual building. It can take several hours.

# Put the Built Image into an SD Card
If the `bitbake` command runs successfully,
you should have a `build` directory under `AGL-Eel`.

Find this file:
`~/AGL-Eel/build/tmp/deploy/images/raspberrypi2/agl-demo-platform-raspberrypi2.wic.xz`

This file contains what you need to put into the SD card.
You can copy it to another place if you want.

Now you can insert the SD card.
Refer to [this post](https://blog.lobraun.de/2015/06/06/mount-sd-cards-within-virtualbox-on-mac-os-x/)
for how to access the SD card plugged onto a Mac OS machine from inside a VirtualBox VM.

After plugging in the SD card run `lsblk` (list block) command in Ubuntu's terminal.
The out put should look something like this:
```bash
 $ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sdb      8:16   0  7.4G  0 disk
└─sdb1   8:17   0  7.4G  0 part
sr0     11:0    1 1024M  0 rom
sda      8:0    0   20G  0 disk
├─sda2   8:2    0    1K  0 part
├─sda5   8:5    0 15.4G  0 part /
└─sda1   8:1    0  4.7G  0 part [SWAP]
```
Here `sdb` refer to the SD card device. (Double check the size to make sure.)

Next, unmount the SD card device, then flash data into it.
Run these commands:  
***Replace `sdb` with the device name that refers your SD card!
The `dd` command can be destructive!***
```bash
sudo umount /dev/sdb
xzcat agl-demo-platform-raspberrypi2.wic.xz | sudo dd of=/dev/sdb bs=4M
sync
```

Now put the SD card into Raspberry Pi 2,
power it on,
then you should be able to see it boot,
and finally rest at AGL home screen.