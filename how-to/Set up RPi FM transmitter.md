# Summary
Todo list:
- Install & test `minimodem` on Raspberry Pi running Raspbian OS
- Install & test `PiFm`


# `minimodem` on Raspberry Pi (Raspbian OS)
## Install
Run the following commands in Raspbian's terminal to install `minimodem`:
```bash
$ sudo apt-get update
$ sudo apt-get install minimodem
```

## Encode and decode a message in CLI
Encode (text→audio file) a message:
```bash
$ minimodem --tx -f msg.wav 300
```
then type your message at the prompt. Press `Ctrl+D` when done.
Here the number 300 means baud rate.

Decode (audio file→text) an audio file:
```bash
$ minimodem --rx -f msg.wav 300
```
and you'll see the message you just encoded with `minimodem --tx`
 


# `PiFm` on Raspberry Pi
## Install `PiFm`
First download the software (code and binary):
```bash
$ mkdir ~/pifm
$ cd ~/pifm
$ wget http://omattos.com/pifm.tar.gz
```
Then extract stuff from the .tar.gz package
```bash
$ tar -xvzf pifm.tar.gz
```

## Test `PiFm`
Try transmitting something with:
```bash
$ sudo ./pifm left_right.wav 103.3 22050 stereo
```
 





# References  
`minimodem` homepage: http://www.whence.com/minimodem/

Turning the Raspberry Pi Into an FM Transmitter: http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter

