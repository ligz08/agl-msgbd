import argparse
import subprocess
from pifm import PiFm
from time import sleep

class MinimodemEncoder:
    def __init__(self, audio_filename, baudmode):
        self.modem = subprocess.Popen(['minimodem', '-t', '-f', audio_filename, baudmode],
                                      stdin=subprocess.PIPE)
    
    def write(self, message):
        self.modem.stdin.write(message)
        
    def close(self):
        self.modem.stdin.close()
        self.modem.terminate()
        

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    message_sources = parser.add_mutually_exclusive_group()
    message_sources.add_argument('-m','--message', default='',
                                 help='text message to broadcast, surround with quotation marks.')
    message_sources.add_argument('-f', '--file',
                                 help='path to a file that contains the message to broadcast')
    parser.add_argument('-r','--repeats', type=int, default=1,
                        help='number of times the message is to be repeated, default 1')
    parser.add_argument('-g', '--gap', type=float, default=5.0,
                        help='gap time between repeats, in seconds, default 5.0')
    parser.add_argument('-b', '--baudmode', default='300',
                        help='baudmode, default 300. Refer to http://www.whence.com/minimodem/minimodem.1.html for '
                             'details')
    args = parser.parse_args()
    
    if args.file:
        with open(args.file, 'r') as f:
            message = f.read() or args.message
            
    encoder = MinimodemEncoder(audio_filename='message.wav', baudmode=args.baudmode)
    encoder.write(message)
    encoder.close()
    
    for repeat in range(int(args.repeats)):
        PiFm.play_sound('message.wav')
        sleep(float(args.gap))