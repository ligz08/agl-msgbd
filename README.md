# agl-msgbd
Message board app based on Automotive Grade Linux (AGL)

## Broadcast Module
The `broadcast` module is meant to run on a road-side machine maintained by
road infrastructure administrator (for example, Department of Transportation).

We implemented a commandline interface for broadcasting a message over FM radio.

Here is an example of broadcasting the message "CHAIN CONTROL 50 MILES AHEAD" for 100 times,
at 5 seconds interval:
```
$ python ./broadcast/broadcast.py -m "CHAIN CONTROL 50 MILES AHEAD" -r 100 -g 5
```

Complete help information for the `broadcast` module as follows:
```
$ python ./broadcast/broadcast.py -h
usage: broadcast.py [-h] [-m MESSAGE | -f FILE] [-r REPEATS] [-g GAP]
                    [-b BAUDMODE]

optional arguments:
  -h, --help            show this help message and exit
  -m MESSAGE, --message MESSAGE
                        text message to broadcast, surround with quotation
                        marks.
  -f FILE, --file FILE  path to a file that contains the message to broadcast
  -r REPEATS, --repeats REPEATS
                        number of times the message is to be repeated, default
                        1
  -g GAP, --gap GAP     gap time between repeats, in seconds, default 5.0
  -b BAUDMODE, --baudmode BAUDMODE
                        baudmode, default 300. Refer to
                        http://www.whence.com/minimodem/minimodem.1.html for
                        details
```

The broadcast module works by first encoding the text message into
an `.wav` audio file with [`minimodem`](http://www.whence.com/minimodem/),
then use [PiFm](http://www.icrobotics.co.uk/wiki/index.php/Turning_the_Raspberry_Pi_Into_an_FM_Transmitter)
to produce FM radio signals.

We used a Raspberry Pi 2 as broadcast device and ran the `broadcast` module on it.


## Listen Module
The `listen` module is meant to run on a motor vehicle's on-board computer.
It monitors FM radio signals and displays the message when one is being broadcast. 